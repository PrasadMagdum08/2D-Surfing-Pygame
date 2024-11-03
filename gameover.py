from settings import *
import main
import home

def gameover(score):
    game_over_font = pygame.font.Font(None, 74)
    button_font = pygame.font.Font(None, 50)
    score_font = pygame.font.Font(None, 50)

    while True:
        screen.fill('skyblue')

        game_over_text = game_over_font.render("Game Over!", True, (255, 0, 0))
        screen.blit(game_over_text, (screen.get_width() // 2 - game_over_text.get_width() // 2, screen.get_height() // 3 - 140))


        score_text = score_font.render(f"Score: {score}", True, (34, 139, 34))
        screen.blit(score_text, (screen.get_width() // 2 - score_text.get_width() // 2, screen.get_height() // 3 + 50))

        try_again_text = button_font.render("Try Again", True, (255, 255, 255))
        home_text = button_font.render("Home", True, (255, 255, 255))
        
        try_again_button = pygame.Rect(screen.get_width() // 2 - 100, screen.get_height() // 2, 210, 50)
        home_button = pygame.Rect(screen.get_width() // 2 - 100, screen.get_height() // 2 + 70, 210, 50)
        
        pygame.draw.rect(screen, (255, 177, 0), try_again_button, border_radius=25)  
        pygame.draw.rect(screen, (0, 0, 128), home_button, border_radius=25)
        
        screen.blit(try_again_text, (try_again_button.x + 30, try_again_button.y + 10))
        screen.blit(home_text, (home_button.x + 60, home_button.y + 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if try_again_button.collidepoint(event.pos):
                    print('Game Restarted!')
                    main.main()  
                elif home_button.collidepoint(event.pos):
                    print("Going to Home")
                    home.home()

