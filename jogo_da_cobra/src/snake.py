from typing import List

class Snake:
    def __init__(self,  screenSize: List,
                        position = [80, 50],
                        body = [[80, 50], [70, 50], [60, 50]],
                        direction = 'DIREITA'):                        
        self.__screenSize = screenSize
        self.__position = position
        self.body = body
        self.__direction = direction

    def setDirection(self, newDirection: str) -> None:
        if newDirection == 'DIREITA' and not self.__direction == 'ESQUERDA':
            self.__direction = 'DIREITA'
        if newDirection == 'ESQUERDA' and not self.__direction == 'DIREITA':
            self.__direction = 'ESQUERDA'
        if newDirection == 'CIMA' and not self.__direction == 'BAIXO':
            self.__direction = 'CIMA'
        if newDirection == 'BAIXO' and not self.__direction == 'CIMA':
            self.__direction = 'BAIXO'

    def ateFood(self, positionFood: List) -> bool:
        if self.__direction == 'DIREITA':
            self.__position[0] += 10 # x + 10
        if self.__direction == 'ESQUERDA':
            self.__position[0] -= 10 # x - 10
        if self.__direction == 'CIMA':
            self.__position[1] -= 10 # y - 10
        if self.__direction == 'BAIXO':
            self.__position[1] += 10 # y + 10

        self.body.insert(0, list(self.__position))

        if self.__position == positionFood:
            return True

        self.body.pop()

        return False

    def colisor(self) -> bool:
        if self.__position[0] > (self.__screenSize[0] - 10) or self.__position[0] < 0:
            return True

        if self.__position[1] > (self.__screenSize[1] - 10) or self.__position[1] < 0:
            return True

        for parte_corpo in self.body[1:]:
            if self.__position == parte_corpo:
                return True