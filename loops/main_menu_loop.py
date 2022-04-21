from settings.buttons import*
from objects.holes import Holes
from objects.chicken_hole import ChickenHole


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
    moorhuhn = pygame.image.load("img/main_menu_background/moorhuhn.png")
    moorhuhn_rect = moorhuhn.get_rect(center=(400,66))

    # for HOLES
    new_holes_max_time = 15
    new_holes_current_time = 0
    index = 0
    finish = False

    while running:
        screen.fill((0, 100, 0))
        screen.blit(back, back_rect)
        screen.blit(moorhuhn, moorhuhn_rect)


        buttons.draw_main_menu('start', 50, 70, 550)
        buttons.draw_main_menu('Best Score', 50, 300, 550)
        buttons.draw_main_menu('Help', 50, 500, 550)
        buttons.draw_main_menu('Exit', 50, 600, 550)

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
                        for hole in holes:
                            hole.shot()
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
                        for hole in holes:
                            hole.shot()
                        running = False
                        return  3
                elif buttons.main_menu_buttons[3].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1:
                        sounds.button_click_sound.play()
                        sounds.main_theme_sound.stop()
                        for hole in holes:
                            hole.shot()
                        running = False
                        return  4




        new_holes_current_time += 1
        if new_holes_current_time == new_holes_max_time:
            index += 1
            new_holes_current_time = 0
            if index < 4:
                holes.add(Holes(screen, index))
            if index == 4:
                holes.add(Holes(screen, index))
                finish = True

        holes.update(sounds)
        # if finish:
        #     chicken_hole.update()
        chicken_hole.update()

        # draw an image instead of REAL CURSOR
        cursor_group.draw(screen)
        cursor_group.update()


        pygame.display.flip()
