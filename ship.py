import pygame


class Ship:
    """ Class to manage the ship """

    def __init__(self, game):
        """ Initialize ship, set starting position """

        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        # Load ship image, get its rect
        self.image = pygame.image.load('img/ship.bmp')
        self.rect = self.image.get_rect()

        # Start ship at bottom center of screen
        # Then store a float for it's x (horizontal) position
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        # Movement flag, ship is not moving to start
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Update the ship's position based on the movement flag """

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """ Draw ship at its current location """

        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """ Center ship on screen """

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)