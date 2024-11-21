from Settings import *
import random

class Obstacle:
    def __init__(self, obstacle_type=0):
        # Define available obstacle types and corresponding images and sizes
        self.obstacle_type = obstacle_type

        if self.obstacle_type == 0:
            # Default rock obstacle
            self.image = pygame.image.load('items/rock.svg').convert_alpha()
            self.image = pygame.transform.scale(self.image, (100, 100))
            self.radius = 25
        elif self.obstacle_type == 1:
            # New obstacle type: barrel
            self.image = pygame.image.load('items/barrel.svg').convert_alpha()
            self.image = pygame.transform.scale(self.image, (60, 60))
            self.radius = 25
        elif self.obstacle_type == 2:
            # New obstacle type: bush
            self.image = pygame.image.load('items/bush.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (80, 80))
            self.radius = 25

        # Set the position of the obstacle randomly within the screen
        self.center = [
            random.randint(self.radius, SCREEN_WIDTH - self.radius),
            random.randint(-SCREEN_HEIGHT, 0)  # y-coordinate starts above the screen
        ]

    def move(self):
        # Move the obstacle downward
        self.center[1] += 5

        # Reset position if it moves off the bottom of the screen
        if self.center[1] - self.radius > SCREEN_HEIGHT:
            self.center[1] = random.randint(-SCREEN_HEIGHT, 0)
            self.center[0] = random.randint(self.radius, SCREEN_WIDTH - self.radius)

    def draw(self):
        # Draw the image centered at the obstacle's position
        image_rect = self.image.get_rect(center=self.center)
        screen.blit(self.image, image_rect)
