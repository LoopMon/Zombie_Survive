import pygame


class Plank(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, angle: int = 0):
        pygame.sprite.Sprite.__init__(self)

        self.sprite = pygame.image.load('source/imgs/plank.png')
        self.sprites = [
            self.sprite.subsurface(pygame.Rect(0, i*32, 32, 32)) for i in range(0, 2) 
        ]

        self.image = self.sprites[0]
        self.image = pygame.transform.scale(self.image, (80, 40))
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.angle = angle

    def breakUp(self):
        self.image = self.sprites[1]
        self.image = pygame.transform.scale(self.image, (80, 40))
        self.image = pygame.transform.rotate(self.image, self.angle)
    
    def repair(self):
        self.image = self.sprites[0]
        self.image = pygame.transform.scale(self.image, (80, 40))
        self.image = pygame.transform.rotate(self.image, self.angle)