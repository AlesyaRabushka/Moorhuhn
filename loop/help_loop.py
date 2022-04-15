import pygame


# HELP INFORMATION
def help_loop(screen, buttons):
    running = True

    while running:
        screen.fill((90, 15, 45))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False


        buttons.draw_text('Help info!', 50, 300, 100)
        pygame.display.flip()