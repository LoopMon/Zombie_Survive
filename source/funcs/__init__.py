import pygame


def resizeImg(img: pygame.Surface, size: tuple[int, int]) -> pygame.Surface:
    img = pygame.transform.scale(img, size)
    return img