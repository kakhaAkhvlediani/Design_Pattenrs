from dataclasses import dataclass
from decimal import Decimal

import pytest

from app.wallet import Wallet, WalletWithBitfinexRates


@pytest.mark.vcr
def test_wallet_with_bitfinex_rates() -> None:
    wallet = WalletWithBitfinexRates()
    wallet.deposit(Decimal(2))
    wallet.withdraw(Decimal(1))

    assert wallet.balance_usd == Decimal(21581)


def test_wallet() -> None:
    rate = Decimal(21581)
    wallet = Wallet(FixedRateProvider(rate))
    wallet.deposit(Decimal(2))
    wallet.withdraw(Decimal(1))

    assert wallet.balance_usd == rate


@dataclass
class FixedRateProvider:
    rate: Decimal

    def fetch(self) -> Decimal:
        return self.rate
