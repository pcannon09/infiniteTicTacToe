from typing import Final as Const

import pygame

class SquarePos:
    def __init__(self, window: pygame.Surface, id: str, pos: int, br: int = 10, fill: bool = False, borderThickness: int = 5,
                 color: tuple = (0, 0, 0)):
        self.window = window

        self.id: Const = id
        self.pos: Const = pos

        self.borderRad = br
        self.fill = fill
        self.color = color
        self.borderThickness =  borderThickness

        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0

    def setColor(self, color: tuple): self.color = color
    def setThickness(self, thickness: int): self.borderThickness = thickness
    def setFill(self, fill: bool): self.fill = fill

    def render(self, x: int, y: int, w: int, h: int):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        pygame.draw.rect(self.window, self.color, (self.x, self.y,
                                                   self.w, self.h), self.borderThickness, border_radius=self.borderRad)

