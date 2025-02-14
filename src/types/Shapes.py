from typing import Final as Const

import var

import pygame

class ErrorUnknownShape(Exception):
    pass

class Shapes:
    def __init__(self, window: pygame.Surface, id: str, shape: str | None = None):
        self.id: Const = id
        
        self.validShapes: list = ["circle", "cross", "square", "triangle", None]

        self.window: pygame.Surface = window
        self.shape: str | None = shape

        self.shapePositionSpacing: int = 10

        var.sysDebug.debug(f"Loading image for `Shapes` with ID: {id} and shape named {self.shape}", "info")

        if (self.shape not in self.validShapes):
            raise ErrorUnknownShape(f"{self.shape} is not a valid shape, make sure you have a valid one")

        if (self.shape is not None):
            self._image: pygame.Surface = pygame.image.load(f"rsrc/imgs/players/{self.shape}.png")

            self._image = pygame.transform.smoothscale(self._image,
                                                       ( var.squareSize - ( self.shapePositionSpacing * 2 ), var.squareSize - ( self.shapePositionSpacing * 2 ) ))

        var.sysDebug.debug(f"LOADED image for `Shapes` with ID: {id}", "info")
        var.sysDebug.debug(f"Init `Shapes` with ID: {id}", "info")

    def set(self, shape: str) -> None:
        self.shape = shape

        if (self.shape is not None):
            self._image: pygame.Surface = pygame.image.load(f"rsrc/imgs/players/{self.shape}.png")

            self._image = pygame.transform.smoothscale(self._image,
                                                       ( var.squareSize - ( self.shapePositionSpacing * 2 ), var.squareSize - ( self.shapePositionSpacing * 2 ) ))

    def render(self, bind):
        """
        Render
        * Render the enemy to the desired ID binded with `SquarePos`
        """
        
        self.window.blit(self._image, (bind.x + self.shapePositionSpacing, bind.y + self.shapePositionSpacing))

