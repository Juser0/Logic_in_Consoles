from QuatroUser import User

class QuatroPlayer(User):
    __mulligan = 2

    @property
    def mulligan(self):
        return self.__mulligan
    
    @mulligan.setter
    def mulligan(self, mulligan : int):
        self.__mulligan = mulligan
