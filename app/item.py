from typing import Protocol


class IItem(Protocol):
    name: str
    count: int

    def get_name(self):
        pass

    def get_count(self):
        pass

    # def __eq__(self, other):
    #     pass
    #
    # def __hash__(self):
    #     pass
