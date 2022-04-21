import pygame
from loops import play_loop
import os

from loops.play_loop import *

class BackgroundTree(pygame.sprite.Sprite):
    def __init__(self,bg,location):
        pygame.sprite.Sprite.__init__(self)
        #bg = pygame.image.load("backgroundcombined.png")
        self.image = bg
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Speed(pygame.sprite.Sprite):
    def __init__(self,bg,location):
        pygame.sprite.Sprite.__init__(self)
        self.image = bg
        self.rect = self.image.get_rect()
        self.rect.center = location

bg1 = pygame.image.load('img/world/background1.png')
background1 = BackgroundTree(bg1,[0,185])
pos_x = 10

bg2 = pygame.image.load('img/world/background2.png')
background2 = BackgroundTree(bg2, [0,145])
pos_x = 10

# bg = pygame.image.load('img/world/background1.png')
# background3 = BackgroundTree(bg, [0,50])

# bgStartGame = ((pygame.image.load('img/background/backgroundworls.png')))
# startGameBG = Speed(bgStartGame,[WIDTH * 0,5, HEIGHT * 0,5])
#
# bgEndGame = ((pygame.image.load('img/background/backgroundtarget1.png')))
# endGameBG = Speed(bgEndGame,[WIDTH * 0,5, HEIGHT * 0,5])
#
# bgBestList = ((pygame.image.load('img/background/backgroundtarget2.png')))
# bestListBG = Speed(bgBestList,[WINTH * 0,5, HEIGHT * 0,5])
#
# bgHelpGame = ((pygame.image.load('img/background/background3.png')))
# helpGameBG = Speed(bgListGame,[WINTH * 0,5, HEIGHT * 0,5])




