from typing import List

import pytest

from app.core.facade import StoreServiceCore
from app.core.receipt.interactor import AddItemRequest, ReceiptResponse
from app.infra.in_memory import InMemoryRepository


@pytest.fixture
def service() -> StoreServiceCore:
    store_repository: InMemoryRepository = InMemoryRepository()

    return StoreServiceCore.create(store_repository=store_repository)


def test_get_initialized_empty_receipt(service: StoreServiceCore) -> None:
    result: ReceiptResponse = service.open_receipt()
    assert result.status == 201

    result = service.get_receipt()
    assert result.status == 200
    assert result.receipt == []


def test_get_not_initialized_receipt(service: StoreServiceCore) -> None:
    result: ReceiptResponse = service.get_receipt()
    assert result.status == 404
    assert result.receipt == []


def test_get_receipt_with_one_item(service: StoreServiceCore) -> None:
    request: AddItemRequest = AddItemRequest(name="Tooth", count=1, price=40.30)

    result: ReceiptResponse = service.open_receipt()
    assert result.status == 201

    result = service.add_item(request)
    assert result.status == 201

    result = service.get_receipt()
    expected: List[dict[str, str | float | int]] = [
        {"Units": 1, "name": "Tooth", "price": 40.3, "total": 40.3}
    ]

    assert result.status == 200
    assert result.receipt == expected


def test_get_receipt_with_multiple_item(service: StoreServiceCore) -> None:
    request: AddItemRequest = AddItemRequest(name="Brain", count=1, price=40.30)

    result: ReceiptResponse = service.open_receipt()
    assert result.status == 201

    result = service.add_item(request)
    assert result.status == 201

    result = service.add_item(request)
    assert result.status == 201

    result = service.add_item(request)
    assert result.status == 201

    request = AddItemRequest(name="Beer", count=3, price=20.0)

    result = service.add_item(request)
    assert result.status == 201

    result = service.get_receipt()
    assert result.status == 200
    expected: List[dict[str, str | float | int]] = [
        {"name": "Brain", "Units": 1, "price": 40.3, "total": 40.3},
        {"name": "Brain", "Units": 1, "price": 40.3, "total": 40.3},
        {"name": "Brain", "Units": 1, "price": 40.3, "total": 40.3},
        {"name": "Beer", "Units": 3, "price": 20.0, "total": 60.0},
    ]
    assert result.receipt == expected


def test_get_receipt_after_adding_mult_items_and_closing(
    service: StoreServiceCore,
) -> None:
    request: AddItemRequest = AddItemRequest(name="Vodka", count=1, price=40.30)

    result: ReceiptResponse = service.open_receipt()
    assert result.status == 201

    result = service.add_item(request)
    assert result.status == 201

    result = service.add_item(request)
    assert result.status == 201

    result = service.add_item(request)
    assert result.status == 201

    request = AddItemRequest(name="Beer", count=3, price=20.0)

    result = service.add_item(request)
    assert result.status == 201

    result = service.get_receipt()
    assert result.status == 200
    expected: List[dict[str, str | float | int]] = [
        {"name": "Vodka", "Units": 1, "price": 40.3, "total": 40.3},
        {"name": "Vodka", "Units": 1, "price": 40.3, "total": 40.3},
        {"name": "Vodka", "Units": 1, "price": 40.3, "total": 40.3},
        {"name": "Beer", "Units": 3, "price": 20.0, "total": 60.0},
    ]
    assert result.receipt == expected

    result = service.close_receipt()
    assert result.status == 200

    result = service.get_receipt()
    assert result.status == 404
