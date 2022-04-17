import pygame


# HELP INFORMATION
def help_loop(screen, sounds, cursor_group, buttons):
    running = True

    sounds.main_theme_sound.play(-1)

    while running:
        screen.fill((90, 15, 45))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sounds.main_theme_sound.stop()
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sounds.main_theme_sound.stop()
                    running = False
                    return True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttons.help_buttons[0].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1:
                        sounds.main_theme_sound.stop()
                        sounds.button_click_sound.play()
                        running = False
                        return True

        # just a text
        buttons.draw_text('Help info!', 50, 300, 100)
        buttons.draw_help('Main Menu', 50, 300, 200)

        # draw an image instead of REAL CURSOR
        cursor_group.draw(screen)
        cursor_group.update()

        pygame.display.flip()