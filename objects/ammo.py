import pygame


#  AMMO class
class Ammo(pygame.sprite.Sprite):
    def __init__(self, sounds):
        pygame.sprite.Sprite.__init__(self)
        self.sounds = sounds
        self.count = 8
        #self.shot = False

    def update(self):
        self.sounds.update_ammo.play()
        self.count = 8

    # change the AMMO amount
    def shot(self):
        if self.count == 0:
            # add EMPTY SHOT SOUND
            self.sounds.empty_shot_sound.play()
            return False
        else:
            self.count -= 1
            # add SHOT SOUND
            self.sounds.shot_sound.play()
            return True

    # to show AMMO on the screen
    def draw_ammo(self):
        pass