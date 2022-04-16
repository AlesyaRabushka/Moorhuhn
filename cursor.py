import pygame

# CURSOR class
class Cursor(pygame.sprite.Sprite):
    def __init__(self, img_path):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()


    def update(self):
        self.rect.center = pygame.mouse.get_pos()