from config import *
from typing import Final as Const
from utils import Debug

DEV: Const = True

X = 500
Y = 550

# Game settings
squareDimentions: tuple = (3, 3)
squareSize: int = 100
squareSpacing: int = 130  # Reduced spacing to fit the board better
BOARD_OFFSET_X: int = 55  # Adjusted for new spacing
BOARD_OFFSET_Y: int = 80  # Pushes the board down to make room for the title

# Feature flags
USE_BACKGROUND: Const = True
USE_DECORATION: Const = False  # Disabled decorative corners

# Debug settings
debug: Const = Debug("./.private/logs/main-logs.txt")
sysDebug: Const = Debug(".private/logs/game-sys-logs.txt")


class Colors:
    WHITE: Const = (255, 255, 255)
    WHITE2: Const = (245, 245, 245)
    BLACK: Const = (0, 0, 0)
    JETBLACK: Const = (30, 30, 30)
    GREY: Const = (155, 155, 155)

    # Enhanced color scheme
    TITLE: Const = (50, 50, 120)
    FOOTER: Const = (80, 80, 80)
    SQUARE_BORDER: Const = (40, 40, 40)
    WIN_TEXT: Const = (20, 150, 20)
    WIN_BG: Const = (220, 255, 220)
    DRAW_TEXT: Const = (150, 150, 20)
    DRAW_BG: Const = (255, 255, 220)
    DECORATION: Const = (100, 100, 180)
    PLAYER_TEXT: Const = (10, 10, 80)
    PLAYER_BG: Const = (240, 240, 250)
