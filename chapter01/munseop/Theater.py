from chapter01.Audience import Audience
from chapter01.TicketSeller import TicketSeller


class Theater:
    def __init__(self, ticket_seller:TicketSeller):
        self._ticket_seller = ticket_seller

    def enter(self, audience:Audience):
        self._ticket_seller.sell_to(audience)
        # 개선1
        # 아래의 코드는 theater가 audience와 tickets_seller뿐만 아니라, audience 소유의 bag과 ticket_seller가 근무하는 ticket_office까지
        # 마음대로 접근 할 수 있다. --> audience와 ticket_seller가 직접 bag과 ticket_office를 처리하는 자율적인 존재가 되도록 설계를 변경한다.
        # 따라서 해당 아래의 내용은 ticket_seller의 sell_to로 이동한다.
        # if audience.get_bag().has_invitation() is True:
        #     ticket = self._ticket_seller.get_ticket_office().get_ticket()
        #     audience.get_bag().set_ticket(ticket)
        # else:
        #     ticket = self._ticket_seller.get_ticket_office().get_ticket()
        #     audience.get_bag().minus_amount(ticket.get_fee())
        #     self._ticket_seller.get_ticket_office().plus_amount(ticket.get_fee())
        #     audience.get_bag().set_ticket(ticket)

