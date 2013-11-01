import os, sys, pygame
sys.path.append(os.getcwd())
import Laser as la
from pygame.locals import KEYDOWN

class Battlecruiser(pygame.sprite.Sprite):
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
    lasers  = []
    score   = 0
    lives   = 4

    def __init__(self, screen_, location):
        super(Battlecruiser, self).__init__()
        self.screen = screen_
        try:
            Battlecruiser.image = pygame.image.load("assets/battlecruiser.gif").convert()
            self.image          = Battlecruiser.image
            self.rect           = self.image.get_rect()
        except IOError:
            print "An error occured trying to read the file."
        self.x, self.y = location[0], location[1]
        self.image_w   = self.rect.width
        self.image_h   = self.rect.height
        self.reset()
        # self.play_sound()

    def play_sound(self):
        pygame.mixer.music.load('assets/death_explode.wav')
        pygame.mixer.music.play()


    def draw(self):
        self.screen.blit(self.image, self.rect)
        self.display_parameter()
        for laser in self.lasers :
            laser.draw()

    def update(self):
        self.rect.topleft = [self.x, self.y]
        for laser in self.lasers :
            if laser.active :
                laser.update()
            else :
                self.lasers.remove(laser)
                laser.kill()

    def update_score(self, score):
        self.score += score

    def display_parameter(self):
        myfont = pygame.font.SysFont("monospace", 25)
        myfont.set_bold(True)
        label = myfont.render("score:" + str(self.score), 10, (255, 255, 0))
        self.screen.blit(label, (50, 0))
        label = myfont.render("lives: x " + str(self.lives), 10, (255, 255, 0))
        self.screen.blit(label, (590, 0))
        
    def event_handler(self, event):
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP :
                self.y -= 5
            elif event.key == pygame.K_DOWN :
                self.y += 5
            elif event.key == pygame.K_LEFT :
                self.x -= 5
            elif event.key == pygame.K_RIGHT :
                self.x += 5
            elif event.key == pygame.K_SPACE :
                self.fire()

    def keyhold_handler(self):
        keys_pressed = pygame.key.get_pressed()

        if self.x in range(0 - self.image_w / 2, 800 - self.image_w / 2) :
            if keys_pressed[pygame.K_LEFT]:
                self.x -= 5
            if keys_pressed[pygame.K_RIGHT]:
                self.x += 5
        if self.y in range(0 - self.image_h / 2, 600 - self.image_h / 2) :
            if keys_pressed[pygame.K_UP]:
                self.y -= 5
            if keys_pressed[pygame.K_DOWN]:
                self.y += 5

    def collision_test(self, enermies):
        if self.active:
            for enermy in enermies :
                if self.active and enermy.active and enermy.do_rect_detect(enermy.rect, self.rect):
                    self.active = False
                    self.play_sound()
                    return True
        return False


    def reset(self):
        self.x = 400 - self.image_w / 2
        self.y = 450

    def fire(self):
        laser1 = la.Laser(self.screen, (self.x + 10, self.y + self.image_h / 2 - 10))
        laser2 = la.Laser(self.screen, (self.x + self.image_w - 10, self.y + self.image_h / 2 - 10))
        self.lasers.append(laser1)
        self.lasers.append(laser2)

    def kill(self): # destroy itself
        del self

#=========================================================================
if __name__ == "__main__":
    pygame.init()
    fpsClock = pygame.time.Clock()
    screen   = pygame.display.set_mode((800, 600))

    b = Battlecruiser(screen, [400, 300])

    while(True):
        fpsClock.tick(50)
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit();sys.exit();
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE:
                    pygame.quit();sys.exit();

            b.event_handler(event)

        b.update()
        b.draw()
        b.keyhold_handler()

        pygame.display.flip() 