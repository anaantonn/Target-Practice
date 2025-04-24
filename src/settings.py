from pygame import mixer

class Settings():
    def __init__(self):
        """Various game settings for different elements."""
        #Display settings.
        self.screen_width = 1500
        self.screen_height = 900
        self.bg_color = (255, 255, 255)

        #Bullet settings.
        self.bullet_speed = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        #Target settings.
        self.target_speed = 0.5
        self.direction = 1

        #Player settings.
        self.player_speed = 5
        self.player_jump_speed = -10
        self.gravity = 0.5

        #Sound effects.
        mixer.init(frequency = 44100, size = -16, channels = 2, buffer = 64)
        self.sound_index = 0
        self.footsteps = mixer.Sound('sound_effects/Footsteps.wav')
        self.bullet_sounds = mixer.Sound('sound_effects/Vandal.wav')
        self.jumping_up = mixer.Sound('sound_effects/Jump_up.wav')
        self.jumping_down = mixer.Sound('sound_effects/Jump_down.wav')
        self.collision_sounds = [
            mixer.Sound('sound_effects/Kill_1.wav'), 
            mixer.Sound('sound_effects/Kill_2.wav'),
            mixer.Sound('sound_effects/Kill_3.wav'),
            mixer.Sound('sound_effects/Kill_4.wav'),
            mixer.Sound('sound_effects/Kill_5.wav')
            ]