from typing import Final as Const

from Shapes import Shapes
from Players import Players

import var

import pygame

class SquarePos:
    def __init__(self, window: pygame.Surface, id: str, pos: int, br: int = 10, fill: bool = False, borderThickness: int = 5,
                 color: tuple = (0, 0, 0)) -> None:
        self.window = window

        self.id: Const = id
        self.pos: Const = pos

        self.borderRad: int = br
        self.borderThickness: int =  borderThickness

        self.fill: bool = fill
        self.clicked: bool = False

        self.color: tuple = color

        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0

        self.shape: Shapes = Shapes(self.window, "getClick-shape")

        var.sysDebug.debug(f"Init `SquarePos` with ID: {id}", "info")

    def setColor(self, color: tuple) -> None: self.color = color
    def setThickness(self, thickness: int) -> None: self.borderThickness = thickness
    def setFill(self, fill: bool) -> None: self.fill = fill

    def render(self, x: int, y: int, w: int, h: int,
               player: Players) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        pygame.draw.rect(self.window, self.color, (self.x, self.y,
                                                   self.w, self.h), self.borderThickness, border_radius=self.borderRad)

        if (self.clicked):
            self.shape.set(player.playerShape)
            self.shape.render(self)

    def getClick(self) -> bool:
        global mouse

        mouse = pygame.mouse.get_pressed()

        if (mouse[0]): # Left click (0), Right click (1)
            mx: int = pygame.mouse.get_pos()[0]
            my: int = pygame.mouse.get_pos()[1]
            
            if (mx >= self.x and mx <= self.x + self.w and
                my >= self.y and my <= self.y + self.h):

                self.clicked = True

                return True

        return False

