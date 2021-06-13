import pygame

class Settings:
    """manages game element settings"""

    def __init__(self):
        #screen settings
        self.screen_color = (230, 230, 230)

        #ship settings
        self.ship_speed = 1.5

        #bullet settings
        self.bullet_color = (105, 204, 150)
        self.bullet_height = 14
        self.bullet_width = 8
        self.bullet_speed = 1
        self.bullets_allowed = 3
        
        
