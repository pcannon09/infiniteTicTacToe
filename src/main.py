from config import *

# from types.Cross import Cross
# from types.Circle import Circle
# from types.SquarePos import SquarePos

from colorama import Fore

import pygame

from var import *

if (DEV):
    print(f"{Fore.LIGHTCYAN_EX}[ * ] Initalized as DEV mode{Fore.RESET}")

pygame.init()

window = pygame.display.set_mode((X, Y))

def main():
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
            sys.exit(0);

if (__name__ == "__main__"):
    while 1:
        main()

