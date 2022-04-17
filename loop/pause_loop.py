import pygame


# PAUSE on PLAY mode
def pause_loop(screen, buttons, cursor):
    running = True
    # turn off the image of the REAL 'CURSOR'
    pygame.mouse.set_visible(False)

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
                        # set the REAL CURSOR back
                        #pygame.mouse.set_visible(True)
                        return 2

        screen.fill((255,204,255))
        buttons.draw_pause('Main Menu', 50, 200, 200)
        buttons.draw_pause('Exit', 50, 200, 100)


        # draw an image instead of REAL CURSOR
        # and update its position
        cursor.draw(screen)
        cursor.update()
        pygame.display.flip()