import pygame
import sys
from settings import Settings

class Alien_Invasion:
    """manages game resources and behaviour of game elements"""

    def __init__(self):
        """initialises game attributes"""

        #initialise pygame
        pygame.init()

        #create the screen       
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1200, 800))
        
        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        """executes the game"""

        #while the game runs, the screen is refreshed at every iteration   
        while True:
            self._update_screen()

            #listen for and respond to keyboard events 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
        """refreshes the display"""

        #redraws the screen at each iteration
        self.screen.fill(self.settings.screen_color)

        pygame.display.flip()

if __name__ == '__main__':
    #create an instance of Alien Invasion
    ai_game = Alien_Invasion()
    ai_game.run_game()
