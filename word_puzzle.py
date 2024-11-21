import pygame
import random

# Initialize Pygame
pygame.init()

# Game Constants
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
FONT_SIZE = 50
BUTTON_WIDTH = 120
BUTTON_HEIGHT = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Word Assemble Game")
font = pygame.font.Font(None, FONT_SIZE)
small_font = pygame.font.Font(None, FONT_SIZE // 2)

# Word list
WORD_LIST = ['PYTHON', 'GAME', 'PUZZLE', 'ASSEMBLE', 'HELLO']

# Shuffle the letters of a word
def shuffle_word(word):
    letters = list(word)
    random.shuffle(letters)
    return letters

# Draw buttons for each letter
def draw_buttons(buttons):
    for letter, rect in buttons:
        pygame.draw.rect(screen, WHITE, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)
        text = font.render(letter, True, BLACK)
        screen.blit(text, text.get_rect(center=rect.center))

# Check if the assembled word is correct
def is_correct(word, assembled):
    return word == ''.join(assembled)

# Display a popup
def show_popup(message):
    popup = pygame.Surface((400, 200))
    popup.fill(WHITE)
    pygame.draw.rect(popup, BLACK, popup.get_rect(), 2)
    text = font.render(message, True, BLUE)
    text_rect = text.get_rect(center=(200, 100))
    popup.blit(text, text_rect)
    screen.blit(popup, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 100))
    pygame.display.flip()
    pygame.time.delay(2000)

# Main Game Loop
def main():
    running = True
    score = 0
    current_word = random.choice(WORD_LIST)
    shuffled_letters = shuffle_word(current_word)
    buttons = []

    # Create button rects for shuffled letters
    button_x = 100
    button_y = SCREEN_HEIGHT // 2
    for letter in shuffled_letters:
        rect = pygame.Rect(button_x, button_y, BUTTON_WIDTH, BUTTON_HEIGHT)
        buttons.append((letter, rect))
        button_x += BUTTON_WIDTH + 20  # Spacing between buttons

    assembled_letters = []
    feedback = ""

    while running:
        screen.fill(WHITE)

        # Draw the score
        score_text = small_font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (20, 20))

        # Draw the shuffled letter buttons
        draw_buttons(buttons)

        # Draw the assembled word
        assembled_text = ''.join(assembled_letters)
        assembled_word_surface = font.render(assembled_text, True, BLACK)
        screen.blit(assembled_word_surface, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 3))

        # Draw feedback (correct/incorrect)
        if feedback:
            feedback_surface = small_font.render(feedback, True, GREEN if feedback == "Correct!" else RED)
            screen.blit(feedback_surface, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 3 + 60))

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for letter, rect in buttons:
                    if rect.collidepoint(x, y):
                        assembled_letters.append(letter)
                        buttons.remove((letter, rect))
                        break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Check assembled word
                    if is_correct(current_word, assembled_letters):
                        feedback = "Correct!"
                        score += len(current_word)

                        # Show the popup
                        show_popup("Congratulations! You have won the game.")
                        
                        # Prepare the next word
                        current_word = random.choice(WORD_LIST)
                        shuffled_letters = shuffle_word(current_word)
                        buttons = []
                        button_x = 100
                        for letter in shuffled_letters:
                            rect = pygame.Rect(button_x, button_y, BUTTON_WIDTH, BUTTON_HEIGHT)
                            buttons.append((letter, rect))
                            button_x += BUTTON_WIDTH + 20
                        assembled_letters = []
                    else:
                        feedback = "Incorrect!"
                        assembled_letters = []

                if event.key == pygame.K_BACKSPACE:  # Remove last letter
                    if assembled_letters:
                        removed_letter = assembled_letters.pop()
                        rect_x = 100 + (len(buttons) * (BUTTON_WIDTH + 20))
                        rect = pygame.Rect(rect_x, button_y, BUTTON_WIDTH, BUTTON_HEIGHT)
                        buttons.append((removed_letter, rect))

        pygame.display.flip()
        pygame.time.Clock().tick(30)

    pygame.quit()

# Run the game
if __name__ == "__main__":
    main()
