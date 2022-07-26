from QuatroCard import Card
from QuatroUser import User
from QuatroPlayer import QuatroPlayer
from QuatroNPC import QuatroNPC


class QuatroSimul:
    def __init__(self):
        self.__winner = 0
        self.__turn = 0
        self.__deck = []

    def proceed(self):
        players = [QuatroPlayer(), QuatroPlayer()]
        vPlayers = [QuatroNPC(), QuatroNPC(), QuatroNPC(),
                    QuatroNPC(), QuatroNPC(), QuatroNPC()]

    @property
    def winner(self):
        return self.__winner

    @property
    def turn(self):
        return self.__turn

    @property
    def deck(self):
        return self.__deck

    @winner.setter
    def winner(self, winner: int):
        self.__winner = winner

    @turn.setter
    def turn(self, turn: int):
        self.__turn = turn

    @deck.setter
    def deck(self, index: int, values):
        self.__deck[index] = values
