import sys
import pygame

from bullet import Bullet
from target import Target

def check_events(ai_settings, screen, player, bullets):
    """Respond to keyboard and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.moving_right = True
            elif event.key == pygame.K_a:
                player.moving_left = True
            elif event.key == pygame.K_SPACE:
                 player.jump()               
            elif event.key == pygame.K_q:
                sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player.moving_right = False
            elif event.key == pygame.K_a:
                player.moving_left = False
        elif event.type == pygame.MOUSEBUTTONDOWN:             
             ai_settings.bullet_sounds.play()
             fire_bullet(ai_settings, screen, player, bullets)
             
def fire_bullet(ai_settings, screen, player, bullets):
    """Fire bullets."""
    mouse_x, mouse_y = pygame.mouse.get_pos()
    new_bullet = Bullet(ai_settings, screen, player, mouse_x, mouse_y)
    bullets.add(new_bullet)

def show_targets(ai_settings, screen, targets):
    """Spawn one target at a time."""
    if len(targets) == 0:
        new_target = Target(ai_settings, screen)
        targets.add(new_target)

def bullet_update(ai_settings, screen, targets, bullets, ace):
    """Update the bullet's position and get rid of old ones."""
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0 or bullet.rect.top >= screen.get_rect().bottom:
            bullets.remove(bullet)

    collisions = pygame.sprite.groupcollide(bullets, targets, True, True)

    if collisions:
        
        ai_settings.collision_sounds[ai_settings.sound_index].play()
        ai_settings.sound_index = (ai_settings.sound_index + 1) % len(ai_settings.collision_sounds)
        if ai_settings.sound_index == 0:
            ace.show()
        show_targets(ai_settings, screen, targets)

def update_screen(ai_settings, screen, player, bullets, targets, ace):
    screen.fill(ai_settings.bg_color)

    #Redraw bullets behind the targets.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    player.blitme()
    targets.update()
    targets.draw(screen)
    ace.blitme()
    pygame.display.flip()