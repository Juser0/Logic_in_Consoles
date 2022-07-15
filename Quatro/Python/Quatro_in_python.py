from QuatroFunc import *

'''
deck = [] # 덱
Vplayers = [] # 가상 플레이어
players = [] # 실제 플레이어
turn = 0 # n번 플레이어의 턴임을 확인시킴
is_trade = False # 교환 여부를 확인시킴
'''

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
        is_mul = input("플레이어 1님, 멀리건 진행하시겠습니까? (예, Y, Yes면 진행, 이외는 진행 X) : ")
        if is_mul == 'Y' or is_mul == 'y' or is_mul == 'Yes' or is_mul == 'yes' or is_mul == '예':
            players[turn].mulligan -= 1
            deck.extend(players[0].hands)
            players[turn].hands = deck[:4]
            del deck[:4]
            print('플레이어 1님, 멀리건을 진행합니다. 남은 멀리건 횟수는 ' + str(players[turn].mulligan) + '회 입니다')
            print_Deck(players[turn].hands)
        else:
            players[turn].mulligan = 0
        turn = 1
    else:
        is_mul = input("플레이어 2님, 멀리건 진행하시겠습니까? (예, Y, Yes면 진행, 이외는 진행 X) : ")
        if is_mul == 'Y' or is_mul == 'y' or is_mul == 'Yes' or is_mul == 'yes' or is_mul == '예':
            players[turn].mulligan -= 1
            deck.extend(players[1].hands)
            players[turn].hands = deck[:4]
            del deck[:4]
            print('플레이어 2님, 멀리건을 진행합니다. 남은 멀리건 횟수는 ' + str(players[turn].mulligan) + '회 입니다')
            print_Deck(players[turn].hands)
        else:
            players[turn].mulligan = 0

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
        del players[0].hands[int(copen) - 1]

    print("\n플레이어 2님 카드를 어떤 카드를 오픈하시겠습니까?", end='')

    print("1번 플레이어 님의 오픈된 카드입니다 : ")
    print_Deck(players[0].opened)

    print("-- 플레이어 "+ str(turn + 1) + "턴 입니다 --")
    ctrade = input("플레이어 "+ str(turn + 1) + "님 카드 교환하시겠습니까? (예, Y, Yes면 진행, 이외는 진행 X) : ")
    if ctrade == 'Y' or ctrade == 'y' or ctrade == 'Yes' or ctrade == 'yes' or ctrade == '예':
        is_trade = True
    
    