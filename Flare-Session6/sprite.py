import pygame
import os

# Sprite class for the main player character
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load all player images for animation
        # CHANGE THIS BASED ON YOUR COMPUTER'S FILE PATH STRUCTURE (READ THE README)
        self.image_location = [os.path.join("Flare-Session4" ,"assets", "player1.png"), 
                          os.path.join("Flare-Session4" ,"assets", "player2.png"), 
                          os.path.join("Flare-Session4" ,"assets", "player3.png"), 
                          os.path.join("Flare-Session4" ,"assets", "player4.png")] 
        
        # Load images into a list
        self.frames = [pygame.image.load(self.image_location[0]).convert_alpha(),
                       pygame.image.load(self.image_location[1]).convert_alpha(),
                       pygame.image.load(self.image_location[2]).convert_alpha(),
                       pygame.image.load(self.image_location[3]).convert_alpha()]

        # Animation variables
        self.frame_index = 0 # Current frame index
        self.image = self.frames[self.frame_index] # Current image
        self.image_idle = self.frames[0] # Idle image
        self.rect = self.image.get_rect() # Hitbox for player
        self.frame_timer = 0 # Frame timer
        self.direction = "right" # Player direction variable
        self.moving = False # Player moving variable
        self.y_speed

        # Set the x and y values of the image
        self.rect.x = 100
        self.rect.y = 200

    # Animation method
    def animate(self):
        if self.moving == True: # Check if the player is moving     
            # Animates every 10 frames
            if self.frame_timer >= 10:
                self.frame_timer = 0
                self.frame_index = (self.frame_index + 1) % len(self.frames)
                self.image = self.frames[self.frame_index]

            # Flip image if facing left
            if self.direction == "left":
                self.image = pygame.transform.flip(self.frames[self.frame_index], True, False)
                
            else:
                self.image = self.frames[self.frame_index]
                
        else: # Make him idle if he isn't moving
            
            # Idle animation
            
             # Flip image if facing left
            if self.direction == "left":
                self.image = pygame.transform.flip(self.image_idle, True, False)
                
            else:
                self.image = self.image_idle
    
    # Update method
    def update(self):
        print("Updating player sprite")
    
    # Movement method
    def move(self, x_change, y_change):
        self.rect.x += x_change # Move in the x direction
        self.rect.y += y_change # Move in the y direction

        