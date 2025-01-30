from typing import Final as Const

from SquarePos import SquarePos

import var

import pygame

class Shapes:
    def __init__(self, window: pygame.Surface, id: str, shape: str):
        self.id: Const = id
        
        self.window = window
        self.shape = shape

        var.sysDebug.debug(f"Loading image for `Shapes` with ID: {id} and shape named {self.shape}", "info")

        self._image: pygame.Surface = pygame.image.load(f"rsrc/imgs/players/{self.shape}.png")
        self._image = pygame.transform.smoothscale(self._image, (var.squareSize - 20, var.squareSize - 20))

        var.sysDebug.debug(f"LOADED image for `Shapes` with ID: {id}", "info")
        var.sysDebug.debug(f"Init `Shapes` with ID: {id}", "info")

    def render(self, bind: SquarePos):
        """
        Render
        * Render the enemy to the desired ID binded with `SquarePos`
        """
        
        self.window.blit(self._image, (bind.x + 10, bind.y + 10))

