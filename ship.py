import pygame
from settings import Settings

class Ship:
    """manages ship attributes and behaviour"""

    def __init__(self, ai_game):
        """initialises ship attributes"""

        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('game_resources/ship.bmp') #this gives the image as a Surface

        #the rect of the ship gives the position of the ship
        self.rect = self.image.get_rect()

        #places the ship at the bottom of the screen, 
        self.rect.midbottom = self.screen_rect.midbottom

        #gives the ship a float horizontal postion
        self.x = float(self.rect.x)
        #flags showing the ship's state of motion
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """draws the ship onto the screen"""

        #draws the image Surface onto the screen Surface at the position of the rect of the ship 
        self.screen.blit(self.image, self.rect)

    def update_pos(self):
        """updates the position of the ship"""

        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        self.rect.x = self.x

