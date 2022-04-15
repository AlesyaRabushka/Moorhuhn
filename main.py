#from loop import *
import pygame, sys

#
# pygame.init()
# pygame.font.init()
# SCREEN_WIDTH = 1000
# SCREEN_HEIGHT = 700
# # create a window
# screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
# pygame.display.set_caption('Moorhuhn')
# game_font = pygame.font.SysFont('Comic Sans MS', 40)
# # hide the cursor
# pygame.mouse.set_visible(True)
#
#
#
#
# # START THE GAME
# # Game Variables
# game_state = 'intro'
# user_name = ''
#
#
# # START GAME
# while True:
#
#     # check events
#     for event in pygame.event.get():
#         # if we press on cross to close the window
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         elif event.type == pygame.KEYDOWN:
#             # if we press ESC in one of the windows
#             # it works and goes to start menu
#             if event.key == pygame.K_ESCAPE:
#                 game_state = 'start_menu'
#
#         # INTRO
#         elif game_state == 'intro':
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if event.button == 1:
#                     game_state = 'start_menu'
#
#         # START MENU
#         elif game_state == 'start_menu':
#             pass
#
#
#
#     # GAME MODE
#     screen.fill((0,100,0))
#
#     # INTRO
#     if game_state == 'intro':
#         welcome_text = game_font.render('Here you are!', True, (255,255,255))
#         press_text = game_font.render('Please!', True, (255, 255, 255))
#         screen.blit(welcome_text, welcome_text.get_rect(center = (SCREEN_WIDTH//3, SCREEN_HEIGHT//3)))
#         screen.blit(press_text, press_text.get_rect(center=(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)))
#
#         # fully updates the screen
#         pygame.display.flip()
#
#
#     # USER NAME
#     elif game_state == 'user_name':
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             input_active = True
#             user_name = ""
#         elif event.type == pygame.KEYDOWN and input_active:
#             if event.key == pygame.K_RETURN:
#                 input_active = False
#                 if user_name == "":
#                     user_name = "Unknown"
#                 # score_manager = ScoreManager(user_name)
#                 # cursor = Cursor(score_manager)
#                 cursor_group = pygame.sprite.Group()
#                 # cursor_group.add(cursor)
#                 game_state = "start_menu"
#             elif event.key == pygame.K_BACKSPACE:
#                 user_name = user_name[:-1]
#             else:
#                 user_name += event.unicode
#         pygame.display.flip()
#
#
#     # START MENU
#     elif game_state == 'start_menu':
#         welcome_text = game_font.render('Main menu!', True, (255, 255, 255))
#         screen.blit(welcome_text, welcome_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))
#
#         # button to start the game
#         start_button = pygame.Rect((SCREEN_WIDTH // 2) - 100, 100, 200, 50)
#         exit_button = pygame.Rect((SCREEN_WIDTH // 2) - 100, 200, 200, 50)
#
#         pygame.draw.rect(screen, (255, 255, 0), start_button)
#         pygame.draw.rect(screen, (255, 255, 0), exit_button)
#
#         mouse_position = pygame.mouse.get_pos()
#         # button to EXIT
#         # if exit_button.collidepoint(mouse_position):
#         #     if event.type == pygame.MOUSEBUTTONDOWN:
#         #         game_state = 'exit'
#
#         # button to enter user_name
#         elif start_button.collidepoint(mouse_position):
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 game_state = 'user_name'
#
#
#         pygame.display.update()
#
#     # EXIT
#     elif game_state == 'exit':
#         welcome_text = game_font.render('Are  you sure?', True, (255, 255, 255))
#         screen.blit(welcome_text, welcome_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))
#
#         # button to start the game
#         yes_button = pygame.Rect((SCREEN_WIDTH // 2) - 100, 100, 200, 50)
#         no_button = pygame.Rect((SCREEN_WIDTH // 2) - 100, 200, 200, 50)
#
#         mouse_position = pygame.mouse.get_pos()
#         if yes_button.collidepoint(mouse_position):
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 pygame.quit()
#                 sys.exit()
#         elif no_button.collidepoint(mouse_position):
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 game_state = 'start_menu'
#
#         pygame.draw.rect(screen, (255, 255, 0), yes_button)
#         pygame.draw.rect(screen, (255, 255, 0), no_button)
#         pygame.display.update()
#
#
# pygame.quit()


from states import*

# MAIN GAME
game = Game()

if __name__ == '__main__':
    print('START GAME')
    game.start_game()


