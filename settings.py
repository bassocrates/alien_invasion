class Settings:
    """ Class to store settings for Alien Invasion game """

    def __init__(self):
        """ Initialize basic game's static settings """

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Star background settings
        self.star_density = 200

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 400
        self.bullet_height = 24
        self.bullet_color = (200, 0, 0)
        self.bullets_allowed = 10

        # Alien settings
        self.fleet_drop_speed = 10

        # Rate of speed change per level
        self.speedup_rate = 1.1

        # Rate of increase for scores per level
        self.score_rate = 1.5

        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        """ Initialize dynamic settings """

        # Ship dynamic settings
        self.ship_speed = 2.0

        # Bullet dynamic settings
        self.bullet_speed = 3.0

        # Alien dynamic settings
        self.alien_speed = 1.0
        self.fleet_direction = 1  # 1 = right, -1 = left
        self.alien_points = 50

    def increase_speed(self):
        """ Increase dynamic settings """

        self.ship_speed *= self.speedup_rate
        self.bullet_speed *= self.speedup_rate
        self.alien_speed *= self.speedup_rate
        self.alien_points = int(self.alien_points * self.score_rate)
