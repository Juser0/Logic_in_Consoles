from QuatroUser import User

class QuatroNPC(User):
    __traded_players = [False, False]

    @property
    def traded_players(self):
        return self.__traded_players
    
    @traded_players.setter
    def traded_players(self, index : int, trade : bool):
        self.__traded_players[index] = trade 
