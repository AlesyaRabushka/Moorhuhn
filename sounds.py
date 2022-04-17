import pygame
import os


class Sound():
    def __init__(self):
        self.shot_sound = pygame.mixer.Sound('sounds/gun_shot_sound.ogg')
        #self.main_menu_sound = pygame.mixer.Sound(os.path.join())
        self.play_background = pygame.mixer.Sound('sounds/ambientloop.ogg')
        #self.play_background = pygame.mixer.Sound('sounds/play_loop_birds_background.wav')