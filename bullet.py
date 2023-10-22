import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ Class to manage the ship's ammo """

    def __init__(self, game):
        """ Create a bullet at the ship's current location """

        super().__init__()
        #super().__init__(*groups)
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0), then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = game.ship.rect.midtop

        # Store location as a float
        self.y = float(self.rect.y)

    def update(self):
        """ Move bullet up the screen """

        # Update the exact position of the bullet
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """ Draw bullet to screen """

        pygame.draw.rect(self.screen, self.color, self.rect)

