import pygame
from scripts.config import _



def draw_text(screen, text, font, color, x, y):
    textobj = font.render(text, 1, color)
    rect_txt = textobj.get_rect()
    rect_txt.topleft = (x, y)
    rect_txt.centerx = int(_.SCREEN_WIDTH / 2)
    screen.blit(textobj, rect_txt)
    return rect_txt


def draw_button(screen, x, y, w , h, bg_c, text_, clr_, x_, y_):
    rect_btn = pygame.Rect(x, y, w, h)
    rect_btn.centerx = int(_.SCREEN_WIDTH / 2)
    pygame.draw.rect(screen, bg_c, rect_btn)
    rect_txt = draw_text(screen, text_, _.font, clr_, x_, y_)
    #rect_txt.centery = rect_btn.centery
    return rect_btn


def drawImage(screen, path, x, y):
    img_ = pygame.image.load(path).convert_alpha()
    rect_img = img_.get_rect()
    if(rect_img.w > _.SCREEN_WIDTH):
        img_ = pygame.transform.scale(img_,(_.SCREEN_WIDTH, y))
        rect_img = img_.get_rect()
    rect_img.centerx = int(_.SCREEN_WIDTH / 2)
    screen.blit(img_, (rect_img.x, y))
    return rect_img