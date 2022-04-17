import pygame
import os


class Sound():
    def __init__(self):
        self.button_click_sound = pygame.mixer.Sound('sounds/button_click.ogg')

        # MAIN MENU mode
        self.main_theme_sound = pygame.mixer.Sound('sounds/main_theme.ogg')

        # USER NAME mode
        self.type_sound = pygame.mixer.Sound('sounds/type_sound.wav')
        self.ready_after_user_name = pygame.mixer.Sound('sounds/game_start.ogg')

        # PLAY mode
        self.shot_sound = pygame.mixer.Sound('sounds/gun_shot_sound.ogg')
        self.play_background = pygame.mixer.Sound('sounds/ambientloop.ogg')
        # self.play_background = pygame.mixer.Sound('sounds/play_loop_birds_background.wav')