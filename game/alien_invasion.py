import sys 
import pygame

# two lines bellow solve an annoying bug with linux regarding sound
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Overall calss to manage game assets and behavior."""

    def __init__(self):
        """Initiliaze the game, and create game ressources."""
        pygame.init()
        self.settings = Settings()

        
        #self.screen is the surface where the game elements will be created
        # windowed screen
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height)) #1200x800px
        
        # fullscreen (windowed is fine)
        # self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien invasions")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group() #grouping all bullets into an instance

        # Set the background color.
        self.bg_color = (230,230,230)

    def run_game(self):
        """Start the main loop of the game."""
        while True:
            self._check_events()
            self.ship.update()
            
            self._update_screen()
            self._update_bullets()
            


    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # KEY DOWN events
            elif event.type == pygame.KEYDOWN: # each keypress is registered to a KEYDOWN event.
                # pygame check if the KEYDOWN event correspond to an input in the program
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            

    def _check_keydown_events(self,event):
        """KEYDOWN event corresponding to key presses"""            
        #move the ship to the right
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

        #move the ship to the LEFT
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pygame.K_q:
                sys.exit()

        elif event.key == pygame.K_SPACE:
                self._fire_bullet()  
            
    def _check_keyup_events(self,event):
        """KEYUP event corresponding to key releases."""            

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        """create a new bullet and then places it in the bullet group"""
        if len(self.bullets) >= self.settings.bullets_allowed:
            pass

        else:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        
        self.bullets.update() #updating all fired bullets into
        # Get rid of bullets pas the game screen (otherwise they are still generated)
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)
        ## print(len(self.bullets))

    def _update_screen(self):
        """update images on the screen, and flip to the new screen"""

        # Redraw the scren during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        #make the most recently drawn screen visible
        #pygame.display.flip()
        pygame.display.update()


# just like flasks
if __name__ == '__main__':
    # Make a game isntance, and run the game.
    ai = AlienInvasion()
    ai.run_game()