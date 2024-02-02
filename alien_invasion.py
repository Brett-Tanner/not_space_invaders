"""Runs the game"""

import sys
import pygame # type: ignore
from settings import Settings

class AlienInvasion:
    """Manages the game loop and resources"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height)
                )
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the gameloop"""
        while True:
            self.screen.fill(self.settings.bg_color)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                pygame.display.flip()
                self.clock.tick(60)

# Only runs if this file is run directly
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
