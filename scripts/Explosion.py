import pygame
from scripts.config import _


class Explosion(pygame.sprite.Sprite):
    #explosion_anim = _.explosion_anim
    def __init__(self, x, y):
        super().__init__()
        self.x_ = x
        self.y_ = y

        self.img_ = _.explosion_anim[0]
        self.rect = self.img_.get_rect()
        self.rect.x = int(self.x_)
        self.rect.y = int(self.y_)

        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 100
        self.alive = True
        pygame.mixer.music.load("resources/audio/explosion.wav")
        pygame.mixer.music.play()
        #pygame.mixer.Channel(0).play(pygame.mixer.Sound("resources/audio/missile_explosion.wav"))

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update > self.frame_rate:
            self.last_update = current_time
            self.frame +=1
            if self.frame < len(_.explosion_anim):
                self.img_ = _.explosion_anim[self.frame]
                self.rect = self.img_.get_rect()
                self.rect.x = int(self.x_)
                self.rect.y = int(self.y_)
            else:
                self.alive = False
                _.list_explosions.remove(self)
                self.kill()
