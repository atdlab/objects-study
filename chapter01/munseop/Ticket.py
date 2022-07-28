# 공연을 관람하기 위한 티켓 객체
class Ticket:
    def __init__(self):
        self._fee: int = None

    def get_fee(self):
        return self._fee
