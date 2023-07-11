import pygame


class Box(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)

        self.sprites = [
            pygame.image.load('source/imgs/Box/box1.png'),
            [
                pygame.image.load('source/imgs/Box/box2.png'),
                pygame.image.load('source/imgs/Box/box3.png')
            ]
        ]
        self.image = self.sprites[0]
        self.image = pygame.transform.scale(self.image, (144, 80))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.open = False
        self.frame = 0

    def update(self):
        if self.open:
            self.frame += 0.1
            if self.frame >= len(self.sprites[1]):
                self.frame = 0
            
            self.image = self.sprites[1][int(self.frame)]
            self.image = pygame.transform.scale(self.image, (144, 80))
        
    def showGuns(self):
        pass
