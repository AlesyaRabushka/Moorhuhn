import pygame


# HELP INFORMATION
def help_loop(screen, sounds, cursor_group, buttons):
    running = True

    sounds.main_theme_sound.play(-1)
    bg = pygame.transform.scale(pygame.image.load('img/help_background/help_back.png'), (800,600))
    bg_rect = bg.get_rect()

    while running:
        screen.fill((90, 15, 45))
        screen.blit(bg, bg_rect)

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
        buttons.draw_text('Right Mouse Button - to shoot', 40, 350, 200)
        buttons.draw_text('SPACE - to reload ammo', 40, 300, 300)
        buttons.draw_help('Main Menu', 50, 300, 400)

        # draw an image instead of REAL CURSOR
        cursor_group.draw(screen)
        cursor_group.update()

        pygame.display.flip()