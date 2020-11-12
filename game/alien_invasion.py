import sys 
import pygame
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

from settings import Settings

class AlienInvasion:
    """Overall calss to manage game assets and behavior."""

    def __init__(self):
        """Initiliaze the game, and create game ressources."""
        pygame.init()
        self.settings = Settings()

        
        #self.screen is the surface where the game elements will be created
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height)) #1200x800px


        # Set the background color.
        self.bg_color = (230,230,230)

    def run_game(self):
        """Start the main loop of the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Redraw the scren during each pass through the loop
            self.screen.fill(self.settings.bg_color)

            #make the most recently drawn screen visible
            pygame.display.flip()

# just like flasks
if __name__ == '__main__':
    # Make a game isntance, and run the game.
    ai = AlienInvasion()
    ai.run_game()