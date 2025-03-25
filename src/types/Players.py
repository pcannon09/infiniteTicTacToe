from typing import Final as Const

from var import sysDebug
from Shapes import Shapes

class Players:
    def __init__(self, id: str, playerShapes: list, startPlayer: int = 1):
        self.id: str = id

        if startPlayer > len(playerShapes):
            startPlayer = len(playerShapes)

        self.playerShapes: list[Shapes] = playerShapes
        self.currentPlayer: int = startPlayer
        self.playerShape: Shapes | None = self.playerShapes[self.currentPlayer - 1]

        sysDebug.debug(f"Init `Players` with ID: {id}")

    def switch(self) -> int:
        self.currentPlayer = 2 if self.currentPlayer == 1 else 1
        
        self.playerShape = self.playerShapes[self.currentPlayer - 1]

        sysDebug.debug(f"Player switched to `{self.currentPlayer}` - ID: {self.id}")

        return self.currentPlayer

    def render(self):
        sysDebug.debug(self.playerShape.image, "debug")

        self.playerShape.render(self.playerShape.image)


