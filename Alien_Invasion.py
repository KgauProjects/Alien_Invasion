import pygame
import sys
from ship import Ship
from settings import Settings
from bullet import Bullet

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

        #create a group of shot bullets
        self.bullets = pygame.sprite.Group()

        self.bullets_used = 0

    def run_game(self):
        """executes the game"""

        #while the game runs, the screen is refreshed at every iteration   
        while True:
            #updates the position of all screen elements
            self._update_screen()

            self._update_bullets()

            #listens for and responds to keyboard events
            self._check_events()

    def _update_screen(self):
        """refreshes the display"""

        #redraws the screen at each iteration
        self.screen.fill(self.settings.screen_color)

        #draws the ship onto the screen
        self.ship.blitme()

        #re-positions the ship (moves the ship)
        self.ship.update_pos()

        #draw all the bullets in the group onto the screen
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
    
        pygame.display.flip()

    def _check_events(self):
        """listens for keyboard events"""

        #listen for and respond to keyboard events 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._handle_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._handle_keyup_events(event)

            elif event.type == pygame.QUIT:
                sys.exit()

    def _fire_bullets(self):
        """if the up arrow is pressed, a bullet is created and added to the group of
        bullets"""

        if self.bullets_used < self.settings.bullets_allowed:     #limits the number of bullets in the screen
            new_bullet = Bullet(self)
            new_bullet.add(self.bullets)
            self.bullets_used += 1

    def _handle_keydown_events(self, event):
        """responds to keypresses"""

        #if 'q' is pressed, quit the game
        if event.key == pygame.K_q:
            sys.exit()

        #ensures continuous motion of the ship in a certain direction whilst a key is pressed 
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

        if event.key == pygame.K_UP:
            self._fire_bullets()
            
    def _handle_keyup_events(self, event):
        """responds to key releases"""

        #stops the motion of the ship when a key is released 
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False 

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

    def _update_bullets(self):
        """manages the bullets in the group of bullets"""

        #if a bullet leaves the screen remove it from the group
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                bullet.remove(self.bullets)
                self.bullets_used -= 1

        #updates the positions of the bullets in the ship
        for bullet in self.bullets.sprites():
            bullet.update_pos()

if __name__ == '__main__':
    #create an instance of Alien Invasion
    ai_game = Alien_Invasion()
    ai_game.run_game()
