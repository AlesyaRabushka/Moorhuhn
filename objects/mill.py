import pygame

class Mill(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)

        self.screen = screen


class MillChicken(pygame.sprite.Sprite):
    def __init__(self, screen, index):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen

        self.alive = True

        self.max_time = 5
        self.current_time = 0

        self.img_index_list = [28, 1, 10, 19]
        self.index = index

        self.pos_list_x = [240, 240, 240, 240]
        self.pos_list_y = [250, 250, 250, 250]

        self.path = 'img/mill/chickenmill' + str(self.img_index_list[index]) + '.png'
        self.image = pygame.transform.scale(pygame.image.load(self.path), (80,80))
        self.rect = self.image.get_rect(bottomleft=(self.pos_list_x[index],self.pos_list_y[index]))
        self.img_mask = pygame.mask.from_surface(self.image)

    def update(self):
        if self.alive:
            self.screen.blit(self.image, self.rect)

        if not self.alive:
            self.kill()

    # check the CURSOR position
    def check_shot(self, cursor, x, y):
        cursor_mask = pygame.mask.from_surface(cursor.image)
        offset = (x - self.rect.x, y - self.rect.y)
        result = self.img_mask.overlap(cursor_mask, offset)
        if result:
            print('yes')
            return True
        else:
            return False