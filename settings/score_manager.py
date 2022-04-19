import pygame
from objects.pumpkin import Pumpkin
from objects.chicken import Chicken

class ScoreManager():
    def __init__(self):
        self.score = 0

    def update(self, shot_object):
        if isinstance(shot_object, Chicken):
            if shot_object.size == shot_object.all_size[0]:
                self.score += 20
            elif shot_object.size == shot_object.all_size[1]:
                self.score += 15
            elif shot_object.size == shot_object.all_size[2]:
                self.score += 10
        elif isinstance(shot_object, Pumpkin):
            self.score += 15