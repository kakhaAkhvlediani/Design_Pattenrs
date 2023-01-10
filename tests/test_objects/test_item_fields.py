import pytest

from app.core.receipt.interactor import IItem, Item


@pytest.fixture
def item() -> IItem:
    return Item("Cow", 3, 3.0)


def test_item_name(item: IItem) -> None:
    assert item.get_name() == "Cow"


def test_count(item: IItem) -> None:
    assert item.get_count() == 3


def test_single_item_price(item: IItem) -> None:
    assert item.get_price() == 3.0


def test_items_total_price(item: IItem) -> None:
    assert item.calculate_price() == 9.0
