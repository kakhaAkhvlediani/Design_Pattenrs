# Let q(x) be a property provable about objects of x of type T.
# Then q(y) should be provable for objects y of type S where S is a subtype of T.
from dataclasses import dataclass


@dataclass
class Rect:
    width: int = 0
    height: int = 0

    def set_w(self, width: int) -> None:
        self.width = width

    def set_h(self, height: int) -> None:
        self.height = height

    def area(self) -> int:
        return self.height * self.width


@dataclass
class Square:
    size: int

    def __init__(self, size: int) -> None:
        self.size = size

    def set_w(self, width: int) -> None:
        self.size = width

    def set_h(self, height: int) -> None:
        self.size = height

    def area(self) -> int:
        return self.size * self.size


def test_should_calculate_area() -> None:
    rect = Square(3)
    rect.set_h(5)
    rect.set_w(10)

    assert rect.area() == 50
