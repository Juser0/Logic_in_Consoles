import random
import os

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
        self.is_traded0 = False
        self.is_traded1 = False

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

def print_Deck(list_name):
    for i in range(len(list_name)):
        print("Color : " + list_name[i].color + " / Num : " + str(list_name[i].num))

def print_Players(list_name):
    for i in range(len(list_name)):
        print(str(i + 1) + "번", end = '   ')
        for j in range(3):
            if list_name[i].hands[j].visible == True:
                print(str(list_name[i].hands[j].color) + ' ' + str(list_name[i].hands[j].num) + ' ', end = '  ')
            else:
                print('X ', end = '  ')

def trade(wp, to, gived):
    take = Card('Black', 0)
    for i in range(len(players[wp].opened)):
        for j in range(3):
            if Vplayers[to - 1].hands[j].num == 0:
                Vplayers[to - 1].hands[j] = gived
                Vplayers[to - 1].hands[j].visible = True
                return take
            elif players[wp].opened.find(Vplayers[to - 1].hands[j].num) == -1 and players[wp].opened.find(Vplayers[to - 1].hands[j].color) == -1:
                take = Vplayers[to - 1].hands[j]
            else:
                if take.num < Vplayers[to - 1].hands[j].num:
                    take = Vplayers[to - 1].hands[j]
                elif take.num == Vplayers[to - 1].hands[j].num:
                    if len(take.color) == 5 and len(Vplayers[to - 1].hands[j].color) == 6:
                        take = Vplayers[to - 1].hands[j]
                    elif len(take.color) > len(Vplayers[to - 1].hands[j].color) and len(Vplayers[to - 1].hands[j].color) != 5:
                        take = Vplayers[to - 1].hands[j]
    idx = Vplayers[to - 1].hands.index(take)
    Vplayers[to - 1].hands[idx] = gived
    return take

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

deck = [] # 덱
Vplayers = [] # 가상 플레이어
players = [] # 실제 플레이어
turn = 0 # n번 플레이어의 턴임을 확인시킴
is_trade = False # 교환 여부를 확인시킴

# 가상 플레이어 6인의 객체 추가
for i in range(6): 
    Vplayers.append(Vplayer())

# 실제 플레이어 2인의 객체 추가
for i in range(2):
    players.append(Player())

# 카드 덱에 추가
for i in range(26):
    if i < 6:
        deck.append(Card('Red', i + 1))
    elif i < 12:
        deck.append(Card('Blue', i - 5))
    elif i < 18:
        deck.append(Card('Yellow', i - 11))
    elif i < 24:
        deck.append(Card('Green', i - 17))
    else:
        deck.append(Card('Black', 0))

random.shuffle(deck)

# 첫 손패 배분
# 플레이어 0번이 선공, 플레이어 1번이 후공이라 가정 (플레이어 0 - 본인, 플레이어 2 - 컴퓨터)
players[0].hands = deck[:4]
del deck[:4]
players[1].hands = deck[:4]
del deck[:4]
print_Deck(players[0].hands)

# print()
# print_Deck(players[1].hands)
# print()
# print_Deck(deck)

'''
멀리건 타임
플레이어는 첫 손패가 좋지 않다고 판단될 때, 멀리건을 최대 2회 요청할 수 있다.
멀리건의 순서는 선 - 후 - 후 - 선의 순서대로 진행된다
'''
while players[0].mulligan > 0 or players[1].mulligan > 0:
    if turn == 0:
        is_mul = input("멀리건 진행하시겠습니까? (예, Y, Yes면 진행, 이외는 진행 X) : ")
        if is_mul == 'Y' or is_mul == 'y' or is_mul == 'Yes' or is_mul == 'yes' or is_mul == '예':
            players[0].mulligan -= 1
            deck.extend(players[0].hands)
            players[0].hands = deck[:4]
            del deck[:4]
            print('플레이어 1님, 멀리건을 진행합니다. 남은 멀리건 횟수는 ' + str(players[0].mulligan) + '회 입니다')
            print_Deck(players[0].hands)
        else:
            players[0].mulligan = 0
        turn = 1
    else:
        snum = 0
        for i in range(len(players[1].hands)):
            snum += players[1].hands[i].num
        if snum < 14:
            players[1].mulligan -= 1 
            deck.extend(players[1].hands)
            players[1].hands = deck[:4]
            del deck[:4]
            print('플레이어 2님, 멀리건을 진행합니다. 남은 멀리건 횟수는 ' + str(players[1].mulligan) + '회 입니다')
        else:
            players[1].mulligan = 0

        if players[1].mulligan == 0:
            turn = 0

# 덱 셔플 후 가상 플레이어에게 카드 전달
random.shuffle(deck)
for i in range(len(Vplayers)):
    Vplayers[i].hands = deck[:3]
    del deck[:3]

turn = 0
while len(players[0].opened) < 4 and len(players[1].opened) < 4:
    clearConsole()
    print_Players(Vplayers)
    print()
    print_Deck(players[0].hands)
    print("1번 플레이어 님의 오픈된 카드입니다 : ")
    print_Deck(players[0].opened)

    if is_trade == False:
        copen = input("\n플레이어 "+ str(turn + 1) + "님 카드를 어떤 카드를 오픈하시겠습니까? (n번째 카드를 열고 싶다 -> n 입력) : ")
        players[0].opened.append(players[0].hands[int(copen) - 1])
        del players[0].hands[int(copen) + 1]

    print("\n플레이어 2님 카드를 어떤 카드를 오픈하시겠습니까?", end='')

    print("1번 플레이어 님의 오픈된 카드입니다 : ")
    print_Deck(players[0].opened)

    print("-- 플레이어 "+ str(turn + 1) + "턴 입니다 --")
    ctrade = input("플레이어 "+ str(turn + 1) + "님 카드 교환하시겠습니까? (예, Y, Yes면 진행, 이외는 진행 X) : ")
    if ctrade == 'Y' or ctrade == 'y' or ctrade == 'Yes' or ctrade == 'yes' or ctrade == '예':
        is_trade = True
    
    