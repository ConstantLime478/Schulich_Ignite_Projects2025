import sys
import os
import pygame
from box import Box


class Platform:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Constants
        self.SCREEN_WIDTH = 1000
        self.SCREEN_HEIGHT = 800
        self.FRAME_RATE = 60
        self.SPEED = 0.8  # Slow smooth speed

        # Colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.BROWN = (128, 113, 83)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.YELLOW = (220, 255, 50)
        self.MAGENTA = (255, 0, 180)
        self.CYAN = (100, 180, 255)
        self.VIOLET = (70, 0, 255)
        self.LIME = (130, 255, 50)

        # Screen and clock
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.screen.set_alpha(0)
        self.clock = pygame.time.Clock()

        # Create evenly spaced boxes horizontally across the screen
        start_x_positions = [i * 160 for i in range(8)]
        colors = [
            self.RED, self.GREEN, self.BLUE, self.YELLOW,
            self.MAGENTA, self.CYAN, self.VIOLET, self.LIME
        ]
        y_positions = [220, 370, 270, 420, 520, 150, 320, 600]

        self.boxes = [
            Box(start_x_positions[i], y_positions[i], 200, colors[i])
            for i in range(8)
        ]

        
    def handle_events(self):
        """Handle user input and system events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        """Update box positions."""
        for box in self.boxes:
            box.x -= self.SPEED
            # Wrap around smoothly to right side when fully off-screen
            if box.x + box.size < 0:
                box.x = self.SCREEN_WIDTH + box.size / 2

    def draw(self):
        """Draw everything on the screen."""
        self.screen.fill(self.BLACK)

        for box in self.boxes:
                # Check if box color is LIME or MAGENTA
            if box.color in [self.LIME, self.MAGENTA]:
                pygame.draw.rect(
                self.screen,
                box.color,
                (box.x, box.y, box.size*1.5, box.size/4)
                )
            else:
                
                pygame.draw.rect(
                    self.screen,
                    box.color,
                    (box.x, box.y, box.size, box.size / 4)
                )

        pygame.display.flip()

    def run(self):
        """Main game loop."""
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.FRAME_RATE)


# # Run the animation
# if __name__ == "__main__":
#     Platform().run()
