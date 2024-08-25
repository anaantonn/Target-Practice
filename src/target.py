import pygame

from pygame.sprite import Sprite
from random import randint

class Target(Sprite):
    """Class to represent the targets."""
    def __init__(self, ai_settings, screen):
        """Initialize target's random positions."""
        super(Target, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.movement_direction = ai_settings.direction
        self.speed = self.ai_settings.target_speed 

        #Load the target image and set its rect attribute.
        self.image = pygame.image.load('images/Target.png')
        self.rect = self.image.get_rect()
        
        #Start a target at a random position on the screen.
        self.rect.x = randint(0, ai_settings.screen_width - self.rect.width)
        self.rect.y = randint(0, ai_settings.screen_height - self.rect.height)
        
        #Store the initial position.
        self.x = float(self.rect.x)
        self.starting_x = self.rect.x

        #Movement range.
        self.right_margin = self.starting_x + 50
        self.left_margin = self.starting_x - 50

    
    def update(self):
        """Move target left and right."""
        screen_rect = self.screen.get_rect()
        self.x += self.speed * self.movement_direction
        if self.rect.x >= self.right_margin or self.rect.x >= screen_rect.right:
            self.movement_direction = -1
        elif self.rect.x <= self.left_margin or self.rect.left <= 0:
            self.movement_direction = 1
        
        #Update the rect position.
        self.rect.x = self.x

    def blitme(self):
        """Draw the target on the screen."""
        self.screen.blit(self.image, self.rect)