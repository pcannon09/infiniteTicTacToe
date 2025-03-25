from config import *

from Players import Players
from SquarePos import SquarePos
from Shapes import Shapes

import var

from colorama import Fore

import pygame
import sys

if (var.DEV):
    var.sysDebug.debug(f"{Fore.LIGHTCYAN_EX}[ * ] Initalized as DEV mode{Fore.RESET}", "info")

pygame.init()


window = pygame.display.set_mode((var.X, var.Y), flags=pygame.RESIZABLE)

currentShape: str = "cross"

cross: Shapes = Shapes(window, "main-cross-shape", "cross")
circle: Shapes = Shapes(window, "main-circle-shape", "circle")

players: Players = Players("main-players", [cross, circle], 1)

squarePositions = [[SquarePos(window, "squarePos", (i, j), br=20, color=(10, 10, 10))
    for j in range(var.squareDimentions[1])]
    for i in range(var.squareDimentions[0])]

for i in range(0,
        var.squareDimentions[0] * var.squareDimentions[1]):
    squarePositions.append(SquarePos(window, f"sq-{i}", i, 20, False, 5, (0, 0, 0)))

def mainUpdate():
    global X, Y

    X, Y = window.get_size()

    window.fill(var.Colors.GREY)

def end(exitCode: int) -> None:
    var.sysDebug.debug("[ * ] End", "warn")

    pygame.quit()
    sys.exit(exitCode)

def main():
    global currentShape

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            end(0)

    mainUpdate()

    # MAIN GAME

    for i in range(0, var.squareDimentions[0]): # Pos X
        for j in range(0, var.squareDimentions[1]): # Pos Y
            squarePositions[i][j].render(10 + var.squareSpacing * i, 10 + var.squareSpacing * j, var.squareSize, var.squareSize, players)
            
            if (squarePositions[i][j].getClick()):
                currentShape = "cross" if players.switch() == 1 else "circle"

                print(currentShape)

                print(players.currentPlayer)

            players.render()

    pygame.display.update()

if (__name__ == "__main__"):
    var.sysDebug.debug("[ * ] Starting...", "info")

    try:
        while 1:
            main()

    except KeyboardInterrupt:
       end(0)

