from loops.play_loop import *
from settings.states import *

pygame.init()

class Camera:
    """
    Camera scrolling class
    """
    def __init__(self,x,y):
        self.rect = pygame.Rect(x, y, 800, 600)

    def move(self, x):
        print(self.rect[0])
        if self.rect[0] == 1900:
            if x < 0:
                self.rect[0] += x
                return True
            else:
                self.rect[0] += 0
                return False
        elif self.rect[0] == 0:
            if x > 0:
                self.rect[0] += x
                return True
            else:
                self.rect[0] += 0
                return False
        else:
            self.rect[0] += x
            return True



sky = pygame.image.load('img/world/sky.png')
bg1 = pygame.transform.scale(sky, (4000, 500))

castle = pygame.image.load('img/world/background1.png')
bg2 = pygame.transform.scale(castle, (2120, 500))

green = pygame.image.load('img/world/background2.png')






