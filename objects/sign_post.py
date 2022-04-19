import pygame

class SignPost(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen

        self.shot = False

        self.image = pygame.image.load('img/sign_post1.png')
        self.rect = self.image.get_rect(center=(500,500))

    def update(self):
        if not self.shot:
            self.image = pygame.image.load('img/sign_post1.png')
        else:
            self.image = pygame.image.load('img/sign_post2.png')

        self.screen.blit(self.image, self.rect)
