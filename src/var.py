from typing import Final as Const

from utils import Debug

DEV: Const = True

X = 500
Y = 500

debug: Const = Debug("./.private/logs/main-logs.txt")

class Colors:
    WHITE: Const = (255, 255, 255)
    WHITE2: Const = (245, 245, 245)

    BLACK: Const = (0, 0, 0)
    JETBLACK: Const = (30, 30, 30)

    GREY: Const = (155, 155, 155)

