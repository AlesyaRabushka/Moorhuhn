import pygame


# PAUSE on PLAY mode
def pause_loop(screen, buttons):
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttons.pause_buttons[0].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1:
                        running = False
                        return 1
                elif buttons.pause_buttons[1].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1:
                        running = False
                        return 2

        screen.fill((255,204,255))
        buttons.draw_pause('Pause', 50, 200, 100)
        buttons.draw_pause('Main Menu', 50, 200, 200)
        pygame.display.flip()