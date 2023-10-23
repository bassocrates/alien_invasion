import pygame
from pygame.sprite import Sprite
import random


class Modifier(Sprite):
    """ Class to add game modifiers (e.g. double points) """

    def __init__(self, game):
        """ Initialize modifiers """

        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # We will randmoize which modifier appears on screen,
        # this will be the list to choose from
        self.possible_mods = ['img/double_points.bmp', 'img/infinite_ammo.bmp']

        self.mod_choice = random.choice(self.possible_mods)
        self.image = pygame.image.load(self.mod_choice).convert_alpha()
        self.rect = self.image.get_rect()

        # Start modifier at random place vertically
        self.rect.y = random.randint(0, self.settings.screen_height - 50)

    def update(self):
        """ Move modifier across the screen """

        # Will need to change # to a setting amount
        self.rect.x += 2
