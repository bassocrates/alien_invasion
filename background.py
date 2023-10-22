import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """ Class to draw stars in background of game """

    def __init__(self, game):
        """ Initialize star rect settings """

        super().__init__()
        self.screen = game.screen
        self.color = (255, 255, 255)

        # Create rect 2x2 pixels at (1, 1)
        self.rect = pygame.Rect(1, 1, 2, 2)

    def draw_star(self):
        """ Draw the star to the screen """

        pygame.draw.rect(self.screen, self.color, self.rect)
