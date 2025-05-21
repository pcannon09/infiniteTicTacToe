from config import *

from Players import Players
from SquarePos import SquarePos
from Shapes import Shapes

import var

from colorama import Fore

import pygame
import sys

if (var.DEV):
    var.sysDebug.debug(
        f"{Fore.LIGHTCYAN_EX}[ * ] Initalized as DEV mode{Fore.RESET}", "info")

pygame.init()

window = pygame.display.set_mode((var.X, var.Y), flags=pygame.RESIZABLE)
pygame.display.set_caption("TicTacToe")

cross: Shapes = Shapes(window, "main-cross-shape", "cross", shape="cross")
circle: Shapes = Shapes(window, "main-circle-shape", "circle", shape="circle")

players: Players = Players("main-players",
                           [circle, cross],
                           1)

currentShape: str = players.currentShape

squarePositions = [[SquarePos(window, f"squarePos-{i}-{j}", (i, j), br=20, color=(10, 10, 10))
                    for j in range(var.squareDimentions[1])]
                   for i in range(var.squareDimentions[0])]


def mainUpdate():
    global X, Y

    X, Y = window.get_size()

    window.fill(var.Colors.GREY)


def end(exitCode: int) -> None:
    var.sysDebug.debug("[ * ] End", "warn")

    pygame.quit()
    sys.exit(exitCode)


def checkWin(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != None:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != None:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != None:
        return board[0][2]

    return None


def main():
    global currentShape

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            end(0)

    mainUpdate()

    gameBoard = [[None, None, None], [None, None, None], [None, None, None]]
    winner = None

    # MAIN GAME
    for i in range(0, var.squareDimentions[0]):  # Pos X
        for j in range(0, var.squareDimentions[1]):  # Pos Y
            squarePositions[i][j].render(
                10 + var.squareSpacing * i, 10 + var.squareSpacing * j, var.squareSize, var.squareSize, players)

            if squarePositions[i][j].clicked:
                gameBoard[i][j] = squarePositions[i][j].shape.shape

            if (squarePositions[i][j].getClick() and gameBoard[i][j] is None and winner is None):
                currentShape = "cross" if players.currentPlayer == 1 else "circle"
                gameBoard[i][j] = currentShape
                squarePositions[i][j].shape.set(currentShape)
                players.switch()

    winner = checkWin(gameBoard)

    if winner:
        font = pygame.font.SysFont("Arial", 30)
        text = font.render(f"Player {winner} wins!", True, var.Colors.BLACK)
        window.blit(text, (var.X // 2 - 100, var.Y - 50))

    fullBoard = all(gameBoard[i][j] is not None for i in range(3)
                    for j in range(3))
    if fullBoard and not winner:
        font = pygame.font.SysFont("Arial", 30)
        text = font.render("It's a draw!", True, var.Colors.BLACK)
        window.blit(text, (var.X // 2 - 70, var.Y - 50))

    players.render()

    pygame.display.update()


if (__name__ == "__main__"):
    var.sysDebug.debug("[ * ] Starting...", "info")

    try:
        while 1:
            main()

    except KeyboardInterrupt:
        end(0)
