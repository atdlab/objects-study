from __future__ import annotations


class Money:
    def __init__(self, amount: float):
        self._amount = amount

    @staticmethod
    def zero() -> Money:
        return Money(0)

    @staticmethod
    def wons(amount: int) -> Money:
        return Money(float(amount))

    @staticmethod
    def wons(amount: float) -> Money:
        return Money(amount)

    def plus(self, amount: Money) -> Money:
        return Money(self._amount.__add__(amount._amount))

    def minus(self, amount: Money) -> Money:
        return Money(self._amount.__sub__(amount._amount))

    def times(self, amount: float) -> Money:
        return Money(self._amount.__mul__(amount))

    def is_less_than(self, other: Money) -> bool:
        return self._amount < other._amount

    def is_greate_than_or_equal(self, other:Money) -> bool:
        return self._amount >= other._amount
