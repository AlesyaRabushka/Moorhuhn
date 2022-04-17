import pygame
import random

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
    def shoot(self, sounds, chickens_group, check_shot):
        for chicken in chickens_group:
            # looking for a shot chicken
            if self.rect.colliderect(chicken.rect) and chicken.alive:
                if check_shot:
                    # add SHOT CHICKEN SOUND
                    index = random.randint(0, 2)
                    sounds.return_chick_hits(index).play()
                    # CHICKEN is DEAD
                    chicken.alive = False
