import pygame
from util.Utils import *


class weapon:

    def __init__(self):
        self.name = ""
        self.times = 0
        self.img: pygame.Surface = pygame.image.load(r"D:\PycharmProjects\FreeFantasy_v2\src\resource\big_.jpg")
        self.bg = pygame.image.load(r"D:\PycharmProjects\FreeFantasy_v2\src\resource\bg_circle.png")
        self.bg = pygame.transform.scale(self.bg, (self.img.get_width() - 20, self.img.get_height() - 20))

    def get_item_surface(self):
        bg = pygame.transform.rotate(self.bg, (self.times * 1) % 360)
        img = self.img.copy()
        rect = get_center_rect(img, bg)
        img.blit(bg, rect)

        if self.times >= 3600000:
            self.times = 0

        self.times += 1
        return img


class Big(weapon):
    def __init__(self):
        super().__init__()
        self.name = "大头锤"
