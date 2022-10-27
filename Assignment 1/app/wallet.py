from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from typing import Protocol

import httpx
import requests
from httpx import HTTPError, HTTPStatusError
from requests import HTTPError


@dataclass
class WalletWithBitfinexRates:
    balance: Decimal = field(default_factory=Decimal)

    URL = f"https://api.bitfinex.com/v2/ticker/tBTCUSD"

    def deposit(self, btc: Decimal) -> None:
        self.balance += btc

    def withdraw(self, btc: Decimal) -> None:
        self.balance -= btc

    @property
    def balance_usd(self) -> Decimal:
        return requests.get(self.URL).json()[0] * self.balance


@dataclass
class Wallet:
    rate_provider: RateProvider
    balance: Decimal = field(default_factory=Decimal)

    def deposit(self, btc: Decimal) -> None:
        self.balance += btc

    def withdraw(self, btc: Decimal) -> None:
        self.balance -= btc

    @property
    def balance_usd(self) -> Decimal:
        return self.rate_provider.fetch() * self.balance


class RateProvider(Protocol):
    def fetch(self) -> Decimal:
        pass


class FailingProvider:
    def fetch(self) -> Decimal:
        raise FetchRateError


@dataclass
class BitfinexRateProvider:
    http_client: HttpClient
    next_provider: RateProvider = field(default_factory=FailingProvider)

    _URL = f"https://api.bitfinex.com/v2/ticker/tBTCUSD"

    def fetch(self) -> Decimal:
        try:
            response_json = self.http_client.get(self._URL)
        except FetchRateError:
            return self.next_provider.fetch()

        return Decimal(response_json[0])


class HttpClient(Protocol):
    def get(self, url: str) -> dict | list:
        pass


class FetchRateError(Exception):
    pass


class HttpxClient:
    def get(self, url: str) -> dict | list:
        response = httpx.get(url)

        try:
            response.raise_for_status()
        except HTTPStatusError:
            raise FetchRateError

        return response.json()


class RequestsClient:
    def get(self, url: str) -> dict | list:
        response = requests.get(url)

        try:
            response.raise_for_status()
        except HTTPError:
            raise FetchRateError

        return response.json()


bitfinex = BitfinexRateProvider(http_client=HttpxClient())


@dataclass
class GeminiRateProvider:
    http_client: HttpClient
    next_provider: RateProvider = field(default_factory=FailingProvider)

    _URL = f"https://api.gemini.com/v1/pubticker/btsusd"

    def fetch(self) -> Decimal:
        try:
            response_json = self.http_client.get(self._URL)
        except FetchRateError:
            return self.next_provider.fetch()

        return Decimal(response_json["last"])


gemini = GeminiRateProvider(http_client=HttpxClient())


@dataclass(frozen=True)
class AverageRateProvider:
    providers: list[RateProvider]

    def fetch(self) -> Decimal:
        rates = [provider.fetch() for provider in self.providers]

        return sum(rates) / len(self.providers)


Wallet(rate_provider=AverageRateProvider([bitfinex, gemini]))

Wallet(
    rate_provider=BitfinexRateProvider(
        http_client=RequestsClient(),
        next_provider=GeminiRateProvider(
            http_client=HttpxClient(),
        ),
    )
)
