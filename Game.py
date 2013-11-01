import os, sys, pygame
sys.path.append(os.getcwd())
from random import randrange, uniform
import Battlecruiser as battle
import Enermy        as enermy
import Background    as background

pygame.init()

FPS      = 45
win_w    = 800
win_h    = 600
fpsClock = pygame.time.Clock()
screen   = pygame.display.set_mode((win_w, win_h))
color    = (255, 0, 0)
enermies_num = 10


object_draws     = []
event_handlers   = []
keyhold_handlers = []
object_updates   = [] 

enermies         = []

b                = battle.Battlecruiser(screen, [400, 300])
bg               = background.Background(screen, [0, 0])

def register_sprite(sprite):
    event_handlers.append(sprite.event_handler)
    object_draws.append(sprite.draw)
    keyhold_handlers.append(sprite.keyhold_handler)
    object_updates.append(sprite.update)

def unregiter_sprite(sprite):
    event_handlers.remove(sprite.event_handler)
    object_draws.remove(sprite.draw)
    keyhold_handlers.remove(sprite.keyhold_handler)
    object_updates.remove(sprite.update)

def enermy_creator(num):
    if enermies.__len__() < num :
        gen = True
        e = enermy.Enermy(screen, (randrange(10, 790), -10))
        for en in enermies : # 
            if en.do_rect_detect(e.rect, en.rect):
                gen = False; break
        if gen :
            e.speed = (0, randrange(2, 8))
            enermies.append(e)
            register_sprite(e)
        else :
            e.kill()

def del_unactive_enermy():
    for en in enermies :
        if en.y > 600 and not en.active :
            enermies.remove(en)
            unregiter_sprite(en)
            en.kill()

def fire_at_enermy(battle_):
    for en in enermies :
        en.collision_test(battle_.lasers, battle_.update_score)


def quit_game(event): # quit game
    if event.type == pygame.QUIT :
        pygame.quit();sys.exit()
    if event.type == pygame.KEYDOWN :
        if event.key == pygame.K_ESCAPE:
            pygame.quit();sys.exit();

def lose_life(battle_):
    for en in enermies :
        enermies.remove(en)
        unregiter_sprite(en)
        en.kill()
    battle_.reset()
    battle_.lives -= 1
    battle_.active = True

def game_over(battle_):
    if battle_.lives <= 0 : 
        myfont = pygame.font.SysFont("monospace", 40)
        myfont.set_bold(True)
        label = myfont.render("Game Over", 10, (255, 0, 0))
        screen.blit(label, (250, 300))
        battle_.active = False


def update():
    screen.fill((40, 40, 40))

    if b.lives > 0 :
        enermy_creator(10) # maintain 5 enermies 
        fire_at_enermy(b)

    del_unactive_enermy()

    for event in pygame.event.get():
        quit_game(event) # quit game
        for handler_fn in event_handlers:
            handler_fn(event) # fire all event handlers

    for keyhold_fn in keyhold_handlers:
        keyhold_fn() # fire all key hold handlers

    for update_fn in object_updates:
        update_fn() # fire all objects' update functions

    for render_fn in object_draws:
        render_fn() # fire all render functions 

    if b.collision_test(enermies) :
        lose_life(b)

    game_over(b)
    pygame.display.flip()    
   

def game():
    # b = battle.Battlecruiser(screen, [400, 300])
    register_sprite(bg)
    register_sprite(b)

    while(True):
        update()
        fpsClock.tick(FPS)

game() # run