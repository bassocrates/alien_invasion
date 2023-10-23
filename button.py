import pygame.font


class Button:
    """ Aclass to build buttons for a game """

    def __init__(self, game, msg):
        """ Initialize button attributes """

        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # Set size and properties of button
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 42)

        # Create rect and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.y -= 55
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """ Turn msg into a rendered image and center text on button """

        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """ Draw blank button, add message """

        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

