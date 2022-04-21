import pygame


#  AMMO class
class Ammo(pygame.sprite.Sprite):
    """
    Class is used to hold AMMO count
    """
    def __init__(self, sounds):
        pygame.sprite.Sprite.__init__(self)
        self.sounds = sounds
        self.count = 8
        #self.shot = False

    def update(self):
        self.sounds.update_ammo.play()
        self.count = 8
        return 8

    # change the AMMO amount
    def shot(self):
        if self.count == 0:
            # add EMPTY SHOT SOUND
            self.sounds.empty_shot_sound.play()
            return False, 9
        else:
            self.count -= 1
            # add SHOT SOUND
            self.sounds.shot_sound.play()
            return True, self.count




# AMMO class
class AmmoGroup(pygame.sprite.Sprite):
    """
    Class is used to show AMMO on the screen
    """
    def __init__(self, screen, index):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.index = index

        self.count = 8
        self.show = True

        self.img_index = 1
        self.path = 'img/ammo/Ammo' + str(self.img_index) + '.png'
        self.image = pygame.transform.scale(pygame.image.load(self.path), (50,80))
        self.rect = self.image.get_rect(center=(500+self.index*30, 500))
        #self.rect = None


    def update(self, index):
        if index == 8:
            self.show = True
        elif index == 9:
            self.show = False
        elif 7 - self.index == index:
            self.show = False
        if self.show:
            self.screen.blit(self.image, self.rect)
        # for i in range(0, self.count):
        #     if i == 7:
        #         self.rect = self.image.get_rect(center=(500 + self.index * 10, 500))
        #         self.screen.blit(self.image, self.rect)
        #         self.stop = True
        #     else:
        #         self.rect = self.image.get_rect(center=(500+self.index*10, 500))
        #         self.screen.blit(self.image, self.rect)

    def kill(self, index):
        if self.index == index:
            self.show = False