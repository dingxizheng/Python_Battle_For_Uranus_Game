import sys
import pygame
from random import randint

class Laser(pygame.sprite.Sprite):
    x = 0
    y = 0
    dx = 0
    dy = 0
    image = None
    image_w = 0 
    image_h = 0
    rect = None
    active = True
    screen = None
    speedY = 10

    def __init__(self, screen_, posX, posY):
    	self.screen = screen_
        self.image = pygame.image.load("assets/laser.gif")
        self.rect = self.image.get_rect()
        self.image_h = self.rect.height
        self.image_w = self.rect.width
        self.x = posX
        self.y = posY

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
    	self.rect.topleft = [self.x, self.y]
        self.y -= self.speedY
        if self.y < 0:
            self.active = False

    def delete(self):
        del self

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800,600))
    lasers = []
    color = (0,0,0)

    # laser = Laser(screen, randint(0, 800), 600)
    # lasers.append(laser)
    while True:
        msElapsed = clock.tick(50)
        screen.fill(color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();sys.exit();
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit();sys.exit();

        for laser_ in lasers:
            if laser_.active:
                laser_.update()
                laser_.draw()
            else:
                lasers.remove(laser_)
                laser_.delete

        laser = Laser(screen, randint(0, 800), 600)
        lasers.append(laser)

        pygame.display.flip()