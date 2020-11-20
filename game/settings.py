# Each time we introduce new functionality into the game its typical to create some new settings as well.
class Settings:
    """a class to store all settings for the game."""
    def __init__(self):
        """default settings."""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        
        #ship settings
        self.ship_speed = 1.5

        #bullet settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3