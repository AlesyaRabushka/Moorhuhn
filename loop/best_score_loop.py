import pygame
from buttons import *

# BEST SCORE
def best_score_loop(screen):
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        but = Button(screen)
        but.draw_text('Best Score Table!', 50, 300, 100)
        screen.fill((204,255,153))
        pygame.display.flip()