#aliens descend from the top of the screen, if the rect of an alien and the rect
#rect of a bullet overlap anywhere, the alien is removed from the screen.

import pygame
import random
from pygame.sprite import Sprite

class Alien(Sprite):
    """manages alien resources and movements"""

    def __init__(self, ai_game):
        """initialises alien attributes"""
        super().__init__()

        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('game_resources/alien.bmp')
        self.rect = self.image.get_rect()

        #places the alien at a random horizontal position at the top of the screen
        self.rect.top = 0 
        self.rect.left = random.randint(0, int(self.screen_rect.right - self.rect.width))

        self.y = float(self.rect.y)


    def blitme(self):
        """draws the alien onto the screen"""

        self.screen.blit(self.image, self.rect)

    def update_pos(self):
        """re-positions the alien"""

        self.y += self.settings.alien_speed

        self.rect.y = self.y




    

