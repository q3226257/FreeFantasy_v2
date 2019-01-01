import pygame
import map.Menu
import thorpy
from info.App import AppInfo
from map.Map import *
from main.Constant import *

if __name__ == '__main__':
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode((680, 580))
    pygame.display.set_caption("FreeFantasy")
    clock = pygame.time.Clock()
    c_menu = map.Menu.Menu(screen)
    c_map = Tower(screen)

    thorpy.Application(screen.get_size(), "ThorPy Overview")
    while 1:
        if AppInfo.current_stat == STAT.MENU_STAT:
            c_menu.update(clock)
        elif AppInfo.current_stat == STAT.MAP_STAT:
            c_map.update(clock)
        if AppInfo.current_stat == STAT.BATTLE_STAT:
            pass

        pygame.display.flip()


def change_stat(stat):
    AppInfo.current_stat = stat
