import pytest

from app.core.facade import StoreServiceCore
from app.core.receipt.interactor import AddItemRequest, ReceiptResponse
from app.core.store.interactor import XReportResponse

# from app.core.receipt.interactor import ReceiptResponse, AddItemRequest
from app.infra.in_memory import InMemoryRepository


@pytest.fixture
def service() -> StoreServiceCore:
    store_repository: InMemoryRepository = InMemoryRepository()

    return StoreServiceCore.create(store_repository=store_repository)


def test_make_x_report_empty(service: StoreServiceCore) -> None:
    result = service.make_x_report()
    assert result.status == 200

    assert result.total_revenue == 0
    assert result.closed_receipts == 0

    assert result.sold_items == dict()


def test_make_x_report_with_one_item_in_open_receipt(service: StoreServiceCore) -> None:
    request: AddItemRequest = AddItemRequest(name="Brain", count=1, price=40.30)

    receipt_result: ReceiptResponse = service.open_receipt()
    assert receipt_result.status == 201

    receipt_result = service.add_item(request)
    assert receipt_result.status == 201

    report_result: XReportResponse = service.make_x_report()

    assert report_result.status == 200

    assert report_result.total_revenue == 0
    assert report_result.closed_receipts == 0

    assert report_result.sold_items == dict()


def test_make_x_report_with_one_sold_item(service: StoreServiceCore) -> None:
    request: AddItemRequest = AddItemRequest(name="Ketchup", count=2, price=10.30)

    receipt_result: ReceiptResponse = service.open_receipt()
    assert receipt_result.status == 201

    receipt_result = service.add_item(request)
    assert receipt_result.status == 201

    report_result: XReportResponse = service.make_x_report()

    assert report_result.status == 200

    assert report_result.total_revenue == 0
    assert report_result.closed_receipts == 0

    assert report_result.sold_items == dict()

    receipt_result = service.close_receipt()

    report_result = service.make_x_report()

    assert report_result.status == 200

    assert report_result.total_revenue == 20.6
    assert report_result.closed_receipts == 1

    expected: dict[str, int] = {"Ketchup": 2}
    assert report_result.sold_items == expected


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

    result = service.close_receipt()
    assert result.status == 200

    report_result: XReportResponse = service.make_x_report()

    assert report_result.status == 200

    assert report_result.closed_receipts == 1
    assert report_result.total_revenue == 180.9

    expected: dict[str, int] = {"Brain": 3, "Beer": 3}
    assert report_result.sold_items == expected
