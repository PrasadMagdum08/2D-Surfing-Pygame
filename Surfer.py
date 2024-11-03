from settings import *

class Surfer:
    def __init__(self):
        self.image = pygame.image.load('items/surfer.svg').convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 70))
        
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)
        self.speed = 5

    def move(self, dx):
        self.rect.x += dx * self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def draw(self):
        screen.blit(self.image, self.rect)