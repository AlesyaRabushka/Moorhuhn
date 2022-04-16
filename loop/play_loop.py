import pygame
from buttons import*
from chicken import Chicken


# PLAY
def play_loop(screen, buttons, cursor, cursor_group, chickens_group):
    running = True
    # turn off the image of the REAL 'CURSOR'
    pygame.mouse.set_visible(False)

    while running:
        screen.fill((90,100,45))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    return 1
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     if chicken.chickens[0].collidepoint(pygame.mouse.get_pos()):
            #         if event.button == 1:
            #             print('we shoot a chicken')
            elif event.type == pygame.MOUSEBUTTONDOWN:
                cursor.shoot(cursor, chickens_group)


        buttons.draw_text('Imagine that you play a game here', 50, 450, 100)
        buttons.draw_text('(нажми esc чтобы вернуться в главное меню)', 20, 450, 200)

        # logic of chicken flight
        # chicken.draw_chicken()
        # chicken.update()


        chickens_group.draw(screen)
        chickens_group.update()

        # draw an image instead of REAL CURSOR
        cursor_group.draw(screen)
        cursor_group.update()
        pygame.display.flip()
