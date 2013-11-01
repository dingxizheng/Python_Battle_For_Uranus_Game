import sys, pygame
from random import randrange, uniform

class Laser(pygame.sprite.Sprite):
    x       = 0
    y       = 0
    dx      = 0
    dy      = 0
    image   = None
    image_w = 0
    image_h = 0
    rect    = None
    active  = True
    screen  = None
    speed   = (0 , 7)

    def __init__(self, screen_, location):
        super(Laser, self).__init__()
        self.screen = screen_
        try:
            Laser.image = pygame.image.load("assets/laser.gif").convert()
            self.image  = Laser.image
            self.rect   = self.image.get_rect()
        except IOError:
            print "An error occured trying to read the file."
        self.x, self.y = location[0], location[1]
        self.image_w   = self.rect.width
        self.image_h   = self.rect.height
        self.reset()
        self.play_sound()

    def play_sound(self):
        pygame.mixer.music.load('assets/laser.wav')
        pygame.mixer.music.play()

    def draw(self):
        self.screen.blit(self.image, self.rect) 

    def update(self):
        self.x += self.speed[0]
        self.y -= self.speed[1]
        self.rect.topleft = [self.x, self.y]
        if self.y < -10 :
            self.active = False

    def event_handler(self, event):
        pass

    def keyhold_handler(self):
        pass

    def reset(self):
        self.x -= self.image_w / 2
        self.y -= self.image_h / 2

    def kill(self):
        del self




#=========================================================================
if __name__ == "__main__":
    pygame.init()
    fpsClock = pygame.time.Clock()
    screen   = pygame.display.set_mode((800, 600))
    counter  = 0
    span     = randrange(10, 35)
    lasers   = []

    while(True):
        fpsClock.tick(50)
        counter += 1
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit();sys.exit();
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE:
                    pygame.quit();sys.exit();

        for las_ in lasers :
            if las_.active :
                las_.update()
                las_.draw()
            else :
                lasers.remove(las_)
                las_.kill()

        if counter > span :
            las = Laser(screen, (randrange(0, 800), 600))
            las.speed = (0, randrange(5, 25))
            lasers.append(las)
            counter = 0
            span = randrange(10, 35)

        pygame.display.flip() 