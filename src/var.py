from config import *
from typing import Final as Const

from utils import Debug

DEV: Const = True

X = 500
Y = 550

squareDimentions: tuple = (3, 3)

squareSize: int = 100
squareSpacing: int = 150

debug: Const = Debug("./.private/logs/main-logs.txt")
sysDebug: Const = Debug(".private/logs/game-sys-logs.txt")


class Colors:
    WHITE: Const = (255, 255, 255)
    WHITE2: Const = (245, 245, 245)

    BLACK: Const = (0, 0, 0)
    JETBLACK: Const = (30, 30, 30)

    GREY: Const = (155, 155, 155)
