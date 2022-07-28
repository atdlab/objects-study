from Util import Util
from chapter01.Bag import Bag
from chapter01.Ticket import Ticket


class Audience:
    def __init__(self, bag: Bag):
        self._bag = bag

    # 개선2
    # 외부에서 audience에 접근하지 못하도록 해당 메소드 삭제
    # def get_bag(self) -> Bag:
    #     return self._bag

    # 개선2
    # 개선1에서 Theater에 존재하던 로직을 TicketSeller로 옮겼으나 문제가 있으므로
    # 개선2에서 audience클래스로 일부로직을 이동한다.
    def buy(self, ticket: Ticket) -> int:
        # 개선 3
        # audience에서 bag에 깊이 결합되어 있어서 아래 메소드의 행위를 bag으로 이동한다.
        # if self._bag.has_invitation():
        #     self._bag.set_ticket()
        #     return 0
        # else:
        #     self._bag.set_ticket(ticket)
        #     self._bag.minus_amount(ticket.get_fee())
        #     return ticket.get_fee()
        return self._bag.hold(ticket)
