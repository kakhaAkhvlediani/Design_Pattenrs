from typing import List

import pytest

from app.core.receipt.interactor import IItem, Item, Receipt


@pytest.fixture
def items() -> List[IItem]:
    items: List[IItem] = [
        Item(_name="Cola", _price=2.0, _count=1),
        Item(_name="Fanta", _price=3.2, _count=1),
        Item(_name="Beer", _price=1.2, _count=7),
        Item(_name="Pasta", _price=1.5, _count=7),
    ]

    return items


def test_receipt_get(items: List[IItem]) -> None:
    receipt = Receipt(items)
    assert items == receipt.get_items()


def test_receipt_total_price(items: List[IItem]) -> None:
    receipt = Receipt(items)
    assert 24.1 == receipt.calculate_price()
