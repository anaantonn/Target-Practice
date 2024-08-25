import pygame

class Ace():
    def __init__(self, ai_settings, screen):
        """A class to manage the Ace animation."""
        self.screen = screen
        self.ai_settings = ai_settings

        #Load the image.
        self.image = pygame.image.load('images/Ace.webp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        #Position the image at the center of the screen.
        self.rect.center = self.screen_rect.center

        self.visible = False
        self.display_time = 3000
        self.show_time = 0
        
    def blitme(self):
        """Draw the image on the screen."""
        if self.visible:
            self.screen.blit(self.image, self.rect)
            if pygame.time.get_ticks() - self.show_time > self. display_time:
                self.visible = False
                
    def show(self):
        self.visible = True
        self.show_time = pygame.time.get_ticks()