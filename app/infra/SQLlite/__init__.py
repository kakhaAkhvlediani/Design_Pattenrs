import sqlite3 as database
from collections import defaultdict
from sqlite3 import Cursor
from typing import DefaultDict

from app.core.receipt.interactor import IItem, IReceipt, Item


class SQLiteStoreRepository:
    def __init__(self) -> None:
        self._database_name = "store.db"
        self._number_of_receipts = 0

        with database.connect(self._database_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS sold_items
                    (
                    id INTEGER PRIMARY KEY NOT NULL,
                    name TEXT NOT NULL,
                    count INTEGER NOT NULL,
                    price FLOAT NOT NULL,
                    receipt_id INTEGER NOT NULL
                    );"""
            )

    def add_closed_receipt(self, receipt: IReceipt) -> None:
        self._number_of_receipts += 1

        with database.connect(self._database_name) as conn:
            cursor = conn.cursor()

            for item in receipt:
                self._add_sold_item(item, self._number_of_receipts, cursor)

            conn.commit()

    def get_sold_items(self) -> DefaultDict[IItem, int]:
        sold_items: DefaultDict[IItem, int] = defaultdict(int)

        with database.connect(self._database_name) as conn:
            cursor: Cursor = conn.cursor()
            cursor.execute("SELECT * FROM sold_items")

            rows: list = cursor.fetchall()

            for item_tuple in rows:
                item: IItem = Item(
                    _name=item_tuple[1], _count=item_tuple[2], _price=item_tuple[3]
                )

                sold_items[item] += 1

        return sold_items

    def get_revenue(self) -> float:
        revenue: float = 0.0

        sold_items: DefaultDict[IItem, int] = self.get_sold_items()

        for item in sold_items:
            revenue += item.calculate_price() * sold_items[item]

        return revenue

    def get_receipt_count(self) -> int:
        return self._number_of_receipts

    def _add_sold_item(self, item: IItem, receipt_id: int, cursor: Cursor) -> None:
        command = """ INSERT INTO sold_items
                        (name, count, price, receipt_id)
                        VALUES(?,?,?,?) """
        data = (
            item.get_name(),
            item.get_count(),
            item.get_price(),
            receipt_id,
        )

        cursor.execute(command, data)
