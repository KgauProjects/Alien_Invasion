import pygame
import sys
from ship import Ship
from settings import Settings

class Alien_Invasion:
    """manages game resources and behaviour of game elements"""

    def __init__(self):
        """initialises game attributes"""

        #initialise pygame
        pygame.init()

        #create the screen       
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        
        pygame.display.set_caption('Alien Invasion')

        #create a ship
        self.ship = Ship(self)

    def run_game(self):
        """executes the game"""

        #while the game runs, the screen is refreshed at every iteration   
        while True:
            self._update_screen()

            #listen for and respond to keyboard events 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self._handle_keydown_events(event)

                elif event.type == pygame.KEYUP:
                    self._handle_keyup_events(event)

                elif event.type == pygame.QUIT:
                    sys.exit()

                

    def _update_screen(self):
        """refreshes the display"""

        #redraws the screen at each iteration
        self.screen.fill(self.settings.screen_color)

        #draws the ship onto the screen
        self.ship.blitme()

        #re-positions the ship (moves the ship)
        self.ship.update_pos()

        pygame.display.flip()

    def _handle_keydown_events(self, event):
        """responds to keypresses"""

        #if 'q' is pressed, quit the game
        if event.key == pygame.K_q:
            sys.exit()

        #ensures continuous motion of the ship in a certain direction whilst a key is pressed 
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

    def _handle_keyup_events(self, event):
        """responds to key releases"""

        #stops the motion of the ship when a key is released 
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False 

        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

if __name__ == '__main__':
    #create an instance of Alien Invasion
    ai_game = Alien_Invasion()
    ai_game.run_game()
