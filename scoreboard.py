import pygame.font

class Scoreboard:
    """ Class to report score info """

    def __init__(self, game):
        """ Initialize score attributes """

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

    def show_score(self):
        """ Draw score to the screen """

        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def check_high_scre(self):
        """ Check for high score """

        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()