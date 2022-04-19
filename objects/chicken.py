import time

import pygame
import random
import os


class Chicken(pygame.sprite.Sprite):
    def __init__(self, screen, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.chickens = []

        # if CHICKEN is still alive
        self.alive = True

        # POSITION and TIMER  of chicken's DEATH
        self.dead_index = 0
        self.max_dead_time = 3
        self.dead_time = 0

        # CHICKEN size
        self.all_size = [(40,40), (60,60), (80,80)]
        self.size = self.all_size[random.randint(0, 2)]

        # choose CHICKEN SPEED
        if self.size == self.all_size[0]:
            self.speed = 0.1
        elif self.size == self.all_size[1]:
            self.speed = 0.15
        elif self.size == self.all_size[2]:
            self.speed = 0.2

        # direction of CHICKEN flight
        self.direction = 0
        self.img_path = None
        r = random.choice([0,900])
        if r == 0:
            self.direction = 1
            self.img_path = 'img/hen_left.png'
        else:
            self.direction = -1
            self.img_path = 'img/hen_right.png'


        self.image = pygame.transform.scale(pygame.image.load(self.img_path).convert_alpha(), self.size)
        self.rect = self.image.get_rect(center=(r,pos_y))


    # logic of flight
    def update(self, dt):
        # if CHICKEN is alive
        if self.alive:

            # self.chickens.append(self.rect)
            self.screen.blit(self.image, self.rect)

            # flight to the RIGHT
            if self.direction == 1:
                self.rect.x += float(self.speed * dt)

            # flight to the LEFT
            else:
                self.rect.x -= float(self.speed * dt)

            # if the chicken is out of the screen
            if self.rect.y >= 540:
                self.kill()
            elif self.rect.x >= 901:
                self.kill()
            if  self.rect.x <= -40:
                self.kill()


        # if we have shot one of them
        if not self.alive:
            self.dead_time += 1
            self.rect.y += float(self.speed * dt)


            if self.dead_time == self.max_dead_time:
                self.dead_time = 0
                self.dead_index += 1
                if self.dead_index == 9:
                    self.kill()
                elif self.dead_index <= 8:
                    path = 'img/chickendead' + str(self.dead_index) + '.png'
                    self.image = pygame.transform.scale(pygame.image.load(path).convert_alpha(), self.size)
                    #self.rect.y += 2


            # delete CHICKEN  if it is out of the screen
            if self.rect.y >= 500:
                self.kill()
            elif self.rect.x >= 901 or self.rect.x <= 0:
                self.kill()

    # def kill_chicken(self):
    #     pygame.sprite.spritecollide(pygame.mouse.get_pos(), chicken, True)