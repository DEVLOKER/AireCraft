from scripts.config import _
import pygame
from random import randint

class AireCraft():
    def __init__(self):
        # (108, 108)
        size_w, size_h = 60, 60

        self.speed_ = 0.1
        self.alive = True
        self.direction = randint(1, 4)
        if self.direction==1:
            self.x_ = 0
            self.y_ = randint(0, _.SCREEN_HEIGHT)
        elif self.direction==3:
            self.x_ = _.SCREEN_WIDTH
            self.y_ = randint(0, _.SCREEN_HEIGHT)
        elif self.direction==4:
            self.x_ = randint(0, _.SCREEN_WIDTH)
            self.y_ = 0
        elif self.direction==2:
            self.x_ = randint(0, _.SCREEN_WIDTH)
            self.y_ = _.SCREEN_HEIGHT

        img = pygame.image.load("resources/images/airecraft/ac_"+str(self.direction)+".png").convert_alpha()
        self.img_ = pygame.transform.scale(img, (size_w, size_h))
        self.rect = self.img_.get_rect()

    def move(self):

        if(self.direction==1):
            self.x_ += self.speed_
        elif(self.direction==3):
            self.x_ -= self.speed_
        elif(self.direction==4):
            self.y_ += self.speed_
        elif(self.direction==2):
            self.y_ -= self.speed_

        self.rect.x = int(self.x_)
        self.rect.y = int(self.y_)

        if self.x_ > _.SCREEN_WIDTH or self.x_+self.rect.w < 0 or self.y_ > _.SCREEN_HEIGHT or self.y_+self.rect.h < 0 :
            self.alive = False
