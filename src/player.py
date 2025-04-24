import pygame

class Player():
    def __init__(self, ai_settings, screen):
        """Initialize the player's starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        #Load the player's image and get its rect.
        self.image = pygame.image.load('images/player.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Position the player at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Store decimal value for the player's center.
        self.center = float(self.rect.centerx)

        #Store the decimal value for jumping.
        self.y = float(self.rect.y)

        #Movement flags.
        self.moving_right = False
        self.moving_left = False
        self.on_ground = True
        self.jumping = False
        self.playing_sound = False
        self.player_footsteps = ai_settings.footsteps

        self.jump_velocity = 0
        self.gravity = ai_settings.gravity
        self.jump_speed = ai_settings.player_jump_speed
        self.jump_up = ai_settings.jumping_up
        self.jump_down = ai_settings.jumping_down

    def update(self):
        """Update player's position."""
        #Update the player's center value
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.player_speed
            if not self.playing_sound:
                self.player_footsteps.play(-1)
                self.playing_sound = True
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.player_speed
            if not self.playing_sound:
                self.player_footsteps.play(-1)
                self.playing_sound = True
        else:
            if self.playing_sound:
                self.player_footsteps.stop()
                self.playing_sound = False

        if self.jumping:
            self.y += self.jump_velocity
            self.jump_velocity += self.gravity
            if self.y >= self.screen_rect.bottom - self.rect.height:                
                self.y = self.screen_rect.bottom - self.rect.height
                self.jump_down.play()
                self.jumping = False
                self.on_ground = True
                
        #Update rect object position.
        self.rect.centerx = self.center
        self.rect.y = self.y
    
    def jump(self):
        """Check if the player is jumping."""
        if self.on_ground and not self.jumping:
            self.jump_up.play()
            self.jumping = True
            self.jump_velocity =+ self.jump_speed
            self.on_ground = False
            

    def blitme(self):
        """Draw the player image on the screen."""
        self.screen.blit(self.image, self.rect)