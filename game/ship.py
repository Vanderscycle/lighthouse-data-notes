import pygame
# pygame treat all entities as rectangles. So the ship is a rectangle
class Ship:
    """ A class to manage the ship"""

    def __init(self, ai_game):
        """init the ship layout and starting position."""
        self.screen = ai_game.screen # assign the screen to an attribute ship
        self.screen_rect = ai_game.screen.get_rect()

        #load the ship image and get its rect.
        self.image = pygame.image.load('game/images/player.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        def blitime(self):
            """draw the ship at its current location"""
            self.screen.blit(self.image,self.rect)
        