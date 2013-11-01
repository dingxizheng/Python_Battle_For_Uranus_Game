import sys, pygame
from random import randrange, uniform

class Background(pygame.sprite.Sprite):
    image_1 = None
    image_2 = None
    rect_1  = None
    rect_2  = None
    active  = True
    screen  = None
    speed   = (0 , 1)
    bgs     = [1, 1, 1, 1]
    current = 0

    def __init__(self, screen_, location):
        super(Background, self).__init__()
        self.screen = screen_
        try:
            self.resize_1((0, 600))
        except IOError:
            print "An error occured trying to read the file."
        # self.x, self.y = location[0], location[1]t

    def draw(self):
        if self.image_1 != None :
            self.rect_1.topleft = (self.rect_1.left + self.speed[0], self.rect_1.top + self.speed[1])
            self.screen.blit(self.image_1, self.rect_1) 
        if self.image_2 != None :
            self.rect_2.topleft = (self.rect_2.left + self.speed[0], self.rect_2.top + self.speed[1])
            self.screen.blit(self.image_2, self.rect_2)

    def update(self):
        self.load_bg()

    def event_handler(self, event):
        pass

    def keyhold_handler(self):
        pass

    def load_bg(self):
        if self.image_1 != None and self.rect_1.top > 600 :
            self.image_1 = None
        if self.image_2 != None and self.rect_2.top > 600 :
            self.image_2 = None

        if ((self.rect_1 != None and self.rect_1.top > 0) or 
            (self.rect_2 != None and self.rect_2.top > 0)) and (self.image_1 == None or self.image_2 == None) :
            print "load"
            if self.image_1 == None :
                self.resize_1((0, self.rect_2.top))
            else :
                self.resize_2((0, self.rect_1.top))

    def resize_1(self, bottomleft):
        filename     = "assets/bgs/b" + str(self.bgs[self.current]) +".jpg"
        self.current = (self.current + 1) % self.bgs.__len__()
        surface      = pygame.image.load(filename)
        size         = surface.get_rect()
        bg           = pygame.transform.scale(surface, (800, int(800.0 / size.width * size.height)))
        self.image_1 = bg.convert()
        self.rect_1  = self.image_1.get_rect()
        self.rect_1.topleft = (bottomleft[0], bottomleft[1] - self.rect_1.height)

    def resize_2(self, bottomleft):
        filename     = "assets/bgs/b" + str(self.bgs[self.current]) +".jpg"
        self.current = (self.current + 1) % self.bgs.__len__()
        surface      = pygame.image.load(filename)
        size         = surface.get_rect()
        bg           = pygame.transform.scale(surface, (800, int(800.0 / size.width * size.height)))
        self.image_2 = bg.convert()
        self.rect_2  = self.image_2.get_rect()
        self.rect_2.topleft = (bottomleft[0], bottomleft[1] - self.rect_2.height)

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

    bg = Background(screen, (0, 0))
    while(True):
        fpsClock.tick(50)
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit();sys.exit();
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE:
                    pygame.quit();sys.exit();

        bg.update()
        bg.draw()
        
        pygame.display.flip() 