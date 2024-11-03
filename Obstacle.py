from settings import *
import random 

class Obstacle:
    def __init__(self):
        self.image = pygame.image.load('items/rock1.svg').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, max(0, max(0,  SCREEN_WIDTH - self.rect.width)))
        self.rect.y = random.randint(-SCREEN_HEIGHT, 0)


    def move(self):
        self.rect.y += 5
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.y = random.randint(-SCREEN_HEIGHT, 0)
            self.rect.y = random.randint(-SCREEN_HEIGHT, 0)
            self.rect.x = random.randint(0, max(0, max(0,  SCREEN_WIDTH - self.rect.width)))

    
    def draw(self):
        screen.blit(self.image, self.rect)