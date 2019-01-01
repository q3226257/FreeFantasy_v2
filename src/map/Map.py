from pygame import *
import pygame
import tmx
import main.Main
from interface.EventDeal import *
from info.App import *
from main.Constant import *


class ABSMap(EventDeal, Update):
    def __init__(self):
        self.initial_position = (0, 0)
        self.map: tmx.TileMap = None
        self.NPCs: tmx.SpriteLayer = None
        self.Player: tmx.SpriteLayer = None
        self.screen: Surface = None

    def react(self):
        for event in pygame.event.get():
            print(event)

    def update(self, fps, *params):
        # while AppInfo.current_stat == STAT.MAP_STAT:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                main.Main.change_stat(STAT.MENU_STAT)

        position = self.initial_position
        if self.Player is not None:
            position = self.Player.position

        self.map.set_focus(*position)
        self.map.update(fps)
        self.map.draw(self.screen)


class Tower(ABSMap):
    def __init__(self, screen: Surface):
        super().__init__()
        self.initial_position = (100, 100)
        self.screen = screen
        self.map = tmx.load(r"D:\PycharmProjects\FreeFantasy\src\tmx\my.tmx", screen.get_size())
