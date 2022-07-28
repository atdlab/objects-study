from chapter01.Audience import Audience
from chapter01.TicketOffice import TicketOffice


class TicketSeller:
    def __init__(self, ticket_office: TicketOffice):
        self._ticket_office = ticket_office

    # 개선1
    # ticket_office의 캡슐화를 위하여 해당 메소드 삭제
    # def get_ticket_office(self):
    #     return self._ticket_office

    def sell_to(self, audience: Audience):
        # 개선2
        # 아래의 코드는 ticket_seller가 audience에 접근하여 결합도가 높으므로 개선한다.
        # if audience.get_bag().has_invitation() is True:
        #     ticket = self._ticket_seller.get_ticket_office().get_ticket()
        #     audience.get_bag().set_ticket(ticket)
        # else:
        #     ticket = self._ticket_seller.get_ticket_office().get_ticket()
        #     audience.get_bag().minus_amount(ticket.get_fee())
        #     self._ticket_seller.get_ticket_office().plus_amount(ticket.get_fee())
        #     audience.get_bag().set_ticket(ticket)

        # 개선 4
        # self._ticket_office.plus_amount(audience.buy(self._ticket_office.get_ticket()))
        self._ticket_office.sell_ticket_to(audience)