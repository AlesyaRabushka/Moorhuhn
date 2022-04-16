import pygame
import random



class Chicken(pygame.sprite.Sprite):
    def __init__(self, screen, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.chickens = []

        self.alive = True

        self.direction = 0
        self.img_path = None
        r = random.choice([0,900])
        if r == 0:
            self.direction = 1
            self.img_path = 'img/hen_left.png'
        else:
            self.direction = -1
            self.img_path = 'img/hen_right.png'


        self.image = pygame.image.load(self.img_path)
        self.rect = self.image.get_rect(center=(r,pos_y))
        # self.rect.x = self.rect.width
        # self.rect.y = self.rect.height
        #self.x = float(self.rect.x)
        #self.y = float(self.rect.y)

    # show chicken on the screen
    # def draw_chicken(self):
    #     self.chickens.append(self.rect)
    #     self.screen.blit(self.image, self.rect)

    # logic of flight
    def fly_chicken(self):
        #self.x += 1
        self.rect.y += 1
        #self.rect.move_ip(self.x, self.y)

    def update(self):
        if self.alive:
            # self.chickens.append(self.rect)
            self.screen.blit(self.image, self.rect)
            #self.x += 1
            if self.direction == 1:
                self.rect.x += 1
            else:
                self.rect.x -= 1



        if not self.alive:
            #self.y += 2
            #self.image = pygame.image.load('img/chickendead1.png')
            self.image = pygame.image.load('img/chickendead3.png')
            self.rect.y += 2
            if self.rect.y >= 500:
                self.kill()

    # def kill_chicken(self):
    #     pygame.sprite.spritecollide(pygame.mouse.get_pos(), chicken, True)