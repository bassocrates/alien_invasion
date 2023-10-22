class Settings:
    """ Class to store settings for Alien Invasion game """

    def __init__(self):
        """ Initialize basic game settings """

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Star background settings
        self.star_density = 200

        # Ship settings
        self.ship_speed = 2.0
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 4
        self.bullet_height = 24
        self.bullet_color = (200, 0, 0)
        self.bullets_allowed = 10

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1    # 1 = right, -1 = left
