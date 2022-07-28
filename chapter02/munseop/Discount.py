from abc import *
from datetime import datetime

from chapter02.Money import Money
from chapter02.Screening import Screening


class DiscountCondition(metaclass=ABCMeta):
    @abstractmethod
    def is_satisfied_by(self, screening: Screening) -> bool:
        raise NotImplementedError


class SequenceCondition(DiscountCondition):
    def __init__(self, sequence: int):
        self._sequence = sequence

    def is_satisfied_by(self, screening: Screening) -> bool:
        return screening.is_sequence(screening)


class PeriodCondition(DiscountCondition):
    def __init__(self, day_of_week: str, start_time: datetime, end_time: datetime):
        self._day_of_week = day_of_week
        self._start_time = start_time
        self._end_time = end_time

    def is_satisfied_by(self, screening: Screening) -> bool:
        return (
                (screening.get_start_time() is None or screening.get_start_time().strftime('%A') == self._day_of_week)
                and (screening.get_start_time() is None or (self._start_time >= screening.get_start_time()
                                                            and self._end_time >= screening.get_start_time()))
        )


class DiscountPolicy(metaclass=ABCMeta):
    def calculate_discount_amount(self, screening: Screening) -> Money:
        raise NotImplementedError


class DefaultDiscountPolicy(DiscountPolicy):
    def __init__(self, conditions: list):
        self._conditions = conditions

    def calculate_discount_amount(self, screening: Screening) -> Money:
        for condition in self._conditions:
            if condition.is_satisfied_by(screening) is True:
                return self.get_discount_amount(screening)

        return Money.zero()

    @abstractmethod
    def get_discount_amount(self, screening: Screening):
        pass


class AmountDiscountPolicy(DefaultDiscountPolicy, DiscountPolicy):
    def __init__(self, discount_amount: Money, conditions: list):
        super().__init__(conditions)
        self._discount_amount = discount_amount

    def get_discount_amount(self, screening: Screening):
        return self._discount_amount


class PercentDiscountPolicy(DefaultDiscountPolicy, DiscountPolicy):
    def __init__(self, percent: float, conditions: list):
        super().__init__(conditions)
        self._percent = percent

    def get_discount_amount(self, screening: Screening):
        return screening.get_movie_fee().times(self._percent)


class NoneDiscountPolicy(DiscountPolicy):

    def calculate_discount_amount(self, screening: Screening) -> Money:
        return Money.zero()
#
# ndc = NoneDiscountPolicy([SequenceCondition(1), PeriodCondition('Monday', datetime.now(), datetime.now())])
# ndc.calculate_discount_amount(Screening())
