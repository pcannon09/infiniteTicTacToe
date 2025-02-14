from typing import Final as Const

from var import sysDebug

class Players:
    def __init__(self, id: str, playerShape: str, startPlayer: int = 1):
        self.id: Const = id

        self.playerShape: str = playerShape

        self.currentPlayer: int = startPlayer
        
        sysDebug.debug(f"Init `Players` with ID: {id}")

    def switch(self):
        self.currentPlayer = 2 if self.currentPlayer == 1 else 1
        
        sysDebug.debug(f"Player switched to `{self.currentPlayer}` - ID: {self.id}")

