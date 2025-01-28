from config import *
from var import *

# from Cross import Cross
# from Circle import Circle
from SquarePos import SquarePos

from colorama import Fore

import pygame

if (DEV):
    print(f"{Fore.LIGHTCYAN_EX}[ * ] Initalized as DEV mode{Fore.RESET}")

pygame.init()

window = pygame.display.set_mode((X, Y), flags=pygame.RESIZABLE)

sqpos1: SquarePos = SquarePos(window, "sq1", 1,
                            20, True, 5, Colors.JETBLACK)

sqpos2: SquarePos = SquarePos(window, "sq2", 2,
                            20, True, 5, Colors.JETBLACK)

def mainUpdate():
    global X, Y

    X, Y = window.get_size()

    window.fill(Colors.GREY)

def main():
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
            sys.exit(0)

    mainUpdate()

    # MAIN GAME
    sqpos1.render(10, 10, 100, 100)
    sqpos2.render(10 + 150, 10, 100, 100)

    pygame.display.update()

if (__name__ == "__main__"):
    while 1:
        main()

