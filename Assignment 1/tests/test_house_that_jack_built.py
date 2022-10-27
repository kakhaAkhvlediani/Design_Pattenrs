from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Protocol

import pytest


@pytest.fixture()
def house_that_jack_built() -> Poem:
    return PoemLog(PoemPerformance(HouseThatJackBuilt()))


def test_recite_verse(house_that_jack_built: Poem) -> None:
    assert house_that_jack_built.recite_verse(1) == "This is the house that Jack built."
    assert (
        house_that_jack_built.recite_verse(2)
        == "This is the malt that lay in the house that Jack built."
    )
    assert house_that_jack_built.recite_verse(3) == (
        "This is "
        "the rat that ate "
        "the malt that lay in "
        "the house that Jack built."
    )
    assert house_that_jack_built.recite_verse(4) == (
        "This is "
        "the cat that killed "
        "the rat that ate "
        "the malt that lay in "
        "the house that Jack built."
    )
    assert house_that_jack_built.recite_verse(5) == (
        "This is "
        "the dog that worried "
        "the cat that killed "
        "the rat that ate "
        "the malt that lay in "
        "the house that Jack built."
    )
    assert house_that_jack_built.recite_verse(6) == (
        "This is "
        "the cow with the crumpled horn that tossed "
        "the dog that worried "
        "the cat that killed "
        "the rat that ate "
        "the malt that lay in "
        "the house that Jack built."
    )
    assert house_that_jack_built.recite_verse(7) == (
        "This is "
        "the maiden all forlorn that milked "
        "the cow with the crumpled horn that tossed "
        "the dog that worried "
        "the cat that killed "
        "the rat that ate "
        "the malt that lay in "
        "the house that Jack built."
    )
    assert house_that_jack_built.recite_verse(8) == (
        "This is "
        "the man all tattered and torn that kissed "
        "the maiden all forlorn that milked "
        "the cow with the crumpled horn that tossed "
        "the dog that worried "
        "the cat that killed "
        "the rat that ate "
        "the malt that lay in "
        "the house that Jack built."
    )
    assert house_that_jack_built.recite_verse(9) == (
        "This is "
        "the judge all shaven and shorn that married "
        "the man all tattered and torn that kissed "
        "the maiden all forlorn that milked "
        "the cow with the crumpled horn that tossed "
        "the dog that worried "
        "the cat that killed "
        "the rat that ate "
        "the malt that lay in "
        "the house that Jack built."
    )
    assert house_that_jack_built.recite_verse(10) == (
        "This is "
        "the rooster that crowed in the morn that woke "
        "the judge all shaven and shorn that married "
        "the man all tattered and torn that kissed "
        "the maiden all forlorn that milked "
        "the cow with the crumpled horn that tossed "
        "the dog that worried "
        "the cat that killed "
        "the rat that ate "
        "the malt that lay in "
        "the house that Jack built."
    )
    assert house_that_jack_built.recite_verse(11) == (
        "This is "
        "the farmer sowing his corn that kept "
        "the rooster that crowed in the morn that woke "
        "the judge all shaven and shorn that married "
        "the man all tattered and torn that kissed "
        "the maiden all forlorn that milked "
        "the cow with the crumpled horn that tossed "
        "the dog that worried "
        "the cat that killed "
        "the rat that ate "
        "the malt that lay in "
        "the house that Jack built."
    )
    assert house_that_jack_built.recite_verse(12) == (
        "This is "
        "the horse and the hound and the horn belonged to "
        "the farmer sowing his corn that kept "
        "the rooster that crowed in the morn that woke "
        "the judge all shaven and shorn that married "
        "the man all tattered and torn that kissed "
        "the maiden all forlorn that milked "
        "the cow with the crumpled horn that tossed "
        "the dog that worried "
        "the cat that killed "
        "the rat that ate "
        "the malt that lay in "
        "the house that Jack built."
    )


def test_recite(house_that_jack_built: Poem) -> None:
    assert house_that_jack_built.recite() == (
        "This is "
        "the house that Jack built.\n"
        "This is "
        "the malt that lay in "
        "the house that Jack built.\n"
        "This is "
        "the rat that ate "
        "the malt that lay in "
        "the house that Jack built.\n"
        "This is "
        "the cat that killed "
        "the rat that ate "
        "the malt that lay in "
        "the house that Jack built.\n"
        "This is "
        "the dog that worried "
        "the cat that killed "
        "the rat that ate "
        "the malt that lay in "
        "the house that Jack built.\n"
        "This is "
        "the cow with the crumpled horn that tossed "
        "the dog that worried "
        "the cat that killed "
        "the rat that ate "
        "the malt that lay in "
        "the house that Jack built.\n"
        "This is "
        "the maiden all forlorn that milked "
        "the cow with the crumpled horn that tossed "
        "the dog that worried "
        "the cat that killed "
        "the rat that ate "
        "the malt that lay in "
        "the house that Jack built.\n"
        "This is "
        "the man all tattered and torn that kissed "
        "the maiden all forlorn that milked "
        "the cow with the crumpled horn that tossed "
        "the dog that worried "
        "the cat that killed "
        "the rat that ate "
        "the malt that lay in "
        "the house that Jack built.\n"
        "This is "
        "the judge all shaven and shorn that married "
        "the man all tattered and torn that kissed "
        "the maiden all forlorn that milked "
        "the cow with the crumpled horn that tossed "
        "the dog that worried "
        "the cat that killed "
        "the rat that ate "
        "the malt that lay in "
        "the house that Jack built.\n"
        "This is "
        "the rooster that crowed in the morn that woke "
        "the judge all shaven and shorn that married "
        "the man all tattered and torn that kissed "
        "the maiden all forlorn that milked "
        "the cow with the crumpled horn that tossed "
        "the dog that worried "
        "the cat that killed "
        "the rat that ate "
        "the malt that lay in "
        "the house that Jack built.\n"
        "This is "
        "the farmer sowing his corn that kept "
        "the rooster that crowed in the morn that woke "
        "the judge all shaven and shorn that married "
        "the man all tattered and torn that kissed "
        "the maiden all forlorn that milked "
        "the cow with the crumpled horn that tossed "
        "the dog that worried "
        "the cat that killed "
        "the rat that ate "
        "the malt that lay in "
        "the house that Jack built.\n"
        "This is "
        "the horse and the hound and the horn belonged to "
        "the farmer sowing his corn that kept "
        "the rooster that crowed in the morn that woke "
        "the judge all shaven and shorn that married "
        "the man all tattered and torn that kissed "
        "the maiden all forlorn that milked "
        "the cow with the crumpled horn that tossed "
        "the dog that worried "
        "the cat that killed "
        "the rat that ate "
        "the malt that lay in "
        "the house that Jack built."
    )


class Poem(Protocol):
    def recite(self) -> str:
        pass

    def recite_verse(self, number: int) -> str:
        pass


@pytest.fixture()
def reverse_house_that_jack_built() -> Poem:
    return HouseThatJackBuilt(orderer=ReverseOrderer())


def test_revers_recite_verse(reverse_house_that_jack_built: Poem) -> None:
    assert reverse_house_that_jack_built.recite_verse(1) == (
        "This is the horse and the hound and the horn belonged to."
    )
    assert reverse_house_that_jack_built.recite_verse(12) == (
        "This is "
        "the house that Jack built "
        "the malt that lay in "
        "the rat that ate "
        "the cat that killed "
        "the dog that worried "
        "the cow with the crumpled horn "
        "that tossed the maiden all forlorn "
        "that milked the man all tattered and torn "
        "that kissed the judge all shaven and shorn "
        "that married the rooster that crowed in the morn "
        "that woke the farmer sowing his corn "
        "that kept the horse and the hound and the horn belonged to."
    )


@pytest.fixture
def yelling_house_that_jack_built() -> Poem:
    return HouseThatJackBuilt(formatter=YellingFormatter())


def test_yelling_recite_verse(yelling_house_that_jack_built: Poem) -> None:
    assert (
        yelling_house_that_jack_built.recite_verse(1)
        == "This is THE HOUSE THAT JACK BUILT."
    )
    assert yelling_house_that_jack_built.recite_verse(12) == (
        "This is "
        "THE HORSE AND THE HOUND AND THE HORN BELONGED TO "
        "THE FARMER SOWING HIS CORN THAT KEPT "
        "THE ROOSTER THAT CROWED IN THE MORN THAT WOKE "
        "THE JUDGE ALL SHAVEN AND SHORN THAT MARRIED "
        "THE MAN ALL TATTERED AND TORN THAT KISSED "
        "THE MAIDEN ALL FORLORN THAT MILKED "
        "THE COW WITH THE CRUMPLED HORN THAT TOSSED "
        "THE DOG THAT WORRIED "
        "THE CAT THAT KILLED "
        "THE RAT THAT ATE "
        "THE MALT THAT LAY IN "
        "THE HOUSE THAT JACK BUILT."
    )


def test_yelling_recite(yelling_house_that_jack_built: Poem) -> None:
    assert yelling_house_that_jack_built.recite() == (
        "This is "
        "THE HOUSE THAT JACK BUILT.\n"
        "This is "
        "THE MALT THAT LAY IN "
        "THE HOUSE THAT JACK BUILT.\n"
        "This is "
        "THE RAT THAT ATE "
        "THE MALT THAT LAY IN "
        "THE HOUSE THAT JACK BUILT.\n"
        "This is "
        "THE CAT THAT KILLED "
        "THE RAT THAT ATE "
        "THE MALT THAT LAY IN "
        "THE HOUSE THAT JACK BUILT.\n"
        "This is "
        "THE DOG THAT WORRIED "
        "THE CAT THAT KILLED "
        "THE RAT THAT ATE "
        "THE MALT THAT LAY IN "
        "THE HOUSE THAT JACK BUILT.\n"
        "This is "
        "THE COW WITH THE CRUMPLED HORN THAT TOSSED "
        "THE DOG THAT WORRIED "
        "THE CAT THAT KILLED "
        "THE RAT THAT ATE "
        "THE MALT THAT LAY IN "
        "THE HOUSE THAT JACK BUILT.\n"
        "This is "
        "THE MAIDEN ALL FORLORN THAT MILKED "
        "THE COW WITH THE CRUMPLED HORN THAT TOSSED "
        "THE DOG THAT WORRIED "
        "THE CAT THAT KILLED "
        "THE RAT THAT ATE "
        "THE MALT THAT LAY IN "
        "THE HOUSE THAT JACK BUILT.\n"
        "This is "
        "THE MAN ALL TATTERED AND TORN THAT KISSED "
        "THE MAIDEN ALL FORLORN THAT MILKED "
        "THE COW WITH THE CRUMPLED HORN THAT TOSSED "
        "THE DOG THAT WORRIED "
        "THE CAT THAT KILLED "
        "THE RAT THAT ATE "
        "THE MALT THAT LAY IN "
        "THE HOUSE THAT JACK BUILT.\n"
        "This is "
        "THE JUDGE ALL SHAVEN AND SHORN THAT MARRIED "
        "THE MAN ALL TATTERED AND TORN THAT KISSED "
        "THE MAIDEN ALL FORLORN THAT MILKED "
        "THE COW WITH THE CRUMPLED HORN THAT TOSSED "
        "THE DOG THAT WORRIED "
        "THE CAT THAT KILLED "
        "THE RAT THAT ATE "
        "THE MALT THAT LAY IN "
        "THE HOUSE THAT JACK BUILT.\n"
        "This is "
        "THE ROOSTER THAT CROWED IN THE MORN THAT WOKE "
        "THE JUDGE ALL SHAVEN AND SHORN THAT MARRIED "
        "THE MAN ALL TATTERED AND TORN THAT KISSED "
        "THE MAIDEN ALL FORLORN THAT MILKED "
        "THE COW WITH THE CRUMPLED HORN THAT TOSSED "
        "THE DOG THAT WORRIED "
        "THE CAT THAT KILLED "
        "THE RAT THAT ATE "
        "THE MALT THAT LAY IN "
        "THE HOUSE THAT JACK BUILT.\n"
        "This is "
        "THE FARMER SOWING HIS CORN THAT KEPT "
        "THE ROOSTER THAT CROWED IN THE MORN THAT WOKE "
        "THE JUDGE ALL SHAVEN AND SHORN THAT MARRIED "
        "THE MAN ALL TATTERED AND TORN THAT KISSED "
        "THE MAIDEN ALL FORLORN THAT MILKED "
        "THE COW WITH THE CRUMPLED HORN THAT TOSSED "
        "THE DOG THAT WORRIED "
        "THE CAT THAT KILLED "
        "THE RAT THAT ATE "
        "THE MALT THAT LAY IN "
        "THE HOUSE THAT JACK BUILT.\n"
        "This is "
        "THE HORSE AND THE HOUND AND THE HORN BELONGED TO "
        "THE FARMER SOWING HIS CORN THAT KEPT "
        "THE ROOSTER THAT CROWED IN THE MORN THAT WOKE "
        "THE JUDGE ALL SHAVEN AND SHORN THAT MARRIED "
        "THE MAN ALL TATTERED AND TORN THAT KISSED "
        "THE MAIDEN ALL FORLORN THAT MILKED "
        "THE COW WITH THE CRUMPLED HORN THAT TOSSED "
        "THE DOG THAT WORRIED "
        "THE CAT THAT KILLED "
        "THE RAT THAT ATE "
        "THE MALT THAT LAY IN "
        "THE HOUSE THAT JACK BUILT."
    )


DATA = [
    "the horse and the hound and the horn belonged to",
    "the farmer sowing his corn that kept",
    "the rooster that crowed in the morn that woke",
    "the judge all shaven and shorn that married",
    "the man all tattered and torn that kissed",
    "the maiden all forlorn that milked",
    "the cow with the crumpled horn that tossed",
    "the dog that worried",
    "the cat that killed",
    "the rat that ate",
    "the malt that lay in",
    "the house that Jack built",
]


class Orderer(Protocol):
    def order(self, items: list[str]) -> list[str]:
        pass


class DefaultOrderer:
    def order(self, items: list[str]) -> list[str]:
        return items


class ReverseOrderer:
    def order(self, items: list[str]) -> list[str]:
        return [*reversed(items)]


class Formatter(Protocol):
    def format(self, items: list[str]) -> list[str]:
        pass


class DefaultFormatter:
    def format(self, items: list[str]) -> list[str]:
        return items


class YellingFormatter:
    def format(self, items: list[str]) -> list[str]:
        return [item.upper() for item in items]


def yelling_reverse_house() -> Poem:
    return HouseThatJackBuilt(orderer=ReverseOrderer(), formatter=YellingFormatter())


# class                     | Order     |
# ---------------------------------------
# HouseThatJackBuilt        | default   |
# ReverseHouseThatJackBuilt | reverse   |
# ShuffleHouseThatJackBuilt | shuffle   |


@dataclass
class HouseThatJackBuilt:
    orderer: Orderer = field(default_factory=DefaultOrderer)
    formatter: Formatter = field(default_factory=DefaultFormatter)

    def recite(self) -> str:
        return "\n".join(self.recite_verse(i + 1) for i, _ in enumerate(self.lines))

    def recite_verse(self, number: int) -> str:
        return f"This is {' '.join(self.choose_phrases(number))}."

    def choose_phrases(self, count: int) -> list[str]:
        return self.formatter.format(self.lines[-count:])

    @property
    def lines(self) -> list[str]:
        return self.orderer.order(DATA)


@dataclass
class PoemDecorator:
    inner: Poem

    def recite(self) -> str:
        return self.inner.recite()

    def recite_verse(self, number: int) -> str:
        return self.inner.recite_verse(number)


@dataclass
class PoemPerformance(PoemDecorator):
    def recite(self) -> str:
        tic = time.perf_counter()
        lyrics = super().recite()
        toc = time.perf_counter()
        elapsed = toc - tic

        print(f"Elapsed time is {elapsed}")
        return lyrics


@dataclass
class PoemLog(PoemDecorator):
    pass
