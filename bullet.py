import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """manages bullet attributes and behaviour"""

    def __init__(self, ai_game):
        """initialises bullet attributes and constructs a bullet"""
        super().__init__()

        #game resources
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.ship = ai_game.ship

        #creates a bullet Rect at (0,0)
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update_pos(self):
        """updates the position of a bullet"""

        #moves the bullet up the screen
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """draws a bullet onto the screen"""

        #draws a bullet of a specified color onto the screen
        pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)

    



        

