import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        
        # Create an instance of the Settings class
        self.settings = Settings()

        # Set the screen dimensions using values from settings
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for events
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets() 
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
          # Move the ship to the right
          self.ship.moving_right = True
          #move ship to the left
        elif event.key == pygame.K_LEFT:
           self.ship.moving_left = True 
        elif event.key == pygame.K_SPACE:
            self._fire_bullet() 
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False 

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()
            # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    

    def _update_screen(self):
        """updates images on the screen, and flip to the new screen"""
         # Redraw the screen with the background color from settings
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
         # Make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    #make an instance of the game and run it
    ai = AlienInvasion()
    ai.run_game()

