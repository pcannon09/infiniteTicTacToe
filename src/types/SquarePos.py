from typing import Final as Const
from Shapes import Shapes
from Players import Players
import var
import pygame
import random


class SquarePos:
    def __init__(self, window: pygame.Surface, id: str, pos: tuple | int, br: int = 10, fill: bool = False,
                 borderThickness: int = 5, color: tuple = (0, 0, 0)) -> None:
        self.window = window
        self.id: Const = id
        self.pos: Const = pos
        self.players: list = []
        self.playerIndex: int = 0
        self.borderRad: int = br
        self.borderThickness: int = borderThickness
        self.fill: bool = fill
        self.clicked: bool = False
        self.color: tuple = color
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.shape: Shapes = Shapes(self.window, f"squarePos-shape-{id}")

        # Animation properties
        self.hover = False
        self.hover_animation = 0
        self.hover_color = (80, 80, 90)
        self.click_animation = 0

        var.sysDebug.debug(f"Init SquarePos with ID: {id}", "info")

    def setColor(self, color: tuple) -> None: self.color = color

    def setThickness(
        self, thickness: int) -> None: self.borderThickness = thickness

    def setFill(self, fill: bool) -> None: self.fill = fill

    def setPlayers(self, players: list) -> None:
        self.players = players

    def render(self, x: int, y: int, w: int, h: int, player: Players) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        # Check for hover state
        mx, my = pygame.mouse.get_pos()
        hover_now = (mx >= self.x and mx <= self.x + self.w and
                     my >= self.y and my <= self.y + self.h)

        # Update hover animation
        if hover_now and not self.hover:
            self.hover = True
        elif not hover_now and self.hover:
            self.hover = False

        # Calculate hover effect
        if self.hover:
            self.hover_animation = min(1.0, self.hover_animation + 0.1)
        else:
            self.hover_animation = max(0.0, self.hover_animation - 0.1)

        # Calculate click animation
        if self.click_animation > 0:
            self.click_animation = max(0, self.click_animation - 0.05)

        # Create a lighter version of the border color for hover effect
        r, g, b = self.color
        hover_r = min(255, r + int(50 * self.hover_animation))
        hover_g = min(255, g + int(50 * self.hover_animation))
        hover_b = min(255, b + int(50 * self.hover_animation))
        current_color = (hover_r, hover_g, hover_b)

        # Draw background with subtle animation
        if not self.clicked:
            bg_color = (210, 210, 230) if self.hover else (200, 200, 220)
            offset = int(2 * self.hover_animation)
            pygame.draw.rect(self.window, bg_color,
                             (self.x + offset, self.y + offset,
                              self.w - offset*2, self.h - offset*2),
                             0, border_radius=self.borderRad)

        # Draw border with animation effects
        thickness = self.borderThickness
        if self.hover:
            thickness += 1

        # Add click effect ripple
        if self.click_animation > 0:
            ripple_size = int(self.w * self.click_animation * 0.5)
            ripple_alpha = int((1 - self.click_animation) * 100)
            ripple_surface = pygame.Surface(
                (ripple_size*2, ripple_size*2), pygame.SRCALPHA)
            pygame.draw.circle(ripple_surface, (*self.hover_color, ripple_alpha),
                               (ripple_size, ripple_size), ripple_size, 2)
            self.window.blit(ripple_surface,
                             (self.x + self.w//2 - ripple_size,
                              self.y + self.h//2 - ripple_size))

        # Draw main square
        pygame.draw.rect(self.window, current_color,
                         (self.x, self.y, self.w, self.h),
                         thickness, border_radius=self.borderRad)

        self.shape.render(self)

    def get_rect(self):
        return [self.x, self.y, self.w, self.h]

    def getClick(self) -> bool:
        mouse = pygame.mouse.get_pressed()
        if (mouse[0]):  # Left click (0), Right click (1)
            mx: int = pygame.mouse.get_pos()[0]
            my: int = pygame.mouse.get_pos()[1]
            if (mx >= self.x and mx <= self.x + self.w and
                    my >= self.y and my <= self.y + self.h):
                if (not self.clicked):
                    self.clicked = True
                    # Trigger click animation
                    self.click_animation = 1.0
                    return True
        return False
