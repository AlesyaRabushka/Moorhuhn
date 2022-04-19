import pygame


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
        self.pumpkin_shot_sound = pygame.mixer.Sound('sounds/pumpkin_shot_sound.ogg')
        # self.play_background = pygame.mixer.Sound('sounds/play_loop_birds_background.wav')

        # CHICKEN hit sounds
        self.chick_hit1 = pygame.mixer.Sound('sounds/chick_hit1.ogg')
        self.chick_hit2 = pygame.mixer.Sound('sounds/chick_hit2.ogg')
        self.chick_hit3 = pygame.mixer.Sound('sounds/chick_hit3.ogg')
        self.chick_hits = []
        self.chick_hits.append(self.chick_hit1)
        self.chick_hits.append(self.chick_hit2)
        self.chick_hits.append(self.chick_hit3)

        # AMMO sounds
        self.empty_shot_sound = pygame.mixer.Sound('sounds/empty_shot_sound.ogg')
        self.update_ammo = pygame.mixer.Sound('sounds/update_ammo.ogg')


    # return CHICKEN HIT SOUND
    def return_chick_hits(self, sound):
        return self.chick_hits[sound]