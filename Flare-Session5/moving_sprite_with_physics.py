import sys
import os
import pygame

"""
SETUP section - preparing everything before the main loop runs
"""
pygame.init()

# Global constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
FRAME_RATE = 60

#  Movement and physics constants
PLAYER_SPEED = 5 # Speed of the player in pixels per frame
GRAVITY = 1  # Gravity effect in pixels per frame
JUMP_STRENGTH = 15  # Initial jump velocity in pixels per frame

# Useful colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Creating the screen and the clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.set_alpha(0)  # Make alpha bits transparent
clock = pygame.time.Clock()

# Importing Important Classes
from sprite_updated import Player
from platform2 import Platform

# Creating our spirte and platform objects
main_c = Player() # Our main character
plat1 = Platform(50, 500, 300, 350/4)  # Platform 1
plat2 = Platform(425, 600, 200, 250/4) # Platform 2
plat3 = Platform(700, 550, 150, 200/4) # Platform 3
plats = [plat1, plat2, plat3]

# Making the background
# Taken from https://www.reddit.com/r/PixelArt/comments/j7751a/mt_fuji_study/
background = pygame.image.load(os.path.join("Flare-Session5" , "assets", "background.png")).convert_alpha()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = screen.get_rect()

# Creating sprite groups
mains = pygame.sprite.Group()
platforms = pygame.sprite.Group()

# Adding our sprite objects to their corresponding sprite group
mains.add(main_c)
platforms.add(plat1, plat2, plat3)

"""
MAIN LOOP section
"""

while True:
    """
    EVENTS section - how the code reacts when users do things
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # When user clicks the 'x' on the window, close our game
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # JUMP
            if event.key == pygame.K_UP and main_c.on_ground:
                    main_c.velocity_y = -JUMP_STRENGTH
                    main_c.on_ground = False   

    # LEFT/RIGHT MOVEMENT
    keys = pygame.key.get_pressed() # Stroing current key presses
    dx = 0 # Change in x position
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
    dy = main_c.velocity_y # vertical movement

    # Move on x-axis
    main_c.rect.x += dx 

    # Collision detection on x-axis
    for plat in plats:
        if pygame.sprite.collide_rect(main_c, plat):
            if dx > 0:
                main_c.rect.right = plat.rect.left  # hit platform from left
            elif dx < 0:
                main_c.rect.left = plat.rect.right  # hit platform from right

    
    # move along y-axis
    main_c.rect.y += dy

    main_c.on_ground = False

    # Collision detection on y-axis
    for plat in plats:
        if pygame.sprite.collide_rect(main_c, plat):
            # Check if falling
            if main_c.velocity_y > 0 and main_c.rect.bottom >= plat.rect.top:
                main_c.rect.bottom = plat.rect.top
                main_c.on_ground = True
                main_c.velocity_y = 0
            # Check upward collision
            elif main_c.velocity_y < 0 and main_c.rect.top <= plat.rect.bottom:
                main_c.rect.top = plat.rect.bottom
                main_c.velocity_y = 0

    # update the moving value
    main_c.moving = dx != 0


    """
    UPDATE section - manipulate everything on the screen
    """
    


    """
    DRAW section - make everything show up on screen
    """
    screen.fill(BLACK)  # Fill the screen with one colour

    screen.blit(background, screen_rect)  # Draw the background image
    
    # Draw our main character
    mains.draw(screen)
    main_c.animate() # Animate our main character
    
    # Draw our platforms
    platforms.draw(screen)
    
    pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
    clock.tick(FRAME_RATE)  # Pause the clock to always maintain FRAME_RATE frames per second
