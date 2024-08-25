import pygame
from pygame.sprite import Group

from settings import Settings
from player import Player
from ace_animation import Ace

import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    clock = pygame.time.Clock()
    pygame.mouse.set_cursor(*pygame.cursors.broken_x)
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                     ai_settings.screen_height))
    pygame.display.set_caption("Target Practice")

    #Make a player and a group of bullets and a group of targets.
    player = Player(ai_settings, screen)
    ace = Ace(ai_settings, screen)
    bullets = Group()
    targets = Group()

    while True:
        gf.show_targets(ai_settings, screen, targets)
        gf.check_events(ai_settings, screen, player, bullets)
        player.update()
        gf.bullet_update(ai_settings, screen, targets, bullets, ace)
        gf.update_screen(ai_settings, screen, player, bullets, targets, ace)
        
        clock.tick(120)
run_game()