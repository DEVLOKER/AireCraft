from scripts.config import _
from scripts.AireCraft import AireCraft
from scripts.Explosion import Explosion
import pygame
#from math import degrees, atan2, sqrt, cos, sin
import math


class Bullet():
    types_ = [{
        "name" : "laser",
        "speed" : 1.5,
        "img" : "resources/images/bullet/laser.png",
        "sound" : "resources/audio/laser.mp3"
    },{
        "name" : "missile",
        "speed" : 2.5,
        "img" : "resources/images/bullet/missile.png",
        "sound" : "resources/audio/missile.mp3"
    }]
    LASER_, MISSILE_ = 0, 1
    def __init__(self, b_type, x_d, y_d):

        self.x_s_ = _.SCREEN_WIDTH / 2
        self.y_s_ = _.SCREEN_HEIGHT
        self.x_ = self.x_s_
        self.y_ = self.y_s_

        dx, dy = x_d - self.x_s_, y_d - self.y_s_
        self.angle_ = math.degrees(math.atan2(-dy, dx))
        #self.distance_ = math.sqrt ( dx**2 + dy**2)

        self.alive = True
        self.type_ = b_type

        self.speed_ = Bullet.types_[self.type_]["speed"]

        img = pygame.image.load(Bullet.types_[self.type_]["img"]).convert_alpha()
        self.img_ = pygame.transform.scale(img, (10, 50))
        self.img_ = pygame.transform.rotate(img, self.angle_-90) # correction_angle
        #self.img_ = pygame.transform.rotozoom(img, self.angle_-90, 0.9)
        self.rect = self.img_.get_rect()

        pygame.mixer.music.load(Bullet.types_[self.type_]["sound"])
        pygame.mixer.music.play()
        #pygame.mixer.Channel(0).play(pygame.mixer.Sound("resources/audio/"+str(self.type_)+".mp3"))

    def move(self):

        self.x_ += math.cos(math.radians(self.angle_)) * self.speed_
        self.y_ -= math.sin(math.radians(self.angle_)) * self.speed_

        self.rect.x = int(self.x_)
        self.rect.y = int(self.y_)

        for a_c_ in _.list_airecraft:
            if self.is_collided_with(a_c_):
                _.list_explosions.append(Explosion(a_c_.x_, a_c_.y_))
                a_c_.alive = False
                self.alive = False


        if self.x_ > _.SCREEN_WIDTH or self.x_+self.rect.w < 0 or self.y_ > _.SCREEN_HEIGHT or self.y_+self.rect.h < 0 :
                self.alive = False

    def is_collided_with(self, acirecraft_):
        #return self.rect.colliderect(acirecraft_.rect)
        return pygame.Rect.colliderect(self.rect, acirecraft_.rect)

