import pygame
from loop_imports import *
from buttons import *
from chicken import Chicken
from cursor import Cursor
from random import randint

pygame.init()
HEIGHT = 600
WIDTH = 900

# the SCREEN of the GAME
screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.time.set_timer(pygame.USEREVENT, 1000)

# all buttons
buttons = Button(screen)

# all chickens
chickens_group = pygame.sprite.Group()
#chickens = Chicken(screen)
chickens_group.add(Chicken(screen, randint(10, 500)))



# CURSOR
cursor = Cursor('img/cursor.png')
cursor_group = pygame.sprite.Group()
cursor_group.add(cursor)


class State:
    # -> MAIN MENU
    def back_to_intro_mode(self):
        # is raised when it is not overrided in Child class
        raise NotImplementedError

    # enter mode
    def enter_new_screen(self):
        raise NotImplementedError

    # -> PLAY
    def play_game_mode(self):
        raise NotImplementedError

    # -> BEST SCORE
    def best_game_mode(self):
        raise NotImplementedError
    # -> HELP INFO mode
    def help_game_mode(self):
        raise NotImplementedError
    # -> EXIT mode
    def exit_game_mode(self):
        raise NotImplementedError


# the main GAME class
class Game:
    def __init__(self):
        # the first screen of the GAME
        # is INTRO (MainMenu)
        self.game_state = UserNameState(game = self)

    # the method that STARTS the GAME
    # -> MainMenu
    def start_game(self):
        self.game_state.enter_new_screen()

    # changes the game state
    def change_game_state(self, new_state: State):
        if self.game_state == None:
            pass
        self.game_state = new_state
        self.game_state.enter_new_screen()

    # -> PLAY mode
    def play_game_mode(self):
        self.game_state.play_game_mode()

    # -> BEST mode
    def best_game_mode(self):
        self.game_state.best_game_mode()

    # -> HELP INFO mode
    def help_game_mode(self):
        self.game_state.help_game_mode()

    def exit_game_mode(self):
        self.game_state.exit_game_mode()


# USER NAME
class UserNameState(State):
    def __init__(self, game):
        self.game = game

    def enter_new_screen(self):
        check, user_name = user_name_loop(screen)
        if check:
            print(user_name)
            self.game.change_game_state(MainMenuState(self.game))


    def back_to_intro_mode(self):
        pass
    def play_game_mode(self):
        pass
    def best_game_mode(self):
        pass
    def help_game_mode(self):
        pass
    def exit_game_mode(self):
        pass

# MAIN MENU mod
class MainMenuState(State):
    def __init__(self, game):
        self.game = game

    # we are already here
    def enter_new_screen(self):
        pygame.display.set_caption("MAIN MENU")

        # choose the next mode in MAIN MENU
        chosen_screen = choose_loop(screen, buttons)
        if chosen_screen == 1:
            self.game.play_game_mode()
        elif chosen_screen == 2:
            self.game.best_game_mode()
        elif chosen_screen == 3:
            self.game.help_game_mode()
        elif chosen_screen == 4:
            self.game.exit_game_mode()


    # we are already here
    def back_to_intro_mode(self):
        pygame.display.set_caption("MAIN MENU")
        print('we are on start screen')
        # choose the next mode in MAIN MENU
        chosen_screen = choose_loop(screen, buttons)
        if chosen_screen == 1:
            print('we are supposed to change it')
            self.game.play_game_mode()
        elif chosen_screen == 2:
            self.game.best_game_mode()
        elif chosen_screen == 3:
            self.game.help_game_mode()

    # -> PLAY mode
    def play_game_mode(self):
        self.game.change_game_state(PlayState(self.game))

    # -> BEST SCORE mode
    def best_game_mode(self):
        self.game.change_game_state(BestScoreState(self.game))

    # -> HELP INFO mode
    def help_game_mode(self):
        self.game.change_game_state(HelpState(self.game))

    def exit_game_mode(self):
        self.game.change_game_state(ExitState(self.game))


# PLAY GAME class
class PlayState(State):
    def __init__(self, game):
        self.game = game

    # -> MainMenu mode
    def back_to_intro_mode(self):
        self.game.change_game_state(MainMenuState(game = self.game))

    # enter current mode
    def enter_new_screen(self):
        pygame.display.set_caption('PLAY')
        print('we are in PLAY mode')
        check = play_loop(screen, buttons, cursor, cursor_group, chickens_group)
        if check == 1:
            self.game.change_game_state(PauseState(self.game))

    # we are already in here
    def play_game_mode(self):
        pass

    # -> BEST SCORE mode
    def best_game_mode(self):
        self.game.change_game_state(BestScoreState(self.game))

    # -> HELP INFO mode
    def help_game_mode(self):
        self.game.change_game_state(HelpState(self.game))

    def exit_game_mode(self):
        self.game.change_game_state(ExitState(self.game))


# PAUSE on PLAY mode
class PauseState(State):
    def __init__(self, game):
        self.game = game

    # -> MainMenu mode
    def back_to_intro_mode(self):
        self.game.change_game_state(MainMenuState(game=self.game))

    # enter current mode
    def enter_new_screen(self):
        pygame.display.set_caption('PAUSE')
        check = pause_loop(screen, buttons, cursor_group)
        if check == 1:
            pass
        elif check == 2:
            self.game.change_game_state(MainMenuState(self.game))

    # we are already in here
    def play_game_mode(self):
        pass

    # -> BEST SCORE mode
    def best_game_mode(self):
        self.game.change_game_state(BestScoreState(self.game))

        # -> HELP INFO mode

    def help_game_mode(self):
        self.game.change_game_state(HelpState(self.game))

    def exit_game_mode(self):
        self.game.change_game_state(ExitState(self.game))

# BEST SCORE table
class BestScoreState(State):
    def __init__(self, game):
        self.game = game

    # -> MAIN MEU mode
    def back_to_intro_mode(self):
        self.game.change_game_state(MainMenuState(self.game))

    # best score table
    def enter_new_screen(self):
        pygame.display.set_caption('BEST SCORE TABLE')
        new_state = best_score_loop(screen, buttons)
        if new_state:
            self.game.change_game_state(MainMenuState(self.game))

    # -> PLAY mode
    def play_game_mode(self):
        self.game.change_game_state(PlayState(self.game))

    # we are already here
    def best_game_mode(self):
        pass

    # -> HELP INFO mode
    def help_game_mode(self):
        self.game.change_game_state(HelpState(self.game))

    def exit_game_mode(self):
        self.game.change_game_state(ExitState(self.game))


# HELP INFO
class HelpState(State):
    def __init__(self, game):
        self.game = game

    # -> MAIN MENU mode
    def back_to_intro_mode(self):
        self.game.change_game_state(MainMenuState(self.game))

    # we are already here
    def enter_new_screen(self):
        pygame.display.set_caption('HELP INFORMATION')
        check = help_loop(screen, buttons)
        # back into MAIN MENU mode
        if check:
            self.game.change_game_state(MainMenuState(self.game))


    # -> PLAY mode
    def play_game_mode(self):
        self.game.change_game_state(PlayState(self.game))

    # -> BEST SCORE mode
    def best_game_mode(self):
        self.game.change_game_state(BestScoreState(self.game))

    # we are already here
    def help_game_mode(self):
        pass
    def exit_game_mode(self):
        self.game.change_game_state(ExitState(self.game))


# EXIT
class ExitState(State):
    def __init__(self, game):
        self.game = game

    # -> Main Menu
    def back_to_intro_mode(self):
        self.game.change_game_state(MainMenuState(self.game))

    # we work here
    def enter_new_screen(self):
        pygame.display.set_caption('EXIT')
        check = exit_loop(screen, buttons)
        if check == 1:
            pygame.quit()
        elif check == 2:
            self.game.change_game_state(MainMenuState(self.game))
        elif check == 0:
            self.game.change_game_state(MainMenuState(self.game))


    def play_game_mode(self):
        pass
    def best_game_mode(self):
        pass
    def help_game_mode(self):
        pass
    def exit_game_mode(self):
        pass