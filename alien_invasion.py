"""Runs the game"""

import sys
import pygame # type: ignore
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height)
                )
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update_position()
            self._update_bullets()
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

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        if len(self.bullets) < self.settings.max_bullets:
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        pygame.display.flip()

# Only runs if this file is run directly
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
