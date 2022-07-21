'''
2022-07-21 클래스 설계 후 제대로 된 클래스 구현을 위해 클래스별 파일을 분리하여 임시로 작성
'''

from gc import is_tracked


class Player:
    def __init__(self):
        self.hands = []
        self.is_traded = False
        self.mulligan = 2
    
    def getMulligan(self):
        return self.mulligan
    
    def setMulligan(self, Num : int):
        self.mulligan = Num

