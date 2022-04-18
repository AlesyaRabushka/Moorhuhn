import pygame

class ScoreManager():
    def __init__(self):
        self.score = 0

    def update(self, shot_object):
        if shot_object == 'chicken':
            self.score += 20
        elif shot_object == 'pumpkin':
            self.score += 15