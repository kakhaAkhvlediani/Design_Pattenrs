import pytest

from app.core.facade import StoreServiceCore
from app.core.receipt.interactor import AddItemRequest, ReceiptResponse
from app.infra.in_memory import InMemoryRepository


@pytest.fixture
def service() -> StoreServiceCore:
    store_repository: InMemoryRepository = InMemoryRepository()

    return StoreServiceCore.create(store_repository=store_repository)


def test_open_and_close_receipt(service: StoreServiceCore) -> None:
    result: ReceiptResponse = service.open_receipt()
    assert result.status == 201

    result = service.close_receipt()
    assert result.status == 200


def test_close_closed_receipt(service: StoreServiceCore) -> None:
    result = service.open_receipt()
    assert result.status == 201

    result = service.close_receipt()
    assert result.status == 200

    result = service.close_receipt()
    assert result.status == 404


def test_close_unopened_receipt(service: StoreServiceCore) -> None:
    result: ReceiptResponse = service.close_receipt()
    assert result.status == 404
    assert result.receipt == []


def test_add_item_to_closed_receipt(service: StoreServiceCore) -> None:
    request: AddItemRequest = AddItemRequest(name="Brain", count=1, price=40.30)

    result: ReceiptResponse = service.add_item(request)
    assert result.status == 404
