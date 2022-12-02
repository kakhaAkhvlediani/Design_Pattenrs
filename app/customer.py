from typing import Protocol

from app.receipt import IReceipt


class ICustomer(Protocol):
    receipt: IReceipt = None

    def show_receipt(self):
        pass

    def get_receipt(self):
        pass

    def pay(self):
        pass
