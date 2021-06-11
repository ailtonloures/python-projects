import os

from src.players.player import Player
from src.players.player_o import PlayerO
from src.players.player_x import PlayerX
from src.printer import Printer
from src.text_style import TextStyle

class Game:
    def __init__(self):
        self._matrix = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        self._turns = 9
        
        self._playerX = PlayerX()
        self._playerO = PlayerO()
        self._firstPlayer = None
        self._secondPlayer = None

    def start(self) -> None:
        os.system("cls")

        self.configPlayers()
        self.run()

    def configPlayers(self) -> None:
        playerXName = str(input(TextStyle.DEFAULT + "Nome do jogador X (Xis): " + TextStyle.PRIMARY))
        playerOName = str(input(TextStyle.DEFAULT + "Nome do jogador O (Bola): " + TextStyle.PRIMARY))
        firstPlayer = str(input(TextStyle.DEFAULT + "Quem será o primeiro a jogar (X/O)? " + TextStyle.PRIMARY))
        
        self._playerX.name = playerXName
        self._playerO.name = playerOName
        
        if firstPlayer == "X" or firstPlayer == "x":
            self._firstPlayer = self._playerX
            self._secondPlayer = self._playerO
        elif firstPlayer == "O" or firstPlayer == "o":
            self._firstPlayer = self._playerO
            self._secondPlayer = self._playerX
        else:
            self._firstPlayer = self._playerX
            self._secondPlayer = self._playerO

    def run(self) -> None:
        initialTurn = 1
        playerTurn = self._firstPlayer
        playerReturn = self._secondPlayer
        
        while initialTurn <= self._turns:
            print(TextStyle.DEFAULT + "\n    0   1   2")

            index = 0

            for row in self._matrix:
                print(TextStyle.DEFAULT + str(index) + ":  " + row[0] + " | " + row[1] + " | " + row[2])
                print(TextStyle.DEFAULT + "   -----------")

                index += 1

            if initialTurn >= 3:
                if self.verifyResults() == True:
                    Printer.success("Jogo finalizado, o vencedor é " + playerReturn.name + ". Parabéns!")
                    
                    playAgain = str(input(TextStyle.PRIMARY + "Deseja jogar novamente (s/n)? "))

                    if playAgain == "s" or playAgain == "S":
                        Game().start()
                    else:
                        Printer.primary("Encerrando...")
                        exit()

            Printer.primary("Jogada " + str(initialTurn) + ". Rodada do jogador " + playerTurn.name)

            row = int(input(TextStyle.DEFAULT + "Linha: " + TextStyle.PRIMARY))
            column = int(input(TextStyle.DEFAULT + "Coluna: " + TextStyle.PRIMARY))
            
            settedPlayer = self.setPlayerInMatrix(row, column, playerTurn)
            
            if settedPlayer == True:
                if playerTurn.value == "X":
                    playerTurn = self._playerO
                    playerReturn = self._playerX
                elif playerTurn.value == "O":
                    playerTurn = self._playerX
                    playerReturn = self._playerO           
                
                initialTurn += 1
                
                os.system("cls")
        else:
            Printer.primary("Jogo finalizado, sem vencedor... :(")

    def setPlayerInMatrix(self, row: int, column: int, player: Player) -> bool:
        matrix = self._matrix
                
        if row < 0 or row > 2:
            Printer.error("Entrada inválida na 'Linha': " + str(row) + ". Permitido apenas os números 0, 1 e 2")
            return False
        
        if column < 0 or column > 2:
            Printer.error("Entrada inválida na 'Coluna': " + str(column) + ". Permitido apenas os números 0, 1 e 2")
            return False
        
        if matrix[row][column] != " ":
            Printer.error("Este local já foi preenchido, tente outro")
            return False
            
        matrix[row][column] = player.value
        
        return True

    def verifyResults(self) -> bool:
        matrix = self._matrix

        if (matrix[0][0] != " " and matrix[0][0] == matrix[0][1]) and (matrix[0][1] != " " and matrix[0][1] == matrix[0][2]):
            return True

        if (matrix[1][0] != " " and matrix[1][0] == matrix[1][1]) and (matrix[1][1] != " " and matrix[1][1] == matrix[1][2]):
            return True

        if (matrix[2][0] != " " and matrix[2][0] == matrix[2][1]) and (matrix[2][1] != " " and matrix[2][1] == matrix[2][2]):
            return True

        if (matrix[0][0] != " " and matrix[0][0] == matrix[1][0]) and (matrix[1][0] != " " and matrix[1][0] == matrix[2][0]):
            return True

        if (matrix[0][1] != " " and matrix[0][1] == matrix[1][1]) and (matrix[1][1] != " " and matrix[1][1] == matrix[2][1]):
            return True

        if (matrix[0][2] != " " and matrix[0][2] == matrix[1][2]) and (matrix[1][2] != " " and matrix[1][2] == matrix[2][2]):
            return True

        if (matrix[0][0] != " " and matrix[0][0] == matrix[1][1]) and (matrix[1][1] != " " and matrix[1][1] == matrix[2][2]):
            return True

        if (matrix[0][2] != " " and matrix[0][2] == matrix[1][1]) and (matrix[1][1] != " " and matrix[1][1] == matrix[2][0]):
            return True

        return False
