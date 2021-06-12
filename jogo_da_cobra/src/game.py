import pygame
import sys
import time

from typing import List
from src.snake import Snake
from src.food import Food

class Game:
    def __init__(self):
        pygame.init()
        
        pygame.display.set_caption('O Jogo da Cobrinha')
        pygame.font.init()

        self.__screenSize = (400, 400)
        self.__font = pygame.font.SysFont('Comic Sans MS', 20)
        self.__screen = pygame.display.set_mode(self.__screenSize)
        self.__time = pygame.time.Clock()
        self.__snake = Snake(self.__screenSize)
        self.__food = Food(self.__screenSize)

    def start(self) -> None:
        score = 0
        fps = 10

        while True:
            self.__screen.fill((0, 0, 0))
            self.control()

            foodPosition = self.__food.getPosition()
            
            if self.__snake.ateFood(foodPosition) == True:
                self.__food.setDevoured(True)
                score += 1

            if self.__snake.colisor() == True:
                self.__setScore(score)

                textRender = self.__font.render('VOCÊ PERDEU!', True, (255,255,255))
                self.__screen.blit(textRender, (120,180))

                pygame.display.flip()
                time.sleep(3)

                self.quit()
            
            self.__setScore(score)

            fps = self.setLevel(score, fps)

            self.__paint(foodPosition, fps)

    def quit(self) -> None:
        pygame.quit()
        sys.exit()

    def __paint(self, foodPosition: List, fps = 10) -> None:
        for snakeBody in self.__snake.body:            
            pygame.draw.rect(self.__screen, pygame.Color(255, 204, 0), pygame.Rect(snakeBody[0], snakeBody[1], 10, 10))

        pygame.draw.rect(self.__screen, pygame.Color(255, 0, 0), pygame.Rect(foodPosition[0], foodPosition[1], 10, 10))
        pygame.display.update()

        self.__time.tick(fps)

    def __setScore(self, score: int) -> None:
        textRender = self.__font.render('Pontuação: %s ' % score, True, (255, 255, 255))
        self.__screen.blit(textRender, (10, 10))

    def control(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.encerrar()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.__snake.setDirection('DIREITA')

                if event.key == pygame.K_UP:
                    self.__snake.setDirection('CIMA')

                if event.key == pygame.K_DOWN:
                    self.__snake.setDirection('BAIXO')

                if event.key == pygame.K_LEFT:
                    self.__snake.setDirection('ESQUERDA')                

    def setLevel(self, score: int, fps: int) -> int:
        if score == 10:
            fps = 20
        if score == 20:
            fps = 30

        return fps