from dataclasses import dataclass, field
from typing import DefaultDict, Iterator, List, Optional, Protocol


class ICalculatePrice(Protocol):
    def calculate_price(self) -> float:
        pass


# ITEM
class IItem(Protocol):
    def calculate_price(self) -> float:
        pass

    def get_name(self) -> str:
        pass

    def get_count(self) -> int:
        pass

    def get_price(self) -> float:
        pass

    def __eq__(self, other: object) -> bool:
        pass

    def __hash__(self) -> int:
        pass


@dataclass
class Item:
    _name: str
    _count: int
    _price: float

    def calculate_price(self) -> float:
        return self.get_price() * self.get_count()

    def get_name(self) -> str:
        return self._name

    def get_count(self) -> int:
        return self._count

    def get_price(self) -> float:
        return self._price

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Item):
            return NotImplemented
        return (
            self.get_name() == other.get_name()
            and self.get_count() == other.get_count()
            and self.get_price() == other.get_price()
        )

    def __hash__(self) -> int:
        return hash((self.get_name(), self.get_count()))


# Receipt
class IReceipt(Protocol):
    def calculate_price(self) -> float:
        pass

    def get_items(self) -> List[IItem]:
        pass

    def get_receipt(self) -> List[dict[str, object]]:
        pass

    def __iter__(self) -> Iterator[IItem]:
        pass


class IReceiptBuilder(Protocol):
    def with_item(self, item: IItem) -> "IReceiptBuilder":
        pass

    def build(self) -> IReceipt:
        pass

    def clear(self) -> "IReceiptBuilder":
        pass


class ReceiptBuilder:
    def __init__(self, kwargs: Optional[List[IItem]] = None):
        self._kwargs = kwargs or []

    def with_item(self, item: IItem) -> IReceiptBuilder:
        self._kwargs.append(item)
        return self

    def build(self) -> IReceipt:
        return Receipt(self._kwargs)

    def clear(self) -> IReceiptBuilder:
        self._kwargs = []
        return self


@dataclass
class Receipt:
    _items: List[IItem]

    def calculate_price(self) -> float:
        price: float = 0.0

        for item in self._items:
            price += item.calculate_price()

        return price

    def get_items(self) -> List[IItem]:
        return self._items.copy()

    def get_receipt(self) -> List[dict[str, object]]:
        data = {}
        result = []
        for item in self:
            data = {
                "name": item.get_name(),
                "Units": item.get_count(),
                "price": item.get_price(),
                "total": item.calculate_price(),
            }

            result.append(data)

        return result

    def __iter__(self) -> Iterator[IItem]:
        return iter(self._items)


@dataclass
class ReceiptResponse:
    status: int
    receipt: List[dict[str, object]] = field(default_factory=lambda: [])


@dataclass
class AddItemRequest:
    name: str
    count: int
    price: float


class IReceiptInteractor(Protocol):
    def add_item(self, request: AddItemRequest) -> ReceiptResponse:
        pass

    def open_receipt(self) -> ReceiptResponse:
        pass

    def get_receipt(self) -> ReceiptResponse:
        pass

    def close_receipt(self) -> ReceiptResponse:
        pass


class IMemoryRepository(Protocol):
    def add_closed_receipt(self, receipt: IReceipt) -> None:
        pass

    def get_sold_items(self) -> DefaultDict[IItem, int]:
        pass

    def get_revenue(self) -> float:
        pass

    def get_receipt_count(self) -> int:
        pass


@dataclass
class ReceiptInteractor:
    _database: IMemoryRepository
    _current_receipt: Optional[IReceiptBuilder] = None

    def add_item(self, request: AddItemRequest) -> ReceiptResponse:
        if self._current_receipt is None:
            return ReceiptResponse(status=404)
        else:
            item = Item(_name=request.name, _count=request.count, _price=request.price)

            self._current_receipt.with_item(item)

            return ReceiptResponse(status=201)

    def open_receipt(self) -> ReceiptResponse:
        if self._current_receipt is None:
            self._current_receipt = ReceiptBuilder()
            return ReceiptResponse(status=201)
        else:
            return ReceiptResponse(status=403)

    def get_receipt(self) -> ReceiptResponse:
        if self._current_receipt is None:
            return ReceiptResponse(status=404)
        else:
            receipt = self._current_receipt.build().get_receipt()
            return ReceiptResponse(status=200, receipt=receipt)

    def close_receipt(self) -> ReceiptResponse:
        if self._current_receipt is None:
            return ReceiptResponse(status=404)
        else:
            receipt = self._current_receipt.build()
            self._current_receipt = None

            self._database.add_closed_receipt(receipt)

            return ReceiptResponse(status=200)
