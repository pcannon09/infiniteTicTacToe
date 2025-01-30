from config import *

from Players import Players
from SquarePos import SquarePos
from Shapes import Shapes

import var

from colorama import Fore

import pygame

if (var.DEV):
    var.sysDebug.debug(f"{Fore.LIGHTCYAN_EX}[ * ] Initalized as DEV mode{Fore.RESET}", "info")

pygame.init()

window = pygame.display.set_mode((var.X, var.Y), flags=pygame.RESIZABLE)

players: Players = Players("main-players", 1, True)

sqpos1: SquarePos = SquarePos(window, "sq1", 1,
                            20, True, 5, var.Colors.JETBLACK)

sqpos2: SquarePos = SquarePos(window, "sq2", 2,
                            20, True, 5, var.Colors.JETBLACK)

sqpos3: SquarePos = SquarePos(window, "sq3", 3,
                            20, True, 5, var.Colors.JETBLACK)

cross: Shapes = Shapes(window, "main-shapes", "cross")

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
    sqpos1.render(10, 10,                         var.squareSize, var.squareSize)
    sqpos2.render(10 + var.squareSpacing, 10,     var.squareSize, var.squareSize)
    sqpos3.render(10 + var.squareSpacing * 2, 10, var.squareSize, var.squareSize)

    cross.render(sqpos1)

    pygame.display.update()

if (__name__ == "__main__"):
    var.sysDebug.debug("", "info")

    while 1:
        main()

