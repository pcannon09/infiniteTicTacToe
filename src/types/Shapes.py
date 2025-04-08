from typing import Final as Const

import var

import pygame

class ErrorUnknownShape(Exception):
    pass

class Shapes:
    def __init__(self, window: pygame.Surface, id: str, shapeID: int | None = None, shape: str | None = None):
        self.id: Const = id
        
        self.validShapes: list = ["circle", "cross", "square", "triangle", None]

        self.window: pygame.Surface = window
        self.shape: str | None = shape
        self.shapeID: int | None = shapeID

        self.shapePositionSpacing: int = 10

        var.sysDebug.debug(f"Loading image for `Shapes` with ID: {id} and shape named {self.shape}", "info")

        if (self.shape not in self.validShapes):
            raise ErrorUnknownShape(f"{self.shape} is not a valid shape, make sure you have a valid one")

        if (self.shapeID is not None):
            self.shapeID = shapeID

        self.image: pygame.Surface | None = self.set(self.shape)

        var.sysDebug.debug(f"LOADED image for `Shapes` with ID: {id}", "info")
        var.sysDebug.debug(f"Init `Shapes` with ID: {id}", "info")

    def set(self, shape: str | None) -> pygame.Surface | None:
        self.shape = shape

        image: pygame.Surface | None = None

        if (self.shape is not None):
            image = pygame.image.load(f"rsrc/imgs/players/{self.shape}.png")
            image = pygame.transform.smoothscale(image,
                                                 ( var.squareSize - ( self.shapePositionSpacing * 2 ), var.squareSize - ( self.shapePositionSpacing * 2 ) ))

            return image

        return None

    def render(self, bind: pygame.Surface | None):
        """
        Render
        * Render the enemy to the desired ID binded with `SquarePos`
        """
        
        if (self.image is not None):
            if (bind is not None):
                self.window.blit(self.image, (bind.get_rect()[0] + self.shapePositionSpacing, bind.get_rect()[1] + self.shapePositionSpacing))

