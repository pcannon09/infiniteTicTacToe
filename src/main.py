from config import *

# from types.Cross import Cross
# from types.Circle import Circle
# from types.SquarePos import SquarePos

from utils import Debug

from colorama import Fore

import pygame

import var

if (var.DEV):
    print(f"{Fore.LIGHTCYAN_EX}[ * ] Initalized as DEV mode")

pygame.init()

debug = Debug("./.private/logs/main-logs.txt")

def main():
    pass

if (__name__ == "__main__"):
    main()

