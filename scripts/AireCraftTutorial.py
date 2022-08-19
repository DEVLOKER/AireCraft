import pygame
from pygame.locals import*
import sys

from scripts.config import _
from scripts.menu import *


def AireCraftTutorial(screen):

    running = True
    scroll_y = 0
    scroll_speed = 15

    while running:
        screen.fill((0,0,0))

        draw_text(screen, 'move mouse and click on left buttom for simple fire & right buttom for extra fire.', _.font, (255, 255, 255), 0, 20+scroll_y)
        drawImage(screen, "resources/images/airecraft/ac_2.png", 0, 80+scroll_y)
        drawImage(screen, "resources/images/mira.gif", 0, 250+scroll_y)
        draw_text(screen, 'press [Echap] to return', _.font, (255, 255, 255), 0, 420+scroll_y)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_UP: # up
                    scroll_y += scroll_speed
                elif event.key == K_DOWN: # down
                    scroll_y -= scroll_speed
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4: # up
                    scroll_y += scroll_speed
                if event.button == 5: # down
                    scroll_y -= scroll_speed

            if scroll_y > 0:
                scroll_y = 0

        pygame.display.update()
        _.mainClock.tick(_.FPS)