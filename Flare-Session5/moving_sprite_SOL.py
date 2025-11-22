import sys
import os
import pygame

"""
SETUP section
"""
pygame.init()

# Global constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
FRAME_RATE = 60

PLAYER_SPEED = 5
GRAVITY = 1  # smaller value works better with velocity-based movement
JUMP_STRENGTH = 15

# Colors 
BLACK = (0, 0, 0)

# Creating the screen and the clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Importing classes
from sprite_updated import Player
from platform2 import Platform

# Create objects
main_c = Player()
main_c.on_ground = False
main_c.velocity_y = 0  # vertical velocity

plat1 = Platform(50, 500, 300, 350/4)
plat2 = Platform(425, 600, 200, 250/4)
plat3 = Platform(700, 550, 150, 200/4)
plats = [plat1, plat2, plat3]

# Background
background = pygame.image.load(os.path.join("Flare-Session4", "assets", "background.png")).convert_alpha()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = screen.get_rect()

# Sprite groups
mains = pygame.sprite.Group(main_c)
platforms = pygame.sprite.Group(plat1, plat2, plat3)


# Main game loop

while True:
    
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # --- JUMP ---
            if event.key == pygame.K_UP and main_c.on_ground:
                main_c.velocity_y = -JUMP_STRENGTH
                main_c.on_ground = False

    # Keyboard input (LEFT/RIGHT)
    keys = pygame.key.get_pressed()
    dx = 0
    if keys[pygame.K_LEFT]:
        dx -= PLAYER_SPEED
        main_c.direction = "left" # Change sprite image direction
        main_c.frame_timer += 1 # Frame timer for animation
    if keys[pygame.K_RIGHT]:
        dx += PLAYER_SPEED
        main_c.direction = "right" # Change sprite image direction
        main_c.frame_timer += 1 # Frame timer for animation

    # GRAVITY
    main_c.velocity_y += GRAVITY
    dy = main_c.velocity_y

    # Move along x-axis
    main_c.rect.x += dx

    for plat in plats:
        if pygame.sprite.collide_rect(main_c, plat):
            if dx > 0:
                main_c.rect.right = plat.rect.left  # hit platform from left
            elif dx < 0:
                main_c.rect.left = plat.rect.right  # hit platform from right

    
    # move along y-axis
    main_c.rect.y += dy

    main_c.on_ground = False  # reset; will check below

    for plat in plats:
        if pygame.sprite.collide_rect(main_c, plat):
            # Check if falling
            if main_c.velocity_y > 0 and main_c.rect.bottom >= plat.rect.top:
                main_c.rect.bottom = plat.rect.top
                main_c.on_ground = True
                main_c.velocity_y = 0
            # Optional: check upward collision (head bump)
            elif main_c.velocity_y < 0 and main_c.rect.top <= plat.rect.bottom:
                main_c.rect.top = plat.rect.bottom
                main_c.velocity_y = 0

    # update the moving flag
    main_c.moving = dx != 0

    # draw
    screen.fill(BLACK)
    screen.blit(background, screen_rect)

    mains.draw(screen)
    main_c.animate()

    platforms.draw(screen)

    pygame.display.flip()
    clock.tick(FRAME_RATE)
