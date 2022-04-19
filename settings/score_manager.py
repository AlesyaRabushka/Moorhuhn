import time

import pygame
from objects_imports import *

class ScoreManager():
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.show_time = True


    # update SCORE progress
    def shot(self, shot_object):
        if isinstance(shot_object, Chicken):
            if shot_object.size == shot_object.all_size[0]:
                self.score += 20
                #self.draw_score(20, shot_object)

            elif shot_object.size == shot_object.all_size[1]:
                self.score += 15
                #self.draw_score(15, shot_object)
            elif shot_object.size == shot_object.all_size[2]:
                self.score += 10
                #self.draw_score(10, shot_object)

        elif isinstance(shot_object, Pumpkin):
            self.score += 15
            #self.draw_score()

        elif isinstance(shot_object, SignPost):
            self.score -= 15
            #self.draw_score()

    # show SCORES on the screen after shooting
    def draw_score(self, score, shot_object):
        font = pygame.font.SysFont('Comic Sans MS', 20)
        button_text = font.render(score, True, (0, 1, 1))
        button_rect = button_text.get_rect()
        button_rect.center = (shot_object.rect.x, shot_object.rect.y)

        self.screen.blit(button_text, button_rect)

    def update(self):
        if self.show_time:
            pass

    # draw text on screen
    def draw_text(self, text, size, pos_x, pos_y):
        font = pygame.font.SysFont('Comic Sans MS', size)
        button_text = font.render(text, True, (0, 1, 1))
        button_rect = button_text.get_rect()
        button_rect.center = (pos_x, pos_y)

        self.screen.blit(button_text, button_rect)

    def update_time(self):
        if self.show_time != 0:
            self.show_time -= 1
            self.draw_score()
        else:
            pass