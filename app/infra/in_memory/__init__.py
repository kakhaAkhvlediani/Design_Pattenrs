from collections import defaultdict
from typing import DefaultDict

from app.core.receipt.interactor import IItem, IReceipt


class InMemoryRepository:
    _sold_items: DefaultDict[IItem, int]
    _closed_receipts: int

    def __init__(self) -> None:
        self._sold_items = defaultdict(int)
        self._closed_receipts = 0

    def add_closed_receipt(self, receipt: IReceipt) -> None:
        for item in receipt:
            self._sold_items[item] += 1

        self._closed_receipts += 1

    def get_sold_items(self) -> DefaultDict[IItem, int]:
        return self._sold_items.copy()

    def get_revenue(self) -> float:
        revenue = 0.0

        for sold_item in self._sold_items:
            revenue += sold_item.calculate_price() * self._sold_items[sold_item]

        return revenue

    def get_receipt_count(self) -> int:
        return self._closed_receipts
