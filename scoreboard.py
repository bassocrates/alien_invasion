import pygame.font
from pygame.sprite import Group
from pygame import transform
from ship import Ship

class Scoreboard:
    """ Class to report score info """

    def __init__(self, game):
        """ Initialize score attributes """

        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        # Font settings for display of score info
        self.text_color = (0, 135, 0)
        self.font = pygame.font.SysFont(None, 32)

        # Prepare initial score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_lives()

    def prep_score(self):
        """ Turn score into a rendered image """

        rounded_score = round(self.stats.score, -1)
        score_str = "Score: " + f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display score in top right of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """ Turn high score into rendered image """

        high_score = round(self.stats.high_score, -1)
        high_score_str = "High Score: " + f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """ Turn level into rendered image """

        level_str = "Level: " + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.centerx = (self.high_score_rect.right + self.score_rect.left) / 2
        self.level_rect.top = self.score_rect.top

    def prep_lives(self):
        """ Prepare ships representing lives to be displayed """

        self.lives = Group()
        for life in range(self.stats.lives_left):
            ship = Ship(self.game)
            ship.image = pygame.transform.scale(ship.image, (35, 28))
            ship.rect.x = 10 + life * ship.rect.width
            ship.rect.y = 15
            self.lives.add(ship)


    def show_score(self):
        """ Draw score to the screen """

        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.lives.draw(self.screen)

    def check_high_score(self):
        """ Check for high score """

        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()