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

# Background image
background = None
if var.USE_BACKGROUND:
    try:
        background = pygame.image.load("rsrc/imgs/background.png")

    except:
        var.sysDebug.debug("[ WARN ] Failed to load background image", "warn")

# Game title and font
title_font = pygame.font.SysFont("Arial", 40, bold=True)
title_text = "TicTacToe"

# Track key state for shortcuts
keys_pressed = {"ctrl": False, "x": False, "s": False, "q": False}

cross: Shapes = Shapes(window, "main-cross-shape", "cross", shape="cross")
circle: Shapes = Shapes(window, "main-circle-shape", "circle", shape="circle")
players: Players = Players("main-players",
                           [circle, cross],
                           1)
currentShape: str = players.currentShape
squarePositions = [[SquarePos(window, f"squarePos-{i}-{j}", (i, j), br=20, color=var.Colors.SQUARE_BORDER)
                    for j in range(var.squareDimentions[1])]
                   for i in range(var.squareDimentions[0])]


def mainUpdate():
    global X, Y
    X, Y = window.get_size()

    # Draw background or fill with gradient
    if background and var.USE_BACKGROUND:
        scaled_bg = pygame.transform.scale(background, (X, Y))
        window.blit(scaled_bg, (0, 0))
    else:
        # Create a gradient background
        for y in range(0, Y, 2):
            color_value = 155 + (y / Y * 40)
            pygame.draw.rect(window, (color_value, color_value, color_value + 20),
                             (0, y, X, 2))

    # Draw title
    title_surface = title_font.render(title_text, True, var.Colors.TITLE)
    window.blit(title_surface, (X // 2 - title_surface.get_width() // 2, 10))


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


def display_game_status(status_text, bg_color, text_color):
    font = pygame.font.SysFont("Arial", 30, bold=True)
    text = font.render(status_text, True, text_color)
    
    # Create a rounded rectangle background
    padding_x, padding_y = 30, 15
    rect_width = text.get_width() + padding_x * 2
    rect_height = text.get_height() + padding_y * 2
    
    # Position in center of screen
    rect_x = var.X // 2 - rect_width // 2
    rect_y = var.Y // 2 - rect_height // 2
    
    # Draw semi-transparent background
    text_bg = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)
    pygame.draw.rect(text_bg, (*bg_color, 230), 
                     (0, 0, rect_width, rect_height), 0, border_radius=15)
    
    # Draw border for better visibility
    border_color = (min(bg_color[0]-30, 255), min(bg_color[1]-30, 255), min(bg_color[2]-30, 255), 255)
    pygame.draw.rect(text_bg, border_color, 
                     (0, 0, rect_width, rect_height), 2, border_radius=15)
    
    window.blit(text_bg, (rect_x, rect_y))
    window.blit(text, (rect_x + padding_x, rect_y + padding_y))


def main():
    global currentShape, title_text, keys_pressed

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            end(0)

        # Key press handling for shortcuts
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                keys_pressed["ctrl"] = True
            elif event.key == pygame.K_x and keys_pressed["ctrl"]:
                keys_pressed["x"] = True
            elif event.key == pygame.K_s and keys_pressed["x"] and keys_pressed["ctrl"]:
                # Activate the title change shortcut
                title_text = "CRUZ EN CUADRADO: La Circumferencia v1.0"
                pygame.display.set_caption(title_text)
                var.sysDebug.debug(
                    f"[ * ] Title changed to {title_text}", "info")
            elif event.key == pygame.K_q and keys_pressed["ctrl"]:
                # Quit shortcut (CTRL+Q)
                var.sysDebug.debug("[ * ] Quit game via CTRL+Q shortcut", "info")
                end(0)

        # Key release handling
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                keys_pressed["ctrl"] = False
            elif event.key == pygame.K_x:
                keys_pressed["x"] = False
            elif event.key == pygame.K_s:
                keys_pressed["s"] = False
            elif event.key == pygame.K_q:
                keys_pressed["q"] = False

    mainUpdate()
    gameBoard = [[None, None, None], [None, None, None], [None, None, None]]
    winner = None

    # MAIN GAME
    for i in range(0, var.squareDimentions[0]):  # Pos X
        for j in range(0, var.squareDimentions[1]):  # Pos Y
            squarePositions[i][j].render(
                var.BOARD_OFFSET_X + var.squareSpacing * i,
                var.BOARD_OFFSET_Y + var.squareSpacing * j,
                var.squareSize, var.squareSize, players)

            if squarePositions[i][j].clicked:
                gameBoard[i][j] = squarePositions[i][j].shape.shape

            if (squarePositions[i][j].getClick() and gameBoard[i][j] is None and winner is None):
                currentShape = "cross" if players.currentPlayer == 1 else "circle"
                gameBoard[i][j] = currentShape
                squarePositions[i][j].shape.set(currentShape)

                players.switch()

    winner = checkWin(gameBoard)

    if winner:
        display_game_status(f"Player {winner} wins!", var.Colors.WIN_BG, var.Colors.WIN_TEXT)

    fullBoard = all(gameBoard[i][j] is not None for i in range(3)
                    for j in range(3))
    if fullBoard and not winner:
        display_game_status("It's a draw!", var.Colors.DRAW_BG, var.Colors.DRAW_TEXT)

    # Draw footer - shortcut info
    footer_font = pygame.font.SysFont("Arial", 12)
    footer_text = footer_font.render(
        "Press CTRL+Q to quit", True, var.Colors.FOOTER)
    window.blit(footer_text, (10, Y - 20))

    players.render()
    pygame.display.update()


if (__name__ == "__main__"):
    var.sysDebug.debug("[ * ] Starting...", "info")
    try:
        while 1:
            main()
    except KeyboardInterrupt:
        end(0)
