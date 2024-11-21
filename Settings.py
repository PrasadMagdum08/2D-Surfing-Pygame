import pygame

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

pygame.display.set_caption('2D Surfing Game')

clock = pygame.time.Clock()