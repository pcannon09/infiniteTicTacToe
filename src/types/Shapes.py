from typing import Final as Const
import var
import pygame
import os


class ErrorUnknownShape(Exception):
    pass


class Shapes:
    def __init__(self, window: pygame.Surface, id: str, shapeID: int | None = None, shape: str | None = None):
        self.id: Const = id

        self.validShapes: list = [
            "circle", "cross", "square", "triangle", None]
        self.window: pygame.Surface = window
        self.shape: str | None = shape
        self.shapeID: int | None = shapeID
        self.shapePositionSpacing: int = 10

        # Custom colors for different shapes
        self.shape_colors = {
            "cross": (220, 50, 50),    # Red for cross
            "circle": (50, 50, 220),   # Blue for circle
            "square": (50, 220, 50),   # Green for square
            "triangle": (220, 220, 50)  # Yellow for triangle
        }

        # Glow effect parameters
        self.glow_effect = True
        self.glow_intensity = 15  # Smaller glow radius for better fit

        var.sysDebug.debug(f"Loading image for Shapes with ID: {
                           id} and shape named {self.shape}", "info")
        if (self.shape not in self.validShapes):
            raise ErrorUnknownShape(
                f"{self.shape} is not a valid shape, make sure you have a valid one")
        if (self.shapeID is not None):
            self.shapeID = shapeID
        self.image: pygame.Surface | None = self.set(self.shape)
        var.sysDebug.debug(f"LOADED image for Shapes with ID: {id}", "info")
        var.sysDebug.debug(f"Init Shapes with ID: {id}", "info")

    def set(self, shape: str | None) -> pygame.Surface | None:
        self.shape = shape
        image: pygame.Surface | None = None
        if (self.shape is not None):
            # Fallback to creating shapes if image doesn't exist
            img_path = f"rsrc/imgs/players/{self.shape}.png"
            if os.path.exists(img_path):
                image = pygame.image.load(img_path)
                # Scale the loaded image to fit properly
                image = pygame.transform.smoothscale(image,
                                                     (int(var.squareSize * 0.75),
                                                      int(var.squareSize * 0.75)))
            else:
                # Create a properly sized surface for the shape
                base_size = int(var.squareSize * 0.75)

                # Create a surface with room for glow
                if self.glow_effect:
                    total_size = base_size + self.glow_intensity*2
                    image = pygame.Surface(
                        (total_size, total_size), pygame.SRCALPHA)

                    # Center position for drawing
                    center_x = total_size // 2
                    center_y = total_size // 2

                    # Get shape color
                    shape_color = self.shape_colors.get(
                        self.shape, (255, 255, 255))

                    if self.shape == "cross":
                        # Adjust dimensions to fit the square
                        shape_size = base_size * 0.8  # Slightly smaller to fit nicely

                        # Draw glow effect
                        for offset in range(5, 0, -1):
                            thickness = 7 - offset  # Thinner lines for smaller shapes
                            alpha = 10 + offset*6
                            glow_color = (*shape_color[:3], alpha)

                            pygame.draw.line(image, glow_color,
                                             (center_x - shape_size//2 + offset,
                                              center_y - shape_size//2 + offset),
                                             (center_x + shape_size//2 - offset,
                                              center_y + shape_size//2 - offset),
                                             thickness)
                            pygame.draw.line(image, glow_color,
                                             (center_x - shape_size//2 + offset,
                                              center_y + shape_size//2 - offset),
                                             (center_x + shape_size//2 - offset,
                                              center_y - shape_size//2 + offset),
                                             thickness)

                        # Draw main cross with proper thickness
                        pygame.draw.line(image, shape_color,
                                         (center_x - shape_size//2,
                                          center_y - shape_size//2),
                                         (center_x + shape_size//2,
                                          center_y + shape_size//2),
                                         4)  # Proper line thickness
                        pygame.draw.line(image, shape_color,
                                         (center_x - shape_size//2,
                                          center_y + shape_size//2),
                                         (center_x + shape_size//2,
                                          center_y - shape_size//2),
                                         4)  # Proper line thickness

                    elif self.shape == "circle":
                        # Adjust radius to fit properly in the square
                        radius = base_size * 0.4  # Circle takes up 80% of the shape area

                        # Draw glow effect
                        for offset in range(5, 0, -1):
                            thickness = 6 - offset  # Thinner ring for smaller circles
                            alpha = 10 + offset*6
                            glow_color = (*shape_color[:3], alpha)
                            pygame.draw.circle(image, glow_color, (center_x, center_y),
                                               radius + offset, thickness)

                        # Draw main circle with proper thickness
                        pygame.draw.circle(
                            image, shape_color, (center_x, center_y), radius, 3)
                else:
                    # Basic shapes without glow
                    image = pygame.Surface(
                        (base_size, base_size), pygame.SRCALPHA)
                    shape_color = self.shape_colors.get(
                        self.shape, (255, 255, 255))

                    if self.shape == "cross":
                        shape_size = base_size * 0.8
                        pygame.draw.line(image, shape_color,
                                         (base_size//2 - shape_size//2,
                                          base_size//2 - shape_size//2),
                                         (base_size//2 + shape_size//2, base_size//2 + shape_size//2), 4)
                        pygame.draw.line(image, shape_color,
                                         (base_size//2 - shape_size//2,
                                          base_size//2 + shape_size//2),
                                         (base_size//2 + shape_size//2, base_size//2 - shape_size//2), 4)
                    elif self.shape == "circle":
                        pygame.draw.circle(image, shape_color,
                                           (base_size//2, base_size//2),
                                           base_size * 0.4, 3)

            self.image = image
            return image
        return None

    def render(self, bind: pygame.Surface | None):
        """
        Render
        * Render the shape centered in the SquarePos
        """

        if (self.image is not None and bind is not None):
            # Calculate center position of the square
            square_center_x = bind.get_rect()[0] + bind.get_rect()[2] // 2
            square_center_y = bind.get_rect()[1] + bind.get_rect()[3] // 2

            # Calculate shape position (centered)
            shape_width = self.image.get_width()
            shape_height = self.image.get_height()
            pos_x = square_center_x - shape_width // 2
            pos_y = square_center_y - shape_height // 2

            # Draw the shape
            self.window.blit(self.image, (pos_x, pos_y))
