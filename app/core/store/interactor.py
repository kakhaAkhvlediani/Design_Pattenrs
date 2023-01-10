from collections import defaultdict
from dataclasses import dataclass
from typing import DefaultDict, Protocol

from app.core.receipt.interactor import IMemoryRepository


@dataclass
class XReportResponse:
    status: int
    sold_items: dict[str, int]
    total_revenue: float
    closed_receipts: int


class IStoreInteractor(Protocol):
    def make_x_report(self) -> XReportResponse:
        pass


@dataclass
class StoreInteractor:
    _database: IMemoryRepository

    def make_x_report(self) -> XReportResponse:
        sold_items = self._database.get_sold_items()

        x_report: DefaultDict[str, int] = defaultdict(int)

        for item in sold_items:
            x_report[item.get_name()] += item.get_count() * sold_items[item]

        total_revenue = round(self._database.get_revenue(), 2)
        closed_receipts = self._database.get_receipt_count()

        return XReportResponse(
            status=200,
            sold_items=dict(x_report),
            total_revenue=total_revenue,
            closed_receipts=closed_receipts,
        )
