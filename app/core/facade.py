from dataclasses import dataclass

from app.core.receipt.interactor import (
    AddItemRequest,
    IMemoryRepository,
    IReceiptInteractor,
    ReceiptInteractor,
    ReceiptResponse,
)
from app.core.store.interactor import IStoreInteractor, StoreInteractor, XReportResponse


@dataclass
class StoreServiceCore:
    _receipt_interactor: IReceiptInteractor
    _store_interactor: IStoreInteractor

    @classmethod
    def create(cls, store_repository: IMemoryRepository) -> "StoreServiceCore":
        return cls(
            _receipt_interactor=ReceiptInteractor(store_repository),
            _store_interactor=StoreInteractor(store_repository),
        )

    def add_item(self, request: AddItemRequest) -> ReceiptResponse:
        return self._receipt_interactor.add_item(request)

    def open_receipt(self) -> ReceiptResponse:
        return self._receipt_interactor.open_receipt()

    def get_receipt(self) -> ReceiptResponse:
        return self._receipt_interactor.get_receipt()

    def close_receipt(self) -> ReceiptResponse:
        return self._receipt_interactor.close_receipt()

    def make_x_report(self) -> XReportResponse:
        return self._store_interactor.make_x_report()
