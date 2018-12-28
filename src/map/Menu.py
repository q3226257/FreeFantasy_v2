import pygame
from info.App import AppInfo

class Menu:
    def __init__(self, a):
        print("init" + a)

    def update(self, clock):
        while AppInfo.showMenu:
            clock.tick(60)
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    AppInfo.showMenu = False
