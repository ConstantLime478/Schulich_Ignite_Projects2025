
# Solution of Exercise - Adding platforms
"""Any platformer needs platforms!
Make a platform class and draw them."""

# By Hayyan Khan 28th-October-2025

import sys
import os
import pygame

class Box:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color  

class Platform:
    def __init__(self):
        """Initialize the platform animation."""
        pygame.init()

        # Screen setup
        self.SCREEN_WIDTH = 1000
        self.SCREEN_HEIGHT = 800
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.screen.set_alpha(0)  # Make alpha bits transparent

        # Frame rate
        self.FRAME_RATE = 60
        self.clock = pygame.time.Clock()

        # Colors
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.YELLOW = (220,255,50)
        self.MAGENTA= (255,0,180)
        self.CYAN = (100,180,255)
        self.VIOLET = (70,0,255)
        self.LIME = (130,255,50)

        # Speed of platform movement
        self.SPEED = 2

        # Platforms using Box class
        box_r = Box(160, 220, 200, self.RED)
        box_g = Box(360, 370, 200, self.GREEN)
        box_b = Box(560, 270, 200, self.BLUE)
        box_y = Box(760, 420, 200, self.YELLOW)
        box_m = Box(160, 520, 300, self.MAGENTA)
        box_c = Box(360, 150, 200, self.CYAN)
        box_v = Box(760, 320, 200, self.VIOLET)  
        box_l = Box(560, 600, 300, self.LIME)
        boxes = [box_r, box_g, box_b, box_y, box_m, box_c, box_v, box_l]
        self.boxes = boxes

    def run(self):
        while True:
            """
            EVENTS section - how the code reacts when users do things
            """
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # When user clicks the 'x' on the window, close our game
                    pygame.quit()
                    sys.exit()

            


            """
            DRAW section - make everything show up on screen
            """
            self.screen.fill(self.BLACK)  # Fill the screen with one colour

            #------------Drawing platforms------------
            for i in range(len(self.boxes)):
                pygame.draw.rect(self.screen, self.boxes[i].color, (self.boxes[i].x, self.boxes[i].y, self.boxes[i].size, self.boxes[i].size/4))
            
            
            #------------Animating platforms------------
                self.boxes[i].x -= 2 

                if self.boxes[i].x + self.boxes[i].size < 0:
                    self.boxes[i].x = self.SCREEN_WIDTH + self.boxes[i].size / 2

            pygame.display.flip()  # Pygame uses a double-buffer, without this we see half-completed frames
            self.clock.tick(self.FRAME_RATE)  # Pause the clock to always maintain FRAME_RATE frames per second

p = Platform()
p.run()

