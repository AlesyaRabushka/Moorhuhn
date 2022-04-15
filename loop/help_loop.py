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
                    return True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttons.help_buttons[0].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1:
                        running = False
                        return True

        # just a text
        buttons.draw_text('Help info!', 50, 300, 100)
        buttons.draw_help('Main Menu', 50, 300, 200)
        pygame.display.flip()