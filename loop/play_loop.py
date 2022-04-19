import sys
import time

from settings.buttons import*
from objects.chicken import Chicken
from random import randint

# PLAY mode
def play_loop(clock, screen, sounds, buttons, cursor, cursor_group, chickens_group, ammo, scores, pumpkin):

    # background SOUND
    sounds.play_background.play(-1)

    running = True
    pause = False
    # turn off the image of the REAL 'CURSOR'
    pygame.mouse.set_visible(False)

    # initialize time value
    # to know if we have to start counting time
    init_time = 0

    while running:
        screen.fill((90,100,45))

        # Returns milliseconds between each call to 'tick'. The convert time to seconds
        dt = clock.tick(60)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sounds.play_background.stop()
                running = False
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sounds.play_background.stop()
                    running = False
                    return 1
                # reload ammo if it is necessary
                elif event.key == pygame.K_SPACE:
                    if ammo.count < 8:
                        ammo.update()

            # add new CHICKEN on the screen0
            elif event.type == pygame.USEREVENT:
                y1 = randint(50,500)
                chickens_group.add(Chicken(screen, y1))
                chickens_group.add(Chicken(screen, randint(50,500)))

            # checks if we have shot a CHICKEN
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # check for AMMO amount
                check_shot = ammo.shot()
                # if we shot the CHICKEN
                if cursor.shoot_chicken(sounds, chickens_group, check_shot, scores):
                    break
                # if we shot the PUMPKIN MAN
                elif cursor.shoot_pumpkin(sounds, pumpkin, check_shot, scores):
                    break


        buttons.draw_text('Imagine that you play a game here', 50, 450, 100)
        buttons.draw_text('(нажми esc чтобы вернуться в главное меню)', 20, 450, 200)

        # updates PUMPKIN state
        pumpkin.update()

        # updates CHICKEN/S state
        chickens_group.draw(screen)
        chickens_group.update(dt)

        # draw an image instead of REAL CURSOR
        cursor_group.draw(screen)
        cursor_group.update()



        # in purpose to make sure that we start counting only ones
        # when we start the play_loop
        init_time += 1
        if init_time == 1:
            start_time = time.time()
        play_time = round(time.time() - start_time)

        # shows LEFT PLAY TIME
        buttons.draw_text(f'{120 - play_time}', 30, 600, 20)

        # shows SCORE progress
        buttons.draw_text(f'{scores.score}', 20, 660, 20)

        # if the timer is got down to 0
        if play_time == 120:
            sounds.play_background.stop()
            running = False
            # go to BEST SCORE mode
            return 2

        pygame.display.flip()

