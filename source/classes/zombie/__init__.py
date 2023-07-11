import pygame


class Zombie(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)

        self.sprites = [
            [pygame.image.load(f'source/imgs/Zombies/Gray/Atack/zombie{i}.png') for i in range(1, 4)],
            [pygame.image.load(f'source/imgs/Zombies/Gray/Running/zombie{i}.png') for i in range(1, 7)],
            [pygame.image.load(f'source/imgs/Zombies/Gray/Stand/zombie{i}.png') for i in range(1, 5)],
        ]

        self.frame = 0
        self.state = 2
        self.image = self.sprites[self.state][self.frame]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        self.frame += 0.1

        if self.frame >= len(self.sprites[self.state]):
            self.frame = 0

        self.image = self.sprites[self.state][int(self.frame)] 
        self.image = pygame.transform.scale(self.image, (128, 128))