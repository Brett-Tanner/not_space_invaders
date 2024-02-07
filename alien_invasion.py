"""Runs the game"""

import sys
from time import sleep
import pygame # type: ignore
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button

class AlienInvasion:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Alien Invasion")
        self.settings = Settings()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height)
                )
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stats = GameStats(self)
        self.game_active = False
        self._create_fleet()
        self.play_button = Button(self, "Play")

    def run_game(self):
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update_position()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for e in pygame.event.get():
            if self._quit_event(e):
                sys.exit()
            elif e.type == pygame.KEYDOWN:
                self._check_keydown(e)
            elif e.type == pygame.KEYUP:
                self._check_keyup(e)
            elif e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _quit_event(self, e):
        return e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_q)

    def _check_keydown(self, e):
        if e.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif e.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif e.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup(self, e):
        if e.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif e.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            current_x = alien_width
            current_y += 2 * alien_height

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.stats.reset_stats()
            self.bullets.empty()
            self.aliens.empty()
            self._create_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)
            self.game_active = True

    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        if len(self.bullets) < self.settings.max_bullets:
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            self._check_bullet_alien_collisions()


    def _check_bullet_alien_collisions(self):
        pygame.sprite.groupcollide(
                self.bullets, self.aliens,
                True, True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def _ship_hit(self):
        if self.settings.ships_left > 0:
            self.settings.ships_left -= 1
        else:
            self.game_active = False

        self.bullets.empty()
        self.aliens.empty()

        self._create_fleet()
        self.ship.center_ship()
        pygame.mouse.set_visible(True)
        sleep(0.5)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.ship.blitme()
        if not self.game_active:
            self.play_button.draw_button()
        pygame.display.flip()

# Only runs if this file is run directly
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
