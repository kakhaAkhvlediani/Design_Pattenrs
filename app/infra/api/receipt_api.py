from fastapi import APIRouter, Depends

from app.core.facade import StoreServiceCore
from app.core.receipt.interactor import AddItemRequest, ReceiptResponse
from app.infra.api.dependables import get_core

receipt_api = APIRouter()


@receipt_api.post("/receipts/open_receipt")
def open_receipt(core: StoreServiceCore = Depends(get_core)) -> ReceiptResponse:
    return core.open_receipt()


@receipt_api.get("/receipts")
def get_receipt(core: StoreServiceCore = Depends(get_core)) -> ReceiptResponse:
    response = core.get_receipt()
    return response


@receipt_api.post("/receipts/add_item/{item_name}")
def add_item(
        name: str,
        count: int,
        price: float,
        core: StoreServiceCore = Depends(get_core),
) -> ReceiptResponse:
    return core.add_item(request=AddItemRequest(name, count, price))


@receipt_api.post("/receipts/close_receipt")
def close_receipt(core: StoreServiceCore = Depends(get_core)) -> ReceiptResponse:
    return core.close_receipt()
