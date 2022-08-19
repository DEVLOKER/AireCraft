
import pygame


class _ (object):

    #___________________________________ Const  _________________________________________

    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 500
    FPS = 1000 # frames per second setting
    MAX_AIRECRAFTS = 10
    MAX_BULLETS = 2
    list_airecraft = []
    list_bullets = []
    list_explosions = []

    explosion_anim = []

    runing = True
    mainClock = None
    screen = None
    bg1 = bg2 = None
    b1x = b1y = b2x = b2y = None
    cloud1 = cloud2 = cloud3 = cloud4 = None
    c1x = c1y = c2x = c2y = c3x = c3y = c4x = c4y = None

    font = None

    @staticmethod
    def loadResources():

        pygame.init()

        _.mainClock = pygame.time.Clock()
        _.screen = pygame.display.set_mode((_.SCREEN_WIDTH, _.SCREEN_HEIGHT), 0, 32)
        pygame.display.set_caption("AireCraft")

        pygame.display.set_icon(pygame.image.load('resources/images/mira.ico'))

        pygame.mixer.init(44100, -16, 2, 1024)
        pygame.mixer.music.set_volume(0.8)


        _.bg1 = pygame.image.load('resources/images/bg/bg01.jpg').convert_alpha()
        _.bg1 = pygame.transform.scale(_.bg1,(_.SCREEN_WIDTH, _.SCREEN_HEIGHT))
        _.bg2 = pygame.image.load('resources/images/bg/bg02.jpg').convert_alpha()
        _.bg2 = pygame.transform.scale(_.bg2,(_.SCREEN_WIDTH, _.SCREEN_HEIGHT))

        _.cloud1=pygame.image.load('resources/images/cloud/cloud01.png').convert_alpha()
        _.cloud1=pygame.transform.rotozoom(_.cloud1, 0, 0.5)
        _.cloud2=pygame.image.load('resources/images/cloud/cloud02.png').convert_alpha()
        _.cloud2=pygame.transform.rotozoom(_.cloud2, 0, 0.5)
        _.cloud3=pygame.image.load('resources/images/cloud/cloud03.png').convert_alpha()
        _.cloud3=pygame.transform.rotozoom(_.cloud3, 0, 0.5)
        _.cloud4=pygame.image.load('resources/images/cloud/cloud04.png').convert_alpha()
        _.cloud4=pygame.transform.rotozoom(_.cloud4, 0, 0.5)

        #_.font = pygame.font.SysFont(None, 20)
        _.font = pygame.font.Font('resources/font/tahoma.ttf', 24)

        _.explosion_anim = [pygame.transform.scale(pygame.image.load('resources/images/exp/explosion0'+str(i)+'.png').convert_alpha(), (75, 75)) for i in range(1, 8+1)]



