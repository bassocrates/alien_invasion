import pygame.font


class Button:
    """ Aclass to build buttons for a game """

    def __init__(self, game, msg, width, height, button_color, text_color, pos=None):
        """ Initialize button attributes """

        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()

        # Set size and properties of button
        self.width, self.height = width, height
        self.button_color = button_color
        self.text_color = text_color
        self.font = pygame.font.SysFont(self.settings.font, 42)

        # Create rect and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        if pos:
            self.rect.centerx = pos[0]
            self.rect.centery = pos[1]
        else:
            self.rect.center = self.screen_rect.center
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """ Turn msg into a rendered image and center text on button """

        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = (self.rect.centerx, self.rect.centery)

    def draw_button(self):
        """ Draw blank button, add message """

        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

