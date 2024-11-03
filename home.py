from settings import *
import main
import random

class Clouds:
    def __init__(self):
        self.image = pygame.image.load('items/waves.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, max(0, max(0,  SCREEN_WIDTH - self.rect.width)))
        self.rect.y = random.randint(-SCREEN_HEIGHT, 0)


    def move(self):
        self.rect.y += 0.5
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.y = random.randint(-SCREEN_HEIGHT, 0)
            self.rect.y = random.randint(-SCREEN_HEIGHT, 0)
            self.rect.x = random.randint(0, max(0, max(0,  SCREEN_WIDTH - self.rect.width)))

    
    def draw(self):
        screen.blit(self.image, self.rect)


def home():
    game_over_font = pygame.font.Font(None, 74)
    button_font = pygame.font.Font(None, 50)
    clouds = [Clouds() for _ in range(5)]

    while True:

        screen.fill('white')
        
        for cloud in clouds:
            cloud.move()
            cloud.draw()



        home_text = game_over_font.render('WeLcOmE To 2D SuRfInG GaMe!', True, (0, 0, 0))
        screen.blit(home_text, (screen.get_width() // 2 - home_text.get_width() // 2, screen.get_height() // 3))


        start_game_text = button_font.render("Start Game", True, (255, 255, 255))
        exit_text = button_font.render("Exit", True, (255, 255, 255))
        
        start_game_button = pygame.Rect(screen.get_width() // 2 - 100, screen.get_height() // 2, 210, 50)
        exit_button = pygame.Rect(screen.get_width() // 2 - 100, screen.get_height() // 2 + 70, 200, 50)
        
        pygame.draw.rect(screen, (0, 128, 0), start_game_button, border_radius=25)
        pygame.draw.rect(screen, (255, 0, 0), exit_button, border_radius=25)
        
        screen.blit(start_game_text, (start_game_button.x + 10, start_game_button.y + 10))
        screen.blit(exit_text, (exit_button.x + 65, exit_button.y + 10))

    

        pygame.display.flip()
        pygame.display.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_game_button.collidepoint(event.pos):
                    print('Game Started!')
                    main.main() 
                elif exit_button.collidepoint(event.pos):
                    print("Exit")
                    return exit()
