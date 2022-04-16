import pygame

class Chicken(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Chicken, self).__init__()
        self.screen = screen
        self.chickens = []

        self.chicken = pygame.image.load('img/hen_left.png')
        self.chicken_rect = self.chicken.get_rect()
        self.chicken_rect.x = self.chicken_rect.width
        self.chicken_rect.y = self.chicken_rect.height
        self.x = float(self.chicken_rect.x)
        self.y = float(self.chicken_rect.y)

    # show chicken on the screen
    def draw_chicken(self):
        self.chickens.append(self.chicken_rect)
        self.screen.blit(self.chicken, self.chicken_rect)

    # logic of flight
    def fly_chicken(self):
        #self.x += 1
        self.chicken_rect.x += 1

    def update(self):
        # self.x += 1
        self.chicken_rect.x += 1

    # def kill_chicken(self):
    #     pygame.sprite.spritecollide(pygame.mouse.get_pos(), chicken, True)