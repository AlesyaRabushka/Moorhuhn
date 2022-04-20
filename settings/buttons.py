import pygame
pygame.font.init()
# class to draw buttons
class Button:
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.main_menu_buttons = []
        self.pause_buttons = []
        self.best_score_buttons = []
        self.help_buttons = []
        self.exit_buttons = []

    def add_main_menu(self, button):
        self.main_menu_buttons.append(button)

    # draw text on screen
    def draw_text(self, text,size, pos_x, pos_y):

        font = pygame.font.SysFont('Comic Sans MS', size)
        button_text = font.render(text, True, (0,1,1))
        button_rect = button_text.get_rect()
        button_rect.center = (pos_x, pos_y)

        self.screen.blit(button_text, button_rect)

    # MAIN MENU buttons
    def draw_main_menu(self, text, size, pos_x, pos_y):
        font = pygame.font.Font('fonts/Roose_Sally.otf', size)

        button_text = font.render(text, True, (0, 255, 255), (255, 255, 255))
        button_rect = button_text.get_rect()
        button_rect.center = (pos_x, pos_y)

        self.main_menu_buttons.append(button_rect)
        self.screen.blit(button_text, button_rect)

    # PAUSE mode buttons
    def draw_pause(self, text, size, pos_x, pos_y):
        font = pygame.font.SysFont('Comic Sans MS', size)
        button_text = font.render(text, True, (0, 1, 1))
        button_rect = button_text.get_rect()
        button_rect.center = (pos_x, pos_y)

        self.pause_buttons.append(button_rect)
        self.screen.blit(button_text, button_rect)

    # BEST SCORE mode buttons
    def draw_best_score(self, text, size, pos_x, pos_y):
        font = pygame.font.SysFont('Comic Sans MS', size)
        button_text = font.render(text, True, (0, 1, 1))
        button_rect = button_text.get_rect()
        button_rect.center = (pos_x, pos_y)

        self.best_score_buttons.append(button_rect)
        self.screen.blit(button_text, button_rect)


    # HELP mode buttons
    def draw_help(self, text, size, pos_x, pos_y):
        font = pygame.font.SysFont('Comic Sans MS', size)
        button_text = font.render(text, True, (0, 1, 1))
        button_rect = button_text.get_rect()
        button_rect.center = (pos_x, pos_y)

        self.help_buttons.append(button_rect)
        self.screen.blit(button_text, button_rect)

    # EXIT mode buttons
    def draw_exit(self, text, size, pos_x, pos_y):
        font = pygame.font.SysFont('Comic Sans MS', size)
        button_text = font.render(text, True, (0, 1, 1))
        button_rect = button_text.get_rect()
        button_rect.center = (pos_x, pos_y)

        self.exit_buttons.append(button_rect)
        self.screen.blit(button_text, button_rect)


class MainMenuButtons(Button):
    def __init__(self):
        super().__init__()
        self.start_img = pygame.image.load('img/startnormal.gif')
        self.start_rect = self.start_img.get_rect()
        super().add_main_menu(self)