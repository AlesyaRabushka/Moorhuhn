import pygame

class Chicken(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Chicken, self).__init__()
        self.screen = screen
        self.chickens = []

        self.image = pygame.image.load('img/hen_left.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    # show chicken on the screen
    def draw_chicken(self):
        self.chickens.append(self.rect)
        self.screen.blit(self.image, self.rect)

    # logic of flight
    def fly_chicken(self):
        #self.x += 1
        self.rect.y += 10

    def update(self):
        self.x += 1
        self.rect.x += 1

    # def kill_chicken(self):
    #     pygame.sprite.spritecollide(pygame.mouse.get_pos(), chicken, True)