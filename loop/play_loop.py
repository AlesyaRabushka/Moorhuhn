from settings.buttons import*
from objects.chicken import Chicken
from random import randint

# PLAY mode
def play_loop(screen, sounds, buttons, cursor, cursor_group, chickens_group):
    print('PLAY mode')

    # background SOUND
    sounds.play_background.play(-1)

    running = True
    pause = False
    # turn off the image of the REAL 'CURSOR'
    pygame.mouse.set_visible(False)

    while running:
        screen.fill((90,100,45))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sounds.play_background.stop()
                running = False
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sounds.play_background.stop()
                    running = False
                    return 1

            # add new CHICKEN on the screen0
            elif event.type == pygame.USEREVENT:
                y1 = randint(50,500)
                chickens_group.add(Chicken(screen, y1))
                chickens_group.add(Chicken(screen, randint(50,500)))
                # y2 = randint(50,500)
                # if y2 - y1 < 50:
                #     chickens_group.add(Chicken(screen, y2 + 30))
                # elif y1 - y2 < 50:
                #     chickens_group.add(Chicken(screen, y1 + 4))
            # checks if we have shot a CHICKEN
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # add SHOT SOUND
                sounds.shot_sound.play()

                cursor.shoot(sounds, chickens_group)

        buttons.draw_text('Imagine that you play a game here', 50, 450, 100)
        buttons.draw_text('(нажми esc чтобы вернуться в главное меню)', 20, 450, 200)



        chickens_group.draw(screen)
        chickens_group.update()

        # draw an image instead of REAL CURSOR
        cursor_group.draw(screen)
        cursor_group.update()


        pygame.display.flip()
