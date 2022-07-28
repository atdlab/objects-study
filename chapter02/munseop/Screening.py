from __future__ import annotations
from datetime import datetime

from chapter02.Customer import Customer
from chapter02.Money import Money
from chapter02.Reservation import Reservation


class Movie:
    def __init__(self, title: str, running_time, fee: Money, discount_policy: DiscountPolicy):
        self._title = title
        self._running_time = running_time
        self._fee = fee
        self._discount_policy = discount_policy

    def get_fee(self) -> Money:
        return self._fee

    def calculate_movie_fee(self, screening: Screening) -> Money:
        return self._fee.minus(self._discount_policy.calculate_discount_amount(screening))


class Screening:
    def __init__(self, movie: Movie = None):
        self._movie = None
        pass

    def get_start_time(self) -> datetime:
        pass

    def get_movie_fee(self) -> Money:
        pass

    def is_sequence(self, screening: Screening) -> bool:
        pass

    def __calculate_fee(self, audience_count) -> Money:
        return self._movie.calculato_movie_fee(self).times(audience_count)

    def reserve(self, customer: Customer, audience_count: int) -> Reservation:
        return Reservation(customer, self, self.__calculate_fee(audience_count), audience_count)
