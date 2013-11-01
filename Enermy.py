import os, sys, pygame 
sys.path.append(os.getcwd())
from random import randrange, uniform

class Enermy(pygame.sprite.Sprite):
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
    speed   = (0 ,0)

    def __init__(self, screen_, location):
        super(Enermy, self).__init__()
        self.screen = screen_
        try:
            Enermy.image = pygame.image.load("assets/mutalisk.gif").convert()
            self.image          = Enermy.image
            self.rect           = self.image.get_rect()
        except IOError:
            print "An error occured trying to read the file."
        self.x, self.y = location[0], location[1]
        self.image_w   = self.rect.width
        self.image_h   = self.rect.height
        self.reset()


    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += self.speed[0]
        self.y += self.speed[1]
        self.rect.topleft = [self.x, self.y]
        if self.y < -30 or self.y > 610:
            self.active = False

    def collision_test(self, lasers, update_score):
        if self.active:
            for laser in lasers :
                if self.do_rect_detect(laser.rect, self.rect) and self.active :
                    self.active = False
                    lasers.remove(laser)
                    laser.kill()
                    self.exploses()
                    self.speed = (self.speed[0], 15)
                    if update_score :
                        update_score(100)
        
    def event_handler(self, event):
        pass

    def keyhold_handler(self):
        pass

    def do_rect_detect(self, rect1, rect2):
        for a, b in [(rect1, rect2), (rect2, rect1)]:
            if((self.is_point_inside_rect(a.left, a.top, b)) or 
               (self.is_point_inside_rect(a.left, a.bottom, b)) or 
               (self.is_point_inside_rect(a.right, a.top, b)) or 
               (self.is_point_inside_rect(a.right, a.bottom, b))):
                return True
        return False


    def is_point_inside_rect(self, x, y, rect):
        if x in range(rect.left, rect.right) and y in range(rect.top, rect.bottom):
            return True
        else:
            return False

    
    def bounce_off(self):
        if self.x not in range(0 - self.image_w / 2, 800 - self.image_w / 2) :
            self.speed = (- self.speed[0], self.speed[1])

        if self.y not in range(0 - self.image_h / 2, 600 - self.image_h / 2) :
            self.speed = (self.speed[0], - self.speed[1])

    def exploses(self):
        try:
            Enermy.image = pygame.image.load("assets/laser_explosion.gif").convert()
            self.image   = Enermy.image
            self.rect    = self.image.get_rect()
        except IOError:
            print "An error occured trying to read the file."
        self.image_w   = self.rect.width
        self.image_h   = self.rect.height
        self.reset()

    def reset(self):
        # self.x = self.x - self.image_w / 2
        self.y = self.y - self.image_h / 2

    def kill(self): # destroy itself
        del self

#=========================================================================
if __name__ == "__main__":
    pygame.init()
    fpsClock = pygame.time.Clock()
    screen   = pygame.display.set_mode((800, 600))
    enermies = []
    e = Enermy(screen, [400, 300])
    e.speed = (4, 4)

    for i in range(11) :
        e = Enermy(screen, [400, 300])
        e.speed = (randrange(-5, 5), randrange(-4, 4))
        enermies.append(e)

    while(True):
        fpsClock.tick(50)
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit();sys.exit();
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE:
                    pygame.quit();sys.exit();
            for e in enermies :
                e.event_handler(event)

        for e in enermies :
            e.update()
            e.draw()
            e.bounce_off()

        pygame.display.flip() 