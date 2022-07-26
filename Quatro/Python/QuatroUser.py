class User:
    def __init__(self):
        self.__hands = []
        self.__traded = 0 

    @property
    def hands(self):
        return self.__hands

    @property
    def traded(self):
        return self.__traded

    @hands.setter
    def hands(self, index : int, values):
        self.__hands[index] = values
    
    @traded.setter
    def traded(self, traded : int):
        self.__traded = traded




    


    

