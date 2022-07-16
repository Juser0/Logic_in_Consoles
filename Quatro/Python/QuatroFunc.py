import random
import os
from QuatroClass import *

deck = [] # 덱
Vplayers = [] # 가상 플레이어
players = [] # 실제 플레이어
turn = 0 # n번 플레이어의 턴임을 확인시킴
is_trade = False # 교환 여부를 확인시킴

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
            elif players[wp].opened.index(Vplayers[to - 1].hands[j].num) == -1 and players[wp].opened.index(Vplayers[to - 1].hands[j].color) == -1:
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

def evalWin():
    is_quatro = []
    for i in range(2):
        if (players[i].opened.color[0] != players[i].opened.color[1] != players[i].opened.color[2] != players[i].opened.color[3]):
            is_quatro[i] = True
        else:
            is_quatro[i] = False
    # 두 플레이어 모두 콰트로를 완성한 경우
    if is_quatro[0] == True and is_quatro[1] == True:
        # 카드의 합이 더 큰 경우를 확인하여 더 큰 쪽이 승자가 된다
        if sum(players[0].opened.num) > sum(players[1].opened.num):
            return 0
        elif sum(players[0].opened.num) < sum(players[1].opened.num):
            return 1
        else:
            max(players[0].opened.num)


clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')