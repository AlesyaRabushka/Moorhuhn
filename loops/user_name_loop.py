from settings.buttons import *

def user_name_loop(screen, sounds):
    running = True
    user_name = ''
    box_width = True
    # turn off CURSOR
    pygame.mouse.set_visible(False)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # enter USER NAME
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # ready to go further SOUND
                    sounds.ready_after_user_name.play()
                    return True, user_name
                elif event.key == pygame.K_BACKSPACE:
                    # переписываем user_name от начала до предпоследнего символа
                    user_name = user_name[0:-1]
                else:
                    # если длина в пределах нормы
                    if box_width:
                        # type text SOUND
                        sounds.type_sound.play()
                        user_name += event.unicode

        screen.fill((254, 204, 153))
        b = Button(screen)
        b.draw_text("Enter User Name", 20, 200, 200)

        pygame.font.init()
        font = pygame.font.Font(None, 40)
        user_name_surf = font.render(user_name, True, (255, 255, 255))
        user_name_rect = pygame.Rect(200, 300, 400, 50)

        # для регулирования длины
        user_name_rect.w = max(200, user_name_surf.get_width() + 30)
        if user_name_rect.w >= 700:
            box_width = False
        pygame.draw.rect(screen, 'lightskyblue3', user_name_rect, 2)

        screen.blit(user_name_surf, (user_name_rect.x + 10, user_name_rect.y + 10))

        b.draw_text('Press ENTER to continue', 15, 200,400)
        pygame.display.flip()