import pygame
from loops import play_loop
import os

from loops.play_loop import *
# from settings.buttons import*
# from objects.holes import Holes
from settings.states import *

# drag = 0
pygame.init()

class cam:
    def __init__(self,x,y):
        self.rect = pygame.Rect(x, y, 800, 600)

    def move(self, x):
        print(x)

        # self.rect[0] += vector[0]
        # self.rect[1] += vector[1]
        if self.rect[0] == 1900:
            if x < 0:
                self.rect[0] += x
            else:
                self.rect[0] += 0
        elif self.rect[0] == 0:
            if x > 0:
                self.rect[0] += x
            else:
                self.rect[0] += 0
        else:
            print(self.rect[0])
            self.rect[0] += x


class BackgroundTree(pygame.sprite.Sprite):
    def __init__(self,bg,location):
        pygame.sprite.Sprite.__init__(self)
        self.image = bg
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


sky = pygame.image.load('img/world/sky.png')
bg1 = pygame.transform.scale(sky, (4000, 500))
background1 = BackgroundTree(bg1, [0,0])
# pos_x = 10

castle = pygame.image.load('img/world/background1.png')
bg2 = pygame.transform.scale(castle, (2120, 500))
background2 = BackgroundTree(castle,[0,150])
# pos_x = 10

green = pygame.image.load('img/world/background2.png')
background3 = BackgroundTree(green, [0,145])
# # pos_x = 10





