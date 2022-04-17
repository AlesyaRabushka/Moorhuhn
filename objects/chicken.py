import pygame
import random



class Chicken(pygame.sprite.Sprite):
    def __init__(self, screen, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.chickens = []

        # if CHICKEN is still alive
        self.alive = True


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
        self.image = pygame.image.load(self.img_path)
        self.rect = self.image.get_rect(center=(r,pos_y))


    # logic of flight
    def update(self):
        # if CHICKEN is alive
        if self.alive:

            # self.chickens.append(self.rect)
            self.screen.blit(self.image, self.rect)
            if self.direction == 1:
                self.rect.x += 1
            else:
                self.rect.x -= 1

            # if the chicken is out of the screen
            if self.rect.y >= 540:
                self.kill()
            elif self.rect.x >= 901:
                self.kill()
            if  self.rect.x <= -40:
                self.kill()


        # if we have shot one of them
        if not self.alive:
            #self.y += 2
            #self.image = pygame.image.load('img/chickendead1.png')
            self.image = pygame.image.load('../img/chickendead3.png')
            self.rect.y += 2

            # delete CHICKEN  if it is out of the screen
            if self.rect.y >= 500:
                self.kill()
            elif self.rect.x >= 901 or self.rect.x <= 0:
                self.kill()

    # def kill_chicken(self):
    #     pygame.sprite.spritecollide(pygame.mouse.get_pos(), chicken, True)