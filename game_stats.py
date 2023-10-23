class GameStats:
    """ Track stats for game """

    def __init__(self, game):
        """ Init statistics """

        self.settings = game.settings
        self.reset_stats()

        self.high_score = 0

    def reset_stats(self):
        """ Init stats that can change during the game """

        self.ships_left = self.settings.ship_limit
        self.score = 0