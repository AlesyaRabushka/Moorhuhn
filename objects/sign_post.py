import pygame

class SignPost(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen

        self.shot = False

        self.image = pygame.transform.scale(pygame.image.load('img/sign_post/sign_post1.png'),(100,200))
        self.rect = self.image.get_rect(center=(500,500))

    def update(self):
        if not self.shot:
            self.image = pygame.transform.scale(pygame.image.load('img/sign_post/sign_post1.png'),(100,200))
        else:
            self.image = pygame.transform.scale(pygame.image.load('img/sign_post/sign_post2.png'),(100,200))

        self.screen.blit(self.image, self.rect)
