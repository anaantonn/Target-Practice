import pygame
import math

from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class to manage bullets fired by the player."""
    def __init__(self, ai_settings, screen, player, mouse_x, mouse_y):
        """Create a bullet object at the player's current position."""
        super(Bullet, self).__init__()
        self.screen = screen

        #Create a bullet rect at (0,0) then set the correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = player.rect.centerx
        self.rect.centery = player.rect.centery
        self.rect.top = player.rect.top

        #Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed

        #Move the bullet towards the cursor position.
        self.distance_x, self.distance_y = mouse_x - self.x, mouse_y - self.y
        self.distance = math.hypot(self.distance_x, self.distance_y)

        if self.distance != 0:
            self.distance_x /= self.distance
            self.distance_y /= self.distance

    def update(self):
        """Move the bullet on the screen."""    
        self.x += self.distance_x * self.speed_factor
        self.y += self.distance_y * self.speed_factor

        self.rect.x = self.x
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)