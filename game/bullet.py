import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self,ai_game):
        
        super().__init__() # we call super to inherit the propreties from sprite
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create a bullet rectangle a (0,0) and the ncorrect position
        self.rect = pygame.Rect((0,0), (self.settings.bullet_width,self.settings.bullet_height)) #from to (x,y) coords for rectangle creation
        self.rect.midtop = ai_game.ship.rect.midtop

        # bullet horizontal value
        self.y = float(self.rect.y)

    def update(self):

        # update the decimal position of the bullet
        self.y -= self.settings.bullet_speed
        #update rectangle position
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)