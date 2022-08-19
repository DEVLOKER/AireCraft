import pygame
from pygame.locals import *
import sys

from scripts.config import _
from scripts.menu import *
from scripts.AireCraft import AireCraft
from scripts.Bullet import Bullet
from scripts.Explosion import Explosion

#___________________________________ var _________________________________________

b1x , b1y = 0 , 0
b2x , b2y = 0, -_.SCREEN_HEIGHT
c1x, c1y = 0,-100
c2x, c2y = 200,350
c3x, c3y = 600,100
c4x, c4y = 700,600

#___________________________________ drawBackground _________________________________________

def drawBackground(screen):
    global b1x, b1y, b2x, b2y
    screen.blit(_.bg1,(int(b1x),int(b1y)))
    screen.blit(_.bg2,(int(b2x),int(b2y)))

    b1y += 0.05
    b2y += 0.05

    if b1y > _.SCREEN_HEIGHT : b1y = -_.SCREEN_HEIGHT+10
    if b2y > _.SCREEN_HEIGHT : b2y = -_.SCREEN_HEIGHT+10

#___________________________________ drawClouds _________________________________________

def drawClouds(screen):
    global c1x, c1y, c2x, c2y, c3x, c3y, c4x, c4y
    screen.blit(_.cloud1,(int(c1x),int(c1y)))
    screen.blit(_.cloud2,(int(c2x),int(c2y)))
    screen.blit(_.cloud3,(int(c3x),int(c3y)))
    screen.blit(_.cloud4,(int(c4x),int(c4y)))

    c1x+=.1
    c2x+=.3
    c3x+=.4
    c4x+=.2

    if c1x > _.SCREEN_WIDTH+10: c1x = -700
    if c2x > _.SCREEN_WIDTH+10: c2x = -700
    if c3x > _.SCREEN_WIDTH+10: c3x = -700
    if c4x > _.SCREEN_WIDTH+10: c4x = -700

#___________________________________ drawMira _________________________________________

def drawMira(screen, x_, y_):
    x_+=5
    y_+=5
    space_ = 3
    len_ = 10
    clr_ = (255, 0, 0)
    pygame.draw.line(screen, clr_, (x_, y_-space_), (x_, y_-len_-space_))
    pygame.draw.line(screen, clr_, (x_, y_+space_), (x_, y_+len_+space_))
    pygame.draw.line(screen, clr_, (x_-space_, y_), (x_-len_-space_, y_))
    pygame.draw.line(screen, clr_, (x_+space_, y_), (x_+len_+space_, y_))
    pygame.draw.circle(screen, clr_, (x_, y_), len_, 1)

#___________________________________ AireCraftSimulator _________________________________________

def AireCraftSimulator(screen):

    running = True
    x_pos = y_pos = 0
    pygame.mouse.set_visible(False)
    while running:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == MOUSEMOTION:
                x_pos, y_pos = pygame.mouse.get_pos()
            elif event.type == MOUSEBUTTONDOWN:
                if len(_.list_bullets)<_.MAX_BULLETS:
                    x_clique, y_clique = pygame.mouse.get_pos()
                    if event.button == 1: # left
                        _.list_bullets.append(Bullet(Bullet.LASER_, x_clique, y_clique))
                    if event.button == 3: # right
                        _.list_bullets.append(Bullet(Bullet.MISSILE_, x_clique, y_clique))


        for i_ in range(len(_.list_airecraft),_.MAX_AIRECRAFTS):
            _.list_airecraft.append(AireCraft())

        screen.fill((0,0,0))

        drawBackground(screen)
        drawClouds(screen)

        for a_c_ in _.list_airecraft:
            if a_c_.alive:
                    a_c_.move()
                    screen.blit(a_c_.img_, (int(a_c_.x_), int(a_c_.y_) ) )
            else:
                    _.list_airecraft.remove(a_c_)


        for b_ in _.list_bullets:
            if b_.alive:
                    b_.move()
                    screen.blit(b_.img_, ( int(b_.x_), int(b_.y_) ) )
            else:
                    _.list_bullets.remove(b_)


        for exp_ in _.list_explosions:
            if True or b_.alive:
                exp_.update()
                screen.blit(exp_.img_, ( int(exp_.x_), int(exp_.y_) ) )
            else:
                _.list_explosions.remove(exp_)


        drawMira(_.screen, x_pos, y_pos)

        #if len(_.list_explosions)>0:
            #print(len(_.list_explosions))

        pygame.display.update()
        _.mainClock.tick(_.FPS)


