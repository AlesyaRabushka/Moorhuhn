import pygame

class BigChicken(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)

        self.screen = screen

        # show on the screen properties
        self.alive = True

        self.show = False
        self.show_cycle = False
        self.max_show_time = 6
        self.max_cycle_show_time = 10
        self.current_time = 0
        self.index = 0

        # time in CYCLE SHOW to count BLINK time
        self.blink_pause = 6
        self.current_blink_time = 0

        # timer to count till first show
        self.wait_time = 20
        self.current_wait_time = 0

        self.path = 'img/big_chicken/big_chicken' + str(self.index) + '.png'
        self.image = pygame.transform.scale(pygame.image.load(self.path), (100,100))
        self.rect = self.image.get_rect(center=(500, 420))


    def update(self):
        # when it appears FIRST TIEM
        if self.show:
            self.current_time += 1
            self.screen.blit(self.image, self.rect)

            if self.current_time == self.max_show_time:
                self.index += 1
                self.current_time = 0

                if self.index <= 17:
                    self.path = 'img/big_chicken/big_chicken' + str(self.index) + '.png'
                    self.image = pygame.transform.scale(pygame.image.load(self.path), (100, 100))

                elif self.index == 18:
                    self.path = 'img/big_chicken/big_chicken' + str(self.index) + '.png'
                    self.image = pygame.transform.scale(pygame.image.load(self.path), (100, 100))
                    self.show = False
                    self.show_cycle = True
                    self.current_time = 0
                    self.index = 8

        # when it just BLINKS
        elif self.show_cycle:
            self.current_time += 1
            self.screen.blit(self.image, self.rect)

            if self.current_time == self.max_show_time:
                self.current_time = 0

                if self.index == 8:
                    self.path = 'img/big_chicken/big_chicken' + str(self.index) + '.png'
                    self.image = pygame.transform.scale(pygame.image.load(self.path), (100, 100))
                    self.index += 1
                    self.current_blink_time += 1

                elif self.index == 9:
                    if self.current_blink_time == self.blink_pause:
                        self.path = 'img/big_chicken/big_chicken' + str(self.index) + '.png'
                        self.image = pygame.transform.scale(pygame.image.load(self.path), (100, 100))
                        self.index += 1
                        self.current_blink_time = 0
                    else:
                        self.index -= 1

                elif self.index > 9 and self.index <= 17:
                    self.path = 'img/big_chicken/big_chicken' + str(self.index) + '.png'
                    self.image = pygame.transform.scale(pygame.image.load(self.path), (100, 100))
                    self.index += 1

                elif self.index == 18:
                    self.path = 'img/big_chicken/big_chicken' + str(self.index) + '.png'
                    self.image = pygame.transform.scale(pygame.image.load(self.path), (100, 100))
                    self.index = 8