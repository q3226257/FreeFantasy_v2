import pygame
import thorpy
from interface.EventDeal import *
from info.Items import *

FONT_COLOR = (255, 255, 255)
BG_COLOR = (20, 14, 10)
FONT = "simsunnsimsun"


class TableList(Update):
    def __init__(self, screen: pygame.Surface, column_num, row_num):
        self.rect = screen.get_rect()
        self.screen = screen
        self.column_num = column_num
        self.row_num = row_num
        self.cell_wid = self.rect.width // column_num
        self.cell_hei = self.rect.height // row_num
        self.item_wid = self.cell_wid - 15
        self.item_hei = self.cell_hei - 15
        self.elements = [None] * column_num * row_num
        self.bg_item: pygame.Surface = None
        self.item_rect = (self.cell_wid / 2 - self.item_wid / 2,
                          self.cell_hei / 2 - self.item_hei / 2,
                          self.item_wid,
                          self.item_hei)

    def update(self, fps, *params):
        self.screen.fill(color=BG_COLOR)

        for index, elem in enumerate(params):
            column = index % self.column_num
            row = index // self.row_num
            element = self.get(index)
            element.set_topleft((column * self.cell_wid + self.rect.left, row * self.cell_hei + self.rect.top))

            img = pygame.transform.scale(elem.get_item_surface(), (self.item_wid, self.item_hei))
            copy = self.bg_item.copy()
            copy.blit(img,
                      self.item_rect
                      )
            element.set_image(copy)
            element.blit()
            element.update()

    def get(self, index):
        index_ = self.elements[index]
        if index_ is None:
            index_ = thorpy.make_image_button(img_normal=r"D:\PycharmProjects\FreeFantasy_v2\src\resource\item_bg2.png")
            index_.set_font(FONT)
            index_.set_size((self.cell_wid - 2, self.cell_hei - 2))
            index_.set_font_color(FONT_COLOR)
            index_.surface = self.screen
            if self.bg_item is None:
                self.bg_item = index_.get_image()
            self.elements[index] = index_
        return index_
