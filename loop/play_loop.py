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


        buttons.draw_text('Let\'s PLAY!', 50, 300, 100)
        pygame.display.flip()
