from typing import Final as Const
from var import sysDebug, Colors
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

        # Player icons for the display
        self.player_icons = {}
        self.load_player_icons()

    def load_player_icons(self):
        """Load player icons for display in the status bar"""
        import os
        for shape in ["cross", "circle"]:
            icon_path = f"rsrc/imgs/players/{shape}_icon.png"
            if os.path.exists(icon_path):
                try:
                    self.player_icons[shape] = pygame.image.load(icon_path)
                    self.player_icons[shape] = pygame.transform.smoothscale(
                        self.player_icons[shape], (24, 24))
                except:
                    # Create a small icon if image can't be loaded
                    self.player_icons[shape] = pygame.Surface(
                        (24, 24), pygame.SRCALPHA)
                    if shape == "cross":
                        pygame.draw.line(
                            self.player_icons[shape], (255, 0, 0), (4, 4), (20, 20), 3)
                        pygame.draw.line(
                            self.player_icons[shape], (255, 0, 0), (20, 4), (4, 20), 3)
                    elif shape == "circle":
                        pygame.draw.circle(
                            self.player_icons[shape], (0, 0, 255), (12, 12), 10, 3)
            else:
                # Create icon if file doesn't exist
                self.player_icons[shape] = pygame.Surface(
                    (24, 24), pygame.SRCALPHA)
                if shape == "cross":
                    pygame.draw.line(
                        self.player_icons[shape], (255, 0, 0), (4, 4), (20, 20), 3)
                    pygame.draw.line(
                        self.player_icons[shape], (255, 0, 0), (20, 4), (4, 20), 3)
                elif shape == "circle":
                    pygame.draw.circle(
                        self.player_icons[shape], (0, 0, 255), (12, 12), 10, 3)

    def switch(self) -> int:
        self.currentPlayer = 2 if self.currentPlayer == 1 else 1
        self.playerShape = self.playerShapes[self.currentPlayer - 1]
        self.currentShape = self.playerShape.shape
        sysDebug.debug(f"Player switched to {
                       self.currentPlayer} - ID: {self.id}")
        return self.currentPlayer

    def render(self):
        # Create a background for the player status that adapts to text width
        font = pygame.font.SysFont("Arial", 24, bold=True)
        text = font.render(f"Current Player: {
                           self.currentShape}", True, Colors.PLAYER_TEXT)

        # Background with adaptive width
        padding = 20
        status_width = text.get_width() + 70  # Added space for icon and padding
        status_height = 40

        status_background = pygame.Surface(
            (status_width, status_height), pygame.SRCALPHA)
        pygame.draw.rect(status_background, (*Colors.PLAYER_BG, 230),
                         (0, 0, status_width, status_height), 0, border_radius=10)

        # Draw a border for better visibility
        pygame.draw.rect(status_background, (*Colors.PLAYER_TEXT, 50),
                         (0, 0, status_width, status_height), 2, border_radius=10)

        self.playerShape.window.blit(status_background, (10, 480))

        # Draw player icon
        if self.currentShape in self.player_icons:
            self.playerShape.window.blit(
                self.player_icons[self.currentShape], (20, 488))

        # Render player text
        self.playerShape.window.blit(text, (50, 488))
