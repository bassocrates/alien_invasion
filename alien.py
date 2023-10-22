import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """ A class to represent an alien in a fleet """

    def __init__(self, game):
        """ Initialize alien, set starting position """

        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Load alien image, set its rect attribute
        self.image = pygame.image.load('img/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each alien near top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """ Return True if alien is at edge of screen """

        screen_rect = self.screen.get_rect()

        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """ Move the alien to the right or left """

        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
