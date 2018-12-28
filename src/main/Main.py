import pygame
import map.Map
import map.Menu
from info.App import AppInfo


if __name__ == '__main__':
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode((380, 320))
    pygame.display.set_caption("Pyllet Town")
    clock = pygame.time.Clock()
    menu = map.Menu.Menu("aa")
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                AppInfo.showMenu = True
        tower = map.Map.Tower(screen)
        tick = clock.tick(60)
        tower.update(tick)
        if AppInfo.showMenu:
            menu.update(clock)
        print("main")
        pygame.display.flip()
