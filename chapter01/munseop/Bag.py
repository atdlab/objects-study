from Util import Util
from chapter01.Invitation import Invitation
from chapter01.Ticket import Ticket


class Bag:
    def __init__(self, **kwargs):
        args_dict = dict(kwargs)
        self._amount = Util.get_dict_value(args_dict, 'amount')
        self._invitation = Util.get_dict_value(args_dict, 'invitation')
        self._ticket = None

    def has_invitation(self):
        return self._invitation is not None

    def has_ticket(self):
        return self._ticket is not None

    # 개선 3
    # Audience에 수행되던 가방에 티켓을 넣는 행위를 가방으로 이동
    def hold(self, ticket: Ticket) -> int:
        if self.has_invitation():
            self.__set_ticket(ticket)
            return 0
        else:
            self.__set_ticket(ticket)
            self.__minus_amount(ticket.get_fee())
            return ticket.get_fee()

    # 개선 3
    # private 메소드로 변경

    # def set_ticket(self, ticket):
    #     self._ticket = ticket
    # def set_invitation(self, invitation):
    #     self._invitation = invitation
    #
    # def plus_amount(self, amount):
    #     self._amount = self._amount + amount
    #
    # def minus_amount(self, amount):
    #     self._amount = self._amount - amount

    def __set_ticket(self, ticket):
        self._ticket = ticket

    def __set_invitation(self, invitation):
        self._invitation = invitation

    def __plus_amount(self, amount):
        self._amount = self._amount + amount

    def __minus_amount(self, amount):
        self._amount = self._amount - amount
