from settings.buttons import*
from objects.holes import Holes


# is used to select one of the buttons
# on MAIN MENU screen
def main_menu_loop(screen, sounds, cursor_group, buttons, chicken_hole, holes):
    running = True

    # turn off the image of the REAL 'CURSOR'
    pygame.mouse.set_visible(False)

    # main theme SOUND
    sounds.main_theme_sound.play(-1)
    back = pygame.image.load("img/main_menu_background/main_menu.png")
    back_rect = back.get_rect()

    new_holes_max_time = 15
    new_holes_current_time = 0
    index = 0
    count = 0

    while running:
        screen.fill((0, 100, 0))
        screen.blit(back, back_rect)


        buttons.draw_main_menu('start', 50, 300, 100)
        buttons.draw_main_menu('Best Score', 50, 300, 200)
        buttons.draw_main_menu('Help', 50, 300, 300)
        buttons.draw_main_menu('Exit', 50, 300, 400)
        # check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sounds.main_theme_sound.stop()
                running = False
            elif event.type == pygame.MOUSEMOTION:
                if buttons.main_menu_buttons[0].collidepoint(pygame.mouse.get_pos()):
                    buttons.draw_main_menu('start_h', 50, 300, 100)
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
                        for hole in holes:
                            hole.shot()

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

        chicken_hole.update()


        new_holes_current_time += 1



        if new_holes_current_time == new_holes_max_time:
            index += 1
            new_holes_current_time = 0
            if index <= 4:
                holes.add(Holes(screen, index))

        holes.update(sounds)

        # draw an image instead of REAL CURSOR
        cursor_group.draw(screen)
        cursor_group.update()


        pygame.display.flip()
