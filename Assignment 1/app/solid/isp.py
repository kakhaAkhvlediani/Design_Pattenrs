# Clients should not be forced to depend on methods they do not use.
from typing import Protocol


class OperatorImpl:
    def op1(self) -> None:
        pass

    def op2(self) -> None:
        pass


class Operator1(Protocol):
    def op1(self):
        pass


class Operator2(Protocol):
    def op2(self):
        pass


class Operator(Operator1, Operator2):
    pass


class User1:
    operator: Operator1

    def use(self):
        self.operator.op1()


class User2:
    operator: Operator2

    def use(self):
        self.operator.op2()


class User3:
    operator: Operator
