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

    # shot the CHICKEN
    def shoot_chicken(self, sounds, chickens_group, check_shot, scores):
        for chicken in chickens_group:
            # looking for a shot chicken
            if self.rect.colliderect(chicken.rect) and chicken.alive:
                if check_shot:
                    # add random SHOT CHICKEN SOUND
                    index = random.randint(0, 2)
                    sounds.return_chick_hits(index).play()

                    # update SCORE
                    scores.update(chicken)

                    # CHICKEN is DEAD
                    chicken.alive = False
                    # break
                    return True

    # shot the PUMPKIN MAN
    def shoot_pumpkin(self, sounds, pumpkin, check_shot, scores):
        # looking for a shot chicken
        if self.rect.colliderect(pumpkin.rect) and pumpkin.alive:
            if check_shot:
                sounds.pumpkin_shot_sound.play()


                # update SCORE
                scores.update(pumpkin)

                # CHICKEN is DEAD
                pumpkin.alive = False

                # break
                return True