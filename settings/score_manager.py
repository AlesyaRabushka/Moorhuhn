import time

import pygame
from objects_imports import *

class ScoreImgManager(pygame.sprite.Sprite):
    def __init__(self, screen, score_manager):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.score = 0
        self.score_manager = score_manager
        self.font = pygame.font.Font('fonts/AA_Magnum.ttf', 50)
        #print(pygame.font.get_fonts())

        self.show = False
        self.max_show_y = 25
        self.current_score = 0

        # SCORE show TIMER
        self.max_show_time = 3
        self.show_time = 0

        # self.img1_path = 'img/' + self.firsrt_number
        # self.img2_path = 'img/' + self.second_number
        self.img_path = 'img/figures/20.jpg'

        #self.image = pygame.transform.scale(pygame.image.load(self.img_path).convert_alpha(), (40,40))
        #self.image = pygame.image.load(self.img_path)

        self.image = self.font.render('0', True, (255,255,255,255))
        self.rect = self.image.get_rect()
        #self.image.set_colorkey((0, 0, 0))


    # update SCORE progress
    def shot(self, shot_object):
        if isinstance(shot_object, Chicken):
            if shot_object.size == shot_object.all_size[0]:
                self.score += 20
                self.score_manager.update_score('+',20)

                self.show = True
                self.draw_score(str(20), shot_object)
                #self.draw_score(20, shot_object)

            elif shot_object.size == shot_object.all_size[1]:
                self.score += 15
                self.score_manager.update_score('+', 15)

                self.show = True
                self.draw_score(str(15), shot_object)
                #self.draw_score(15, shot_object)
            elif shot_object.size == shot_object.all_size[2]:
                self.score += 10
                self.score_manager.update_score('+', 10)

                self.show = True
                self.draw_score(str(10), shot_object)
                #self.draw_score(10, shot_object)

        elif isinstance(shot_object, Pumpkin):
            self.score += 15
            self.score_manager.update_score('+', 15)

            self.show = True
            self.draw_score(str(15), shot_object)

        elif isinstance(shot_object, SignPost):
            # self.score -= 15
            self.score_manager.update_score('-', 15)

            self.show = True
            self.draw_score(str(-15), shot_object)
            #self.draw_score()

    # show SCORES on the screen after shooting
    def draw_score(self, new_score, shot_object):

        self.image = self.font.render(new_score, True, (255,255,255))
        self.rect = self.image.get_rect(center=(shot_object.rect.x, shot_object.rect.y))
        #self.image.set_colorkey((0,0,0))

        self.current_score = new_score
        # new_path = 'img/figures'+new_score+'.png'


    def update(self):
        # if we want to see it on the screen
        if self.show:
            self.show_time += 1
            self.screen.blit(self.image, self.rect)
            if self.show_time == self.max_show_time:
                self.max_show_y -= 5
                self.rect.y -= 5

                if self.max_show_y == 0:
                    self.show = False
                    self.kill()
                else:
                    self.show_time = 0


    # draw text on screen
    def draw_text(self, text, size, pos_x, pos_y):
        font = pygame.font.SysFont('Comic Sans MS', size)
        button_text = font.render(text, True, (0, 1, 1))
        button_rect = button_text.get_rect()
        button_rect.center = (pos_x, pos_y)

        self.screen.blit(button_text, button_rect)


class ScoreManager:
    """
    Class to show current SCORE progress
    """
    def __init__(self, screen):
        self.screen = screen
        self.score = 0

    # add new scores
    def update_score(self, sign, new_score):
        if sign == '+':
            self.score += new_score
        elif sign == '-':
            self.score -= new_score

    # return current score
    def return_score(self):
        return int(self.score)