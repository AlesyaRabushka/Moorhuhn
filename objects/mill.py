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
        self.animation_index = self.img_index_list[index]
        self.pos_list_x = [240, 241, 242, 243]
        self.pos_list_y = [250, 252, 250, 248]

        self.path = 'img/mill/chickenwindmil' + str(self.img_index_list[index]) + '.png'
        self.image = pygame.transform.scale(pygame.image.load(self.path), (100,100))
        self.rect = self.image.get_rect(bottomleft=(self.pos_list_x[index],self.pos_list_y[index]))
        self.img_mask = pygame.mask.from_surface(self.image)

        self.bottom_left = self.rect.bottomleft
        print(self.rect.bottomleft)

    def update(self):
        if self.alive:
            self.screen.blit(self.image, self.rect)
            self.current_time += 1
            if self.current_time == self.max_time:
                self.current_time = 0
                self.animation_index += 1
                if self.animation_index <= 35:
                    self.path = 'img/mill/chickenwindmil' + str(self.animation_index) + '.png'
                    self.image = pygame.transform.scale(pygame.image.load(self.path), (100,100))
                    self.img_mask = pygame.mask.from_surface(self.image)


                elif self.animation_index == 36:
                    self.path = 'img/mill/chickenwindmil' + str(self.animation_index) + '.png'
                    self.image = pygame.transform.scale(pygame.image.load(self.path), (100, 100))
                    self.img_mask = pygame.mask.from_surface(self.image)

                    #self.animation_index = self.img_index_list[self.index]
                    self.animation_index = 0

        if not self.alive:
            self.kill()

    # check the CURSOR position
    def check_shot(self, cursor, x, y):
        cursor_mask = pygame.mask.from_surface(cursor.image)
        offset = (x - self.rect.x, y - self.rect.y)
        result = self.img_mask.overlap(cursor_mask, offset)
        if result:
            return True
        else:
            return False