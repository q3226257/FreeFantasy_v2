import pygame
import map.Map

if __name__ == '__main__':
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode((380, 320))
    pygame.display.set_caption("Pyllet Town")
    clock = pygame.time.Clock()

    while 1:
        for event in pygame.event.get():
            pass
        tower = map.Map.Tower(screen)
        tick = clock.tick(60)
        tower.update(tick)
        pygame.display.flip()
