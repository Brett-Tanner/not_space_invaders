import pygame # type: ignore

class Ship:
    def __init__(self, game):
        self.image = pygame.image.load('images/ship.bmp')

        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_left = False
        self.moving_right = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update_position(self):
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed