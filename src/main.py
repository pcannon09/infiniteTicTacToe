from config import *

from Players import Players
from SquarePos import SquarePos
from Shapes import Shapes

import var

from colorama import Fore

import pygame
import sys
import math

if (var.DEV):
    var.sysDebug.debug(f"{Fore.LIGHTCYAN_EX}[ * ] Initalized as DEV mode{Fore.RESET}", "info")

pygame.init()

window = pygame.display.set_mode((var.X, var.Y), flags=pygame.RESIZABLE)

players: Players = Players("main-players", 1, True)

cross: Shapes = Shapes(window, "main-shapes", "cross")

squarePositions: list[SquarePos] = []

for i in range(0,
        var.squareDimentions[0] * var.squareDimentions[1]):
    squarePositions.append(SquarePos(window, f"sq-{i}", i, 20, False, 5, (0, 0, 0)))

def mainUpdate():
    global X, Y

    X, Y = window.get_size()

    window.fill(var.Colors.GREY)

def main():
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
            sys.exit(0)

    mainUpdate()

    # MAIN GAME

    for i in range(0, var.squareDimentions[0]):
        for j in range(0, var.squareDimentions[1]):
            squarePositions[i].render(10 + var.squareSpacing * i, 10 + var.squareSpacing * j, var.squareSize, var.squareSize)

    pygame.display.update()

if (__name__ == "__main__"):
    var.sysDebug.debug("", "info")

    while 1:
        main()

