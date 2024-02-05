class Settings:
    def __init__(self):
        # Screen settings
        self.bg_color = '#5bb6d5'
        self.screen_height = 800
        self.screen_width = 1200

        # Ship settings
        self.ship_speed = 2.5
        self.ship_limit = 3
        self.ships_left = self.ship_limit

        # Bullet settings
        self.bullet_color = (60, 60, 60)
        self.bullet_height = 15
        self.bullet_speed = self.ship_speed + 4.0
        self.bullet_width = 100
        self.max_bullets = 5

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 150
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
