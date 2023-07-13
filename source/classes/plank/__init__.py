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
        self.life = 100
        self.visible = True
        self.frame = 0

    def breakUp(self):
        if self.life <= 0:
            self.frame += 0.1
            if self.frame >= 3:
                self.visible = False
                self.life = 0
                self.frame = 0
                self.image = self.sprites[0]

            self.image = self.sprites[1]
            self.image = pygame.transform.scale(self.image, (80, 40))
            self.image = pygame.transform.rotate(self.image, self.angle)
    
    def repair(self):
        self.image = self.sprites[0]
        self.life = 100
        self.image = pygame.transform.scale(self.image, (80, 40))
        self.image = pygame.transform.rotate(self.image, self.angle)