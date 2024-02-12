class Settings:
    def __init__(self):
        # Screen settings
        self.bg_color = '#5bb6d5'
        self.screen_height = 800
        self.screen_width = 1200

        # Ship settings
        self.ship_limit = 3
        self.ships_left = self.ship_limit

        # Bullet settings
        self.bullet_color = (60, 60, 60)
        self.bullet_height = 15
        self.bullet_width = 5
        self.max_bullets = 5

        # Alien settings
        self.fleet_drop_speed = 15

        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 2.5
        self.bullet_speed = self.ship_speed + 4.0
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
