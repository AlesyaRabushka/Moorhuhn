from settings.buttons import *

# BEST SCORE
def best_score_loop(screen, sounds, cursor_group, buttons):
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # elif event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_ESCAPE:
            #         running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttons.best_score_buttons[0].collidepoint(pygame.mouse.get_pos()):
                    if event.button == 1:
                        sounds.button_click_sound.play()
                        running = False
                        return True

        screen.fill((204, 255, 153))
        buttons.draw_text('Best Score Table!', 50, 300, 100)
        buttons.draw_best_score('Main Menu', 50, 300, 200)

        # draw an image instead of REAL CURSOR
        cursor_group.draw(screen)
        cursor_group.update()

        pygame.display.flip()