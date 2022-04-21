import sys
import time

import pygame

from settings.buttons import*
from settings.timer import Timer
from objects_imports import *


from random import randint
from objects.background import*

# PLAY mode
def play_loop(clock, screen, sounds, buttons, cursor, cursor_group, chickens_group, ammo, score_manager, scores_group, pumpkin, sign_post):
    # bg_w, bg_h = 2000,800
    # bg = (pygame.image.load('img/world/background1.png')
    # bg = pygame.transform.smoothscale(pygame.image.load('img/world/backgroundcombined.png'), (bg_w,bg_h))
    # bg_rect = bg.get_rect()
    # pos_x = 10
    # speed = 10
#Backgroundspeed
    # done = False
    # while not done:
    #     clock.tick(60)
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             done = True
    #
    #     allKeys = pygame.key.get_pressed()
    #     pos_x += speed if allKeys[pygame.K_LEFT] else -speed if allKeys[pygame.K_RIGHT] else 0
    #
    #     x_rel = pos_x % bg_w
    #     x_part2 = x_rel - bg_w if x_rel > 0 else x_rel + bg_w
    #
    #     screen.blit(bg,(x_rel,0))
    #     screen.blit(bg,(x_part2,0))

    # background SOUND
    sounds.play_background.play(-1)

    # to check that we are still playing
    running = True
    # to check last 10 sec of the PLAY
    timer = Timer()

    # turn off the image of the REAL 'CURSOR'
    pygame.mouse.set_visible(False)

    # initialize time value
    # to know if we have to start counting time
    init_time = 0

    big_chicken = None
    big_chick_timer = 0

    while running:
        screen.fill((0,0,255))
        screen.blit(bg1,background1)
        screen.blit(bg2, background2)

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
                # if we shot SIGN POST
                if cursor.shoot_big_chicken(sounds, big_chicken, check_shot, score_manager, scores_group):
                    continue
                elif cursor.shoot_sign_post(sounds, sign_post, check_shot, score_manager, scores_group):
                    continue
                # if we shot the CHICKEN
                elif cursor.shoot_chicken(sounds, chickens_group, check_shot, score_manager, scores_group):
                    break
                # if we shot the PUMPKIN MAN
                elif cursor.shoot_pumpkin(sounds, pumpkin, check_shot, score_manager, scores_group):
                    break

        buttons.draw_text('Imagine that you play a game here', 50, 450, 100)
        buttons.draw_text('(нажми esc чтобы вернуться в главное меню)', 20, 450, 200)

        # updates PUMPKIN state
        pumpkin.update()

        # updates CHICKEN/S state
        chickens_group.draw(screen)
        chickens_group.update(dt)

        # updates SIGN POST
        sign_post.update()

        # shows SCORE progress
        buttons.draw_text(f'Score: {score_manager.return_score()}', 30, 700, 20)

        # updates SCORE progress
        scores_group.update()

        # --------- BIG CHICKEN POP UPS ---------
        big_chick_timer += 1
        if big_chick_timer == 20:
            print('here new')
            sounds.big_chicken_pops_up_sound.play()
            big_chicken = BigChicken(screen)
            big_chicken.show = True
            print(big_chicken.alive)
            big_chicken.update()
        elif big_chick_timer > 20:
            big_chicken.update()


        # --------- COUNT PLAY TIME ---------
        # in purpose to make sure that we start counting only ones
        # when we start the play_loop
        init_time += 1
        if init_time == 1:
            start_time = time.time()
        play_time = round(time.time() - start_time)

        # shows LEFT PLAY TIME
        buttons.draw_text(f'Time: {90 - play_time}', 30, 82, 20)



        # --------- CHECK LEFT TIME ---------
        # if the timer is got down to 0
        play_time_check = timer.time_check(sounds, play_time)
        if play_time_check == 1:
            sounds.play_background.stop()
            sounds.game_over_sound.play()
            running = False
            # go to the BEST SCORE mode
            return 2

        # draw an image instead of REAL CURSOR
        cursor_group.draw(screen)
        cursor_group.update()

        pygame.display.flip()
