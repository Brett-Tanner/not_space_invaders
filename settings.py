class Settings:
    def __init__(self):
        # Screen settings
        self.bg_color = '#5bb6d5'
        self.screen_height = 800
        self.screen_width = 1200

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_color = (60, 60, 60)
        self.bullet_height = 15
        self.bullet_speed = self.ship_speed + 1.0
        self.bullet_width = 3
        self.max_bullets = 5
