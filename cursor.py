import pygame

# CURSOR class
class Cursor(pygame.sprite.Sprite):
    def __init__(self, img_path):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()

    # updates the position
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    # shoot the chicken
    def shoot(self, cursor, chicken):
        for ch in chicken:
            ch.alive = False
        #pygame.sprite.spritecollide(cursor, chicken, True)