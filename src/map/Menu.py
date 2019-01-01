import pygame
import thorpy
from info.App import AppInfo
from main.Constant import *
from info.Items import *
import main.Main
from interface.EventDeal import Update

a = [Big(), Big(), Big()]


class Menu(Update):
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        rect = pygame.Rect(screen.get_width() / 2, 0, screen.get_width() / 2, screen.get_height())
        menu_screen = self.screen.subsurface(rect)
        self.table_list: thorpy.TableList = thorpy.TableList(
            menu_screen, column_num=5, row_num=10)

    def update(self, clock, *params):
        # while AppInfo.current_stat == STAT.MENU_STAT:
        fps = clock.tick(60)

        self.table_list.update(fps, *a)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                main.Main.change_stat(STAT.MAP_STAT)
