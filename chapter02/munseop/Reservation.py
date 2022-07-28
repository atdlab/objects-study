from chapter02 import Screening
from chapter02.Customer import Customer
from chapter02.Money import Money


class Reservation:
    def __init__(self, customer:Customer, screening:Screening, fee:Money, audience_count:int):
        self._customer = customer
        self._screening = screening
        self._fee = fee
        self._audience_count = audience_count

