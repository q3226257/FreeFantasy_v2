import pygame


def get_center_rect(src: pygame.Surface, dest):
    return pygame.Rect(src.get_width() / 2 - dest.get_width() / 2,
            src.get_height() / 2 - dest.get_height() / 2,
            dest.get_width(),
            dest.get_height())
