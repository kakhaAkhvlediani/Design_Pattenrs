from typing import Protocol

from app.item import IItem


class ICashier(Protocol):
    def open_receipt(self):
        pass

    def add_item(self, item: IItem):
        pass

    def close_receipt(self):
        pass

    def make_z_report(self):
        pass

    def give_receipt(self):
        pass
