import pygame
# pygame treat all entities as rectangles. So the ship is a rectangle
# when working with game elements work with center,centerx,centery attributes of the rect
# when working with at an edge of the screen, work with top, bottom, left, right attributes
# Pygame has (0,0) as the top-left corner and (1200,800) for the bottom right corner (or whatever res has been selected for the game window)
class Ship:
    """ A class to manage the ship"""

    def __init__(self, ai_game):
        """init the ship layout and starting position."""
        self.screen = ai_game.screen # assign the screen to an attribute ship
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #load the ship image and get its rect. image set for 50x50px
        self.image = pygame.image.load('/home/henri/Documents/Lighthouse-lab/lighthouse-data-notes/game/images/player.bmp') # we use bmp because pygame handles them better
        self.rect = self.image.get_rect() # rectangular objects x/y coord

        #start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom # other attributes are midtop,midleft,midright

        # store a decimal value tfor the ship positon. (the ship only uses one dimension)
        self.x = float(self.rect.x)

        #movement flag for continiuous movement(while the key is pressed down)
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """update the ship's position based on the flag movement"""
        if self.moving_right and self.rect.right < self.screen_rect.right: # done so that the spaceshop doesn't go past the edge of the game screen
            # udate the ship's x value and not the rect
            self.x += self.settings.ship_speed
            #self.rect.x += 1
        if self.moving_left and self.rect.left >0: # 0 because of the cordinate system where x= 0 is at the left of the screen
            self.x -= self.settings.ship_speed
            #self.rect.x -= 1
        self.rect.x = self.x
    def blitme(self):
        """draw the ship at its current location (defined in self"""
        self.screen.blit(self.image,self.rect)
        