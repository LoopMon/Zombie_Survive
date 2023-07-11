import pygame
from random import randint


class Floor:
    def __init__(self, x: int, y: int, start: int, end: int):
        self.img = pygame.image.load('source/imgs/floor.png')
        self.images = []
        self.scale = 80
        self.x = x
        self.y = y
        self.start = start
        self.end = end

        self.createFloor()
        self.resizeFloor()
        
    def createFloor(self):
        for i in range(self.start, self.end):
            if i % 5 == 0:
                posY = randint(1, 2)
                rect = pygame.Rect(0, posY*32, 32, 32)
                img = self.img.subsurface(rect)
                self.images.append(img)
            else:
                rect = pygame.Rect(0, 0, 32, 32)
                img = self.img.subsurface(rect)
                self.images.append(img)

    def resizeFloor(self):
        for i in range(0, len(self.images)):
            img = self.images[i]
            self.images[i] = pygame.transform.scale(img, (self.scale, self.scale))
            
    def drawFloor(self, canvas):
        for count, floor in enumerate(self.images):
            canvas.blit(floor, (count * self.scale, self.y))