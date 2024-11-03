from settings import *
from Surfer import *
from Obstacle import *
import gameover
import home

score = 0 

def check_collision(player, obstacles):
    for obstacle in obstacles:
        if player.rect.colliderect(obstacle.rect):
            return True
    return False
    
def main():
    running = True
    surfer = Surfer()
    obstacles = [Obstacle() for _ in range(5)]
    
    font = pygame.font.Font(None, 36)  

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            surfer.move(-1)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            surfer.move(1)

        screen.fill('skyblue')
        
        for obstacle in obstacles:
            obstacle.move()
            obstacle.draw()

        surfer.draw()

        score += 1 
        score_text = font.render(f"Score: {score}", True, (0, 0, 0)) 
        screen.blit(score_text, (450, 10))

        if check_collision(surfer, obstacles):
            print('Game Over!')
            gameover.gameover(score) 
            running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    home.home()
