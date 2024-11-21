from Settings import *

class Surfer:
    def __init__(self):
        # Load and scale the surfer image (optional)
        self.image = pygame.image.load('items\surfer.svg').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))
        
        # Define circle attributes
        self.radius = 12  # Half the width of the scaled image
        self.center = [SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100]  # Initial position
        
        self.speed = 5  # Movement speed

    def move(self, dx):
        # Update the surfer's horizontal position
        self.center[0] += dx * self.speed

        # Prevent the surfer from moving outside the screen boundaries
        if self.center[0] - self.radius < 0:  # Left boundary
            self.center[0] = self.radius
        if self.center[0] + self.radius > SCREEN_WIDTH:  # Right boundary
            self.center[0] = SCREEN_WIDTH - self.radius

    def draw(self):
        # Draw the circle for debugging purposes
        # pygame.draw.circle(screen, (255, 0, 0), self.center, self.radius, 2)

        # Optionally, draw the image centered at the circle
        image_rect = self.image.get_rect(center=self.center)
        screen.blit(self.image, image_rect)
