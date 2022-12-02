from typing import Protocol


class IReceipt(Protocol):
    def calculate_amount(self):
        pass
