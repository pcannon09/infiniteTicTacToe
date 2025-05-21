from typing import Final as Const

from var import sysDebug
from Shapes import Shapes
import pygame


class Players:
    def __init__(self, id: str, playerShapes: list[Shapes], startPlayer: int = 1):
        self.id: str = id

        if startPlayer > len(playerShapes):
            startPlayer = len(playerShapes)

        self.playerShapes: list = playerShapes
        self.currentPlayer: int = 1  # Player 1
        self.currentShape: str | None = self.playerShapes[self.currentPlayer - 1].shape
        self.playerShape: Shapes | None = self.playerShapes[self.currentPlayer - 1]

        sysDebug.debug(f"Init Players with ID: {id}")

    def switch(self) -> int:
        self.currentPlayer = 2 if self.currentPlayer == 1 else 1

        self.playerShape = self.playerShapes[self.currentPlayer - 1]
        self.currentShape = self.playerShape.shape

        sysDebug.debug(f"Player switched to {
                       self.currentPlayer} - ID: {self.id}")

        return self.currentPlayer

    def render(self):
        font = pygame.font.SysFont("Arial", 24)
        text = font.render(f"Current Player: {
                           self.currentShape}", True, (0, 0, 0))

        self.playerShape.window.blit(text, (10, 480))
