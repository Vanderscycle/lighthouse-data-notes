# Each time we introduce new functionality into the game its typical to create some new settings as well.
class Settings:
    """a class to store all settings for the game."""
    def __init__(self):
        """default settings."""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        