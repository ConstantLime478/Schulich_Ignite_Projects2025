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

# Useful colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Creating the screen and the clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# x (left), y (top), width, height 
rect = pygame.Rect(0, 0, 200, 150)

x_move = 5
y_move = 5

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
        pass  # Replace this line
    if keys_pressed[pygame.K_LEFT]:
        pass  # Replace this line
    if keys_pressed[pygame.K_RIGHT]:
        pass  # Replace this line
    if keys_pressed[pygame.K_DOWN]:
        pass  # Replace this line

    # Mouse events
    mouse_pos = pygame.mouse.get_pos()
    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:
        pass  # Replace this line
    if mouse_buttons[2]:
        pass  # Replace this line

    """
    UPDATE section - manipulate everything on the screen
    """

    # Move horizontally first
    rect.x += x_move

    # Then check for boundaries *after* movement
    if rect.x == SCREEN_WIDTH - rect.width:
        #rect.x = SCREEN_WIDTH - rect.width  # Clamp to edge
        x_move = -x_move
    elif rect.x == 0:
       # rect.x = 0  # Clamp to edge
        x_move = -x_move
        
    # Move horizontally first
    rect.y += y_move

    # Then check for boundaries *after* movement
    if rect.y == SCREEN_HEIGHT - rect.height:
        #rect.x = SCREEN_WIDTH - rect.width  # Clamp to edge
        y_move = -y_move
    elif rect.y == 0:
       # rect.x = 0  # Clamp to edge
        y_move = -y_move

    """
    DRAW section - make everything show up on screen
    """
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, rect)

    pygame.display.flip()
    clock.tick(FRAME_RATE)
