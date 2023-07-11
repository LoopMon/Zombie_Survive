import pygame
from random import randint


class Light(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        self.sprites = [
            pygame.image.load(f'source/imgs/Light/Light{i}.png') for i in range(1, 9)
        ]
        self.frame = randint(0, 7)
        self.image = self.sprites[self.frame]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        self.frame += 0.05

        if self.frame >= len(self.sprites):
            self.frame = 0

        self.image = self.sprites[int(self.frame)]
        self.image = pygame.transform.scale(self.image, (64, 64))

