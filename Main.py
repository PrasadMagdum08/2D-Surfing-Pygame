from Settings import *
from Surfer import *
from Obstacle import *
import Gameover
import Home
import math


def circle_collision(circle1_center, circle1_radius, circle2_center, circle2_radius):
    """
    Detect collision between two circles.
    """
    distance = math.sqrt(
        (circle1_center[0] - circle2_center[0]) ** 2 +
        (circle1_center[1] - circle2_center[1]) ** 2
    )
    return distance < (circle1_radius + circle2_radius)


def check_collision(player, obstacles):
    """
    Check collision between the player (surfer) and obstacles.
    """
    for obstacle in obstacles:
        if circle_collision(player.center, player.radius, obstacle.center, obstacle.radius):
            return True
    return False


def main():
    running = True
    surfer = Surfer()

    # Create a list of obstacles with random types
    obstacles = [Obstacle(obstacle_type=random.randint(0, 2)) for _ in range(10)]

    score = 0
    font = pygame.font.Font(None, 36)

    game_running = True
    button_size = 30
    button_x, button_y = SCREEN_WIDTH - button_size - 10, 10

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if button_x <= mouse_x <= button_x + button_size and button_y <= mouse_y <= button_y + button_size:
                    game_running = not game_running

        if game_running:
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

            # Check if score is a multiple of 1000 and add more obstacles
            if score % 100 == 0:
                new_obstacle = Obstacle(obstacle_type=random.randint(0, 2))  # Randomly choose obstacle type
                obstacles.append(new_obstacle)  # Add it to the list

            score_text = font.render(f"Score: {score}", True, (0, 0, 0))
            screen.blit(score_text, (500, 10))

            if check_collision(surfer, obstacles):
                print('Game Over!')
                Gameover.gameover(score)
                running = False

        if game_running:
            # Draw pause icon (two vertical bars)
            pygame.draw.rect(screen, BLACK, (button_x, button_y, button_size // 2 - 2, button_size))
            pygame.draw.rect(screen, BLACK, (button_x + button_size // 2 + 2, button_y, button_size // 2 - 2, button_size))
        else:
            # Draw play icon (triangle)
            pygame.draw.polygon(screen, BLACK, [(button_x, button_y), (button_x, button_y + button_size), (button_x + button_size, button_y + button_size // 2)])

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    Home.home()
