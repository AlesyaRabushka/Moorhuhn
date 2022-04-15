import pygame
from buttons import*


# PLAY
def play_loop(screen, buttons):
    running = True

    while running:
        screen.fill((90,100,45))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    return 1


        buttons.draw_text('Imagine that you play a game here', 50, 450, 100)
        buttons.draw_text('(нажми esc чтобы вернуться в главное меню)', 20, 450, 200)
        pygame.display.flip()
