from typing import Final as Const

from var import sysDebug

class Players:
    def __init__(self, id: str, startPlayer: int = 1, playerIsCircle: bool = False):
        self.id: Const = id

        self.playerIsCircle = playerIsCircle
        self.player = startPlayer
        
        sysDebug.debug(f"Init `Players` with ID: {id}")

    def switch(self):
        self.player = 2 if self.player == 1 else 1
        
        sysDebug.debug(f"Player switched to `{self.player}` - ID: {self.id}")

