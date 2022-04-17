from settings.buttons import*



# is used to select one of the buttons
# on MAIN MENU screen
def choose_loop(screen, sounds, cursor_group, buttons):
    running = True

    # turn off the image of the REAL 'CURSOR'
    pygame.mouse.set_visible(False)

    # main theme SOUND
    sounds.main_theme_sound.play(-1)

    while running:
        # check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sounds.main_menu_sound.stop()
                running = False
            # elif event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_ESCAPE:
            #         running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttons.main_menu_buttons[0].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1:
                        sounds.button_click_sound.play()
                        sounds.main_theme_sound.stop()
                        running = False
                        return 1
                elif buttons.main_menu_buttons[1].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1:
                        sounds.button_click_sound.play()
                        sounds.main_theme_sound.stop()
                        running = False
                        return  2
                elif buttons.main_menu_buttons[2].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1:
                        sounds.button_click_sound.play()
                        sounds.main_theme_sound.stop()
                        running = False
                        return  3
                elif buttons.main_menu_buttons[3].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1:
                        sounds.button_click_sound.play()
                        sounds.main_theme_sound.stop()
                        running = False
                        return  4




        screen.fill((0, 100, 0))
        buttons.draw_main_menu('Play', 50, 300, 100)
        buttons.draw_main_menu('Best Score', 50, 300, 200)
        buttons.draw_main_menu('Help', 50, 300, 300)
        buttons.draw_main_menu('Exit', 50, 300, 400)

        # draw an image instead of REAL CURSOR
        cursor_group.draw(screen)
        cursor_group.update()


        pygame.display.flip()
