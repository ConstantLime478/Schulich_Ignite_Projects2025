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
JUMP_VELOCITY = -15
y_speed = 5
x_speed = 5
GRAVITY = 9.8

# Useful colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Creating the screen and the clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.set_alpha(0)  # Make alpha bits transparent
clock = pygame.time.Clock()

# Importing Important Classes
from sprite import Player
from platform2 import Platform

# Creating our spirte and platform objects
main_c = Player() # Our main character
plat1 = Platform(50, 500, 350, 350/4)  # Platform 1
plat2 = Platform(425, 600, 250, 250/4) # Platform 2
plat3 = Platform(700, 450, 200, 200/4) # Platform 3

# Making the background
# Taken from https://www.reddit.com/r/PixelArt/comments/j7751a/mt_fuji_study/
background = pygame.image.load(os.path.join("Flare-Session4" , "assets", "background.png")).convert_alpha()
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

    # Keyboard events
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP]:
        
        main_c.move(0, -y_speed) # Move main character up by 5 pixels
        main_c.moving = True # Showing that he is moving
    
    elif keys_pressed[pygame.K_SPACE]:
        y_speed = JUMP_VELOCITY
        main_c.move(0, -y_speed) # Make the main character jump with a set velocity
        main_c.moving = True # Showing that he is moving
        y_speed += GRAVITY # Simulate gravity effect by increasing downward speed
        main_c.rect.y += y_speed   
        
    elif keys_pressed[pygame.K_LEFT]:
        
        main_c.move(-x_speed, 0) # Move main character left by 5 pixels
        main_c.direction = "left" # Change sprite image direction
        main_c.frame_timer += 1 # Frame timer for animation
        main_c.moving = True # Showing that he is moving
        
    elif keys_pressed[pygame.K_RIGHT]:
        
        main_c.move(x_speed, 0) # Move main character right by 5 pixels
        main_c.direction = "right" # Change sprite image direction
        main_c.frame_timer += 1 # Frame timer for animation
        main_c.moving = True # Showing that he is moving
        
    elif keys_pressed[pygame.K_DOWN]:
        
        main_c.move(0, y_speed) # Move main character down by 5 pixels
        main_c.moving = True # Showing that he is moving
        
    else:
        main_c.moving = False # Showing that he is not moving
        main_c.frame_timer = 0 # Reset frame timer when not moving
        
    # Mouse events
    mouse_pos = pygame.mouse.get_pos()  # Get position of mouse as a tuple representing the (x, y) coordinate
   

    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:  # If left mouse pressed
        
        main_c.x = mouse_pos[0] # Change x pos to mouse x pos
        
        main_c.y = mouse_pos[1] # Change y pos to mouse y pos
    


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
