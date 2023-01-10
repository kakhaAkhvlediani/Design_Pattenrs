import pytest

from app.core.facade import StoreServiceCore
from app.core.receipt.interactor import AddItemRequest, ReceiptResponse
from app.infra.in_memory import InMemoryRepository


@pytest.fixture
def service() -> StoreServiceCore:
    store_repository: InMemoryRepository = InMemoryRepository()

    return StoreServiceCore.create(store_repository=store_repository)


def test_open_receipt(service: StoreServiceCore) -> None:
    result: ReceiptResponse = service.open_receipt()

    assert result.status == 201


def test_add_item_to_opened_receipt(service: StoreServiceCore) -> None:
    request: AddItemRequest = AddItemRequest(name="Brain", count=1, price=40.30)

    result: ReceiptResponse = service.open_receipt()
    assert result.status == 201

    result = service.add_item(request)
    assert result.status == 201


def test_add_item_to_closed_receipt(service: StoreServiceCore) -> None:
    request: AddItemRequest = AddItemRequest(name="Brain", count=1, price=40.30)

    result: ReceiptResponse = service.open_receipt()
    assert result.status == 201

    result = service.add_item(request)
    assert result.status == 201


def test_add_one_item_to_receipt(service: StoreServiceCore) -> None:
    request: AddItemRequest = AddItemRequest(name="Brain", count=1, price=40.30)

    result: ReceiptResponse = service.open_receipt()
    assert result.status == 201

    result = service.add_item(request)
    assert result.status == 201


def test_add_several_item_to_receipt(service: StoreServiceCore) -> None:
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
