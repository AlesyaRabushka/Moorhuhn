import pygame

class Pumpkin(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()

        self.screen = screen

        self.alive = True
        self.image = pygame.image.load('img/pumpkin1.png')
        self.rect = self.image.get_rect(center=(200,500))

    # update current PUMPKIN state
    def update(self):
        if self.alive:
            self.screen.blit(self.image, self.rect)

        else:
            self.image = pygame.image.load('img/pumpkin9.png')
            self.screen.blit(self.image, self.rect)