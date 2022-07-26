class Card:
    def __init__(self):
        self.__color = 'Black' # 초기 카드는 검은색 0으로 초기화
        self.__num = 0 # 초기 카드는 검은색 0으로 초기화
        self.__visible = False # 초기 카드의 보여줌 여부 설정 (가상플레이어, 본인 카드 표시여부)
    
    @property
    def color(self):
        return self.__color

    @property
    def num(self):
        return self.__num

    @property
    def visible(self):
        return self.__visible

    @color.setter
    def color(self, color: str):
        self.__color = color

    @num.setter
    def num(self, num : int):
        self.__num = num

    @visible.setter
    def visible(self, visible: bool):
        self.__visible = visible
