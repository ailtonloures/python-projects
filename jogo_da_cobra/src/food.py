import random

from typing import List

class Food:
    def __init__(self, screenSize: List):
        self.__screenSize = screenSize
        self.position = [
            random.randrange(10, self.__screenSize[0], 10),
            random.randrange(10, self.__screenSize[1], 10)
        ]
        self.__devoured = False

    def getPosition(self) -> List:
        if self.__devoured == True:
            self.position = [
                random.randrange(10, self.__screenSize[0], 10),
                random.randrange(10, self.__screenSize[1], 10)
            ]
            self.setDevoured(False)

        return self.position

    def setDevoured(self, devoured: bool) -> None:
        self.__devoured = devoured