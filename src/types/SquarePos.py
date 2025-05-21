from typing import Final as Const

from Shapes import Shapes
from Players import Players

import var

import pygame


class SquarePos:
    def __init__(self, window: pygame.Surface, id: str, pos: tuple | int, br: int = 10, fill: bool = False,
                 borderThickness: int = 5, color: tuple = (0, 0, 0)) -> None:
        self.window = window

        self.id: Const = id
        self.pos: Const = pos

        self.players: list = []
        self.playerIndex: int = 0

        self.borderRad: int = br
        self.borderThickness: int = borderThickness

        self.fill: bool = fill
        self.clicked: bool = False

        self.color: tuple = color

        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0

        self.shape: Shapes = Shapes(self.window, f"squarePos-shape-{id}")

        var.sysDebug.debug(f"Init SquarePos with ID: {id}", "info")

    def setColor(self, color: tuple) -> None: self.color = color
    def setThickness(
        self, thickness: int) -> None: self.borderThickness = thickness

    def setFill(self, fill: bool) -> None: self.fill = fill

    def setPlayers(self, players: list) -> None:
        self.players = players

    def render(self, x: int, y: int, w: int, h: int,
               player: Players) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        pygame.draw.rect(self.window, self.color, (self.x, self.y,
                                                   self.w, self.h), self.borderThickness, border_radius=self.borderRad)

        self.shape.render(self)

    def get_rect(self):
        return [self.x, self.y, self.w, self.h]

    def getClick(self) -> bool:
        mouse = pygame.mouse.get_pressed()

        if (mouse[0]):  # Left click (0), Right click (1)
            mx: int = pygame.mouse.get_pos()[0]
            my: int = pygame.mouse.get_pos()[1]

            if (mx >= self.x and mx <= self.x + self.w and
                    my >= self.y and my <= self.y + self.h):
                if (not self.clicked):
                    self.clicked = True
                    return True

        return False
