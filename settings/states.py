import pygame.sprite
from random import randint

from loop_imports import *
from objects_imports import *
from settings_imports import*

pygame.init()
HEIGHT = 600
WIDTH = 800

# the SCREEN of the GAME
screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.time.set_timer(pygame.USEREVENT, 4000)


# BUTTONS
buttons = Button(screen)

main_buttons = pygame.sprite.Group()
for i in range(0, 4):
    main_buttons.add(MainMenuButtons(screen, i))

# CHICKEN
chickens_small_group = pygame.sprite.Group()
chickens_small_group.add(ChickenSmall(screen, randint(100, 200)))
chickens_mid_group = pygame.sprite.Group()
chickens_mid_group.add(ChickenMiddle(screen, randint(100,300)))
chickens_big_group = pygame.sprite.Group()
chickens_big_group.add(ChickenBig(screen, randint(100,500)))

# BIG CHICKEN
big_chicken_group = pygame.sprite.Group()

# SOUNDS
sounds = Sound()

# SCORE
scores_group = pygame.sprite.Group()
score_manager = ScoreManager(screen)
scores_group.add(ScoreImgManager(screen, score_manager))

#scores_group = ScoreManager(screen)

# CHICKEN HOLE
chicken_hole = ChickenHole(screen)

# HOLE
holes = pygame.sprite.Group()
holes.add(Holes(screen, 0))

# MILL CHICKEN
mill = pygame.sprite.Group()
for i in range(0,4):
    mill.add(MillChicken(screen, i))

# AMMO
ammo = Ammo(sounds)
ammo_group = pygame.sprite.Group()
for i in range(0, 8):
    ammo_group.add(AmmoGroup(screen, i))

# PUMPKIN MAN
pumpkin = Pumpkin(screen)

# SIGN POST
sign_post = SignPost(screen)

# CURSOR
cursor = Cursor(screen, 'img/cursor/cursor.png')
cursor_group = pygame.sprite.Group()
cursor_group.add(cursor)

# CLOCK
clock = pygame.time.Clock()

def set_user_name(name):
    USER_NAME = name


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
        self.game_state = MainMenuState(game = self)

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
        check, user_name = user_name_loop(screen, sounds)
        global USER_NAME
        USER_NAME = user_name

        if check:
            print('user name: ', user_name)
            self.game.change_game_state(PlayState(self.game))
        if not check:
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
        chosen_screen = main_menu_loop(screen, sounds, cursor, cursor_group, main_buttons, buttons, chicken_hole, holes)
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
        # choose the next mode in MAIN MENU
        chosen_screen = main_menu_loop(screen, sounds, cursor_group, buttons)
        if chosen_screen == 1:
            self.game.play_game_mode()
        elif chosen_screen == 2:
            self.game.best_game_mode()
        elif chosen_screen == 3:
            self.game.help_game_mode()

    # -> PLAY mode
    def play_game_mode(self):
        self.game.change_game_state(UserNameState(self.game))

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
        check, score = play_loop(clock, screen, sounds, buttons, cursor, cursor_group, chickens_small_group, chickens_mid_group, chickens_big_group, ammo, ammo_group, score_manager, scores_group, pumpkin, sign_post, big_chicken_group, mill)
        global SCORE
        SCORE = score

        if check == 1:
            self.game.change_game_state(PauseState(self.game))
        elif check == 2:
            self.game.change_game_state(BestScoreState(self.game))

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
        check = pause_loop(screen, sounds, buttons, cursor_group)
        if check == 1:
            # go back to MAIN MENU mode
            self.game.change_game_state(MainMenuState(self.game))
        elif check == 2:
            # go to EXIT mode
            self.game.change_game_state(ExitState(self.game))

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
        new_state = best_score_loop(screen, sounds, cursor_group, buttons, USER_NAME, SCORE)
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
        check = help_loop(screen, sounds, cursor_group, buttons)
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
        check = exit_loop(screen, sounds, cursor_group, buttons)
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