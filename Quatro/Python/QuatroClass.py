'''
카드 클래스
카드는 빨강, 파랑, 노랑, 초록, 검정 카드로 이루어져있다.
검정색 카드는 0카드 2개만 존재하며, 나머지 4가지 색의 카드는 1~6까지 존재한다
생성자를 통해 색, 숫자를 입력받아 객체를 생성한다
'''

class Card:
    def __init__(self, color, num):
        self.color = color
        self.num = num
        self.visible = False

'''
가상 플레이어 클래스
가상 플레이어는 플레이어들과 교환을 진행하는 객체이다.
두 플레이어와의 교환을 각각 1번씩 해야하므로 두 플레이어에 대한 교환 여부를 boolean 자료형으로 받는다.
그리고 교환할 카드가 담길 리스트를 만들어둔다.
'''

class Vplayer:
    hands = []
    def __init__(self):
        self.is_traded = [False, False]

'''
플레이어 클래스
플레이어는 최대 4장의 카드를 들고 있을 수 있는 핸드 리스트와, 카드가 오픈된 리스트를 가진다.
또한, 처음 손패가 안 좋을때 새로 교환할 수 있는 멀리건 횟수를 생성할 때 2회로 초기화해준다.
'''
class Player:
    hands = []
    opened = []
    def __init__(self):
        self.mulligan = 2