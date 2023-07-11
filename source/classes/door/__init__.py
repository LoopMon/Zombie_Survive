import pygame


class Door(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('source/imgs/door.png')
        self.image = pygame.transform.scale(self.image, (128, 128))

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.planks = []
        self.max_planks = 3
        self.count_planks = self.max_planks

    def build_planks(self, planks: list):
        for plank in planks:
            self.planks.append(plank)

    def drawPlanks(self, canvas: pygame.Surface):
        for plank in self.planks:
            canvas.blit(plank.image, (plank.rect.x, plank.rect.y))