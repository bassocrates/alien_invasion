#!/usr/bin/python3
# alien_invasion.py - pygame implementation of classic space invaders game

# TODO:
#   - Add ability to play by hitting 'p' key (add start game function)
#   - Add difficulty buttons
#   - Add text that shows 'reloading' when bullet limit hit
#   - Add quit button (file menu?)
#   - Add game modifiers:
#       - Tokens that appear randomly, when shot give power ups
#           - Faster bullets, more bullets, faster ship, laser bullet
#           - Randomly kill alien(s)
#   - Off set fleet rows?
#   - Display lives in upper corner
#   - Display text when events happen (level up, lost life, etc.)

# Imports
import sys
import pygame
import random
from time import sleep

from settings import Settings
from background import Star
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    """ Main class to manage game assets and behavior """

    def __init__(self):
        """ Initialize game, create resources """

        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.clock = pygame.time.Clock()

        pygame.display.set_caption('Alien Invasion')

        # Create game stats and scoreboard to display stats
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.stars = pygame.sprite.Group()

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Start game in active state
        self.game_active = False

        # Generate play button
        self.play_button = Button(self, "Play")

    def run_game(self):
        """ Start the main loop for the game """

        # First make the random star background, which will be static
        self._make_background()

        while True:
            # Watch for keyboard and mouse events.
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)

    def _make_background(self):
        """ Create the sprite group of star rects, randomly placed on the screen """

        for x in range(1, self.settings.star_density):
            new_star = Star(self)
            new_star.rect.x = random.randint(0, 1200)
            new_star.rect.y = random.randint(0, 800)
            self.stars.add(new_star)

    def _check_events(self):
        """ Respond to key presses and events """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Move ship left or right when arrow keys pressed
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """ Start game when play button is clicked """

        button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        if button_clicked and not self.game_active:
            self._start_game()

    def _check_keydown_events(self, event):
        """ Respond to keys being pressed """

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self._start_game()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """ Respond to keys being pressed """

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _start_game(self):
        """ Start the game when play button or 'p' is pressed """

        self.settings.init_dynamic_settings()
        self.stats.reset_stats()
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_lives()
        self.game_active = True

        # Hide the mouse
        pygame.mouse.set_visible(False)

        # Clear out previous game from screen
        self.bullets.empty()
        self.aliens.empty()

        # Create new game
        self._create_fleet()
        self.ship.center_ship()

    def _fire_bullet(self):
        """ Create bullet and add to bullets group """

        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """ Update position of bullets, delete old ones """

        self.bullets.update()  # update bullet positions

        # Delete bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """ Check and respond to bullet-alien collisions """

        # Check for bullets that hit aliens
        # If so, get rid of bullet and alien
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, False, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()

    def _update_aliens(self):
        """ Update positions of all aliens in fleet """

        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting bottom of the screen
        self._check_aliens_bottom()

    def _create_fleet(self):
        """ Create the fleet of aliens """

        # Create an alien and continue creating until no room left in row
        # Spacing between aliens = size of one alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Finished a row, reset x value, increment y value
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """ Create an alien and place it in current row """

        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """ Respond if an alien hits an edge """

        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """ Drop fleet and change direction """

        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed

        self.settings.fleet_direction *= -1

    def _check_aliens_bottom(self):
        """ Check if an aliens made it to the bottom of the screen """

        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()    # same behavior as if ship is hit by alien
                break

    def _ship_hit(self):
        """ Respond to ship being hit ny an alien """

        if self.stats.lives_left > 0:
            # Lose a life
            self.stats.lives_left -= 1
            self.sb.prep_lives()

            # Clear any aliens and bullets from the screen
            self.aliens.empty()
            self.bullets.empty()

            # Create new fleet, re-center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Pause so the player can mentally re-group
            sleep(2)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        """ Update images on screen, flip to new screen """
        self.screen.fill(self.settings.bg_color)

        for star in self.stars.sprites():
            star.draw_star()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme()
        self.aliens.draw(self.screen)
        # print(len(self.aliens))

        # Draw score info
        self.sb.show_score()

        if not self.game_active:
            self.play_button.draw_button()

        # Make most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    game = AlienInvasion()
    game.run_game()
