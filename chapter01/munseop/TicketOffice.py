from Util import Util
from chapter01.Audience import Audience


class TicketOffice:
    def __init__(self, amount: int, tickets: []):
        self._amount = amount
        self._tickets = tickets

    def sell_ticket_to(self, audience:Audience):
        self.__plus_amount(audience.buy(self.__get_ticket()))

    #개선4
    def __get_ticket(self):
        target = self._tickets[0]
        self._tickets.remove(target)
        return target

    def __minus_amount(self, amount):
        self._amount = self._amount - amount

    def __plus_amount(self, amount):
        self._amount = self._amount + amount

#
# ticket_office = TicketOffice(amount=100, tickets=[0, 1, 2])
# print(ticket_office.get_ticket())
