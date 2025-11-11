import sys
import os
import pygame
from player import Player

"""
SETUP section - preparing everything before the main loop runs
"""
pygame.init()

# Creating our main character and platforms through calling the Player class
main_c = Player(500, 400, 50, (0, 255, 0))  # Create our main character in the center of the screen
plat1 = Player(50, 500, 350, (255, 100, 100))  # Platform 1
plat2 = Player(425, 600, 250, (100, 255, 100)) # Platform 2
plat3 = Player(700, 450, 200, (100, 100, 255)) # Platform 3

# Global constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
FRAME_RATE = 60

# Useful colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Creating the screen and the clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.set_alpha(0)  # Make alpha bits transparent
clock = pygame.time.Clock()

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
        
        main_c.move(0, -5) # Move main character up by 5 pixels
        
    if keys_pressed[pygame.K_LEFT]:
        
        main_c.move(-5, 0) # Move main character left by 5 pixels
    
    if keys_pressed[pygame.K_RIGHT]:
        
        main_c.move(5, 0) # Move main character right by 5 pixels
    
    if keys_pressed[pygame.K_DOWN]:
        
        main_c.move(0, 5) # Move main character down by 5 pixels

    # Mouse events
    mouse_pos = pygame.mouse.get_pos()  # Get position of mouse as a tuple representing the (x, y) coordinate
   

    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:  # If left mouse pressed
        
        main_c.x = mouse_pos[0] # Change x pos to mouse x pos
        
        main_c.y = mouse_pos[1] # Change y pos to mouse y pos
    
    if mouse_buttons[2]:  # If right mouse pressed
        pass  # Replace this line



    """
    UPDATE section - manipulate everything on the screen
    """
    


    """
    DRAW section - make everything show up on screen
    """
    screen.fill(BLACK)  # Fill the screen with one colour

     # Draw our main character
    pygame.draw.rect(screen, main_c.color, (main_c.x, main_c.y, main_c.size, main_c.size)) 

    # Draw our platforms
    pygame.draw.rect(screen, plat1.color, (plat1.x, plat1.y, plat1.size, plat1.size/5))  # Platform 1
    pygame.draw.rect(screen, plat2.color, (plat2.x, plat2.y, plat2.size, plat2.size/5))  # Platform 2
    pygame.draw.rect(screen, plat3.color, (plat3.x, plat3.y, plat3.size, plat3.size/5))  # Platform 3
    
    pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
    clock.tick(FRAME_RATE)  # Pause the clock to always maintain FRAME_RATE frames per second
