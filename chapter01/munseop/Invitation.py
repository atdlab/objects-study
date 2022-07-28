from datetime import datetime

# 초대장 구현
class Invitation:
    def __init__(self):
        self._when: datetime = None # 관람일자
