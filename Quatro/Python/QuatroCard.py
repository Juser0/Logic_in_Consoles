'''
2022-07-21 클래스 설계 후 제대로 된 클래스 구현을 위해 클래스별 파일을 분리하여 임시로 작성
'''

class Card:
    def __init__(self):
        self.color = 'Black' # 초기 카드는 검은색 0으로 초기화
        self.num = 0 # 초기 카드는 검은색 0으로 초기화
        self.visible = False # 초기 카드의 보여줌 여부 설정 (가상플레이어, 본인 카드 표시여부)

    def getColor(self):
        return self.color

    def getNum(self):
        return self.num

    def getVisible(self):
        return self.visible

    def setColor(self, color: str):
        self.color = color

    def setNum(self, num : int):
        self.num = num

    def setVisible(self, Status: bool):
        self.visible = Status
