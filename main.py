
import pygame
from pygame.locals import *
from sys import exit

from scripts.config import _
#import scripts.config
from scripts.menu import *
from scripts.AireCraftSimulator import *
from scripts.AireCraftTutorial import *


def main_menu(screen):

    button_bgc = (0, 122, 204)
    clr_white = (255, 255, 255)

    while True:

        pygame.mouse.set_visible(True)

        screen.fill((0,0,0))
        draw_text(screen, 'Menu', _.font, clr_white, 20, 20)

        mx, my = pygame.mouse.get_pos()

        btn_sim = draw_button(screen, 50, 100, 320, 45, button_bgc, 'Play AireCraft', clr_white, 150, 110)
        btn_trl = draw_button(screen, 50, 200, 320, 45, button_bgc, 'Documentation', clr_white, 150, 210)
        btn_ext = draw_button(screen, 50, 300, 320, 45, button_bgc, 'Close', clr_white, 150, 310)


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()#sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()#sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if btn_sim.collidepoint((mx, my)):
                        AireCraftSimulator(screen)
                    elif btn_trl.collidepoint((mx, my)):
                        AireCraftTutorial(screen)
                    elif btn_ext.collidepoint((mx, my)):
                        pygame.quit()
                        exit()#sys.exit()


        pygame.display.update()
        _.mainClock.tick(_.FPS)



_.loadResources()
main_menu(_.screen)

#sys.exit()
#os.system("pause")

