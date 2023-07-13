import pygame


class Door(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('source/imgs/door.png')
        self.image = pygame.transform.scale(self.image, (100, 128))

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.planks = []
        self.currentPlank = 0
        self.max_planks = 3
        self.count_planks = self.max_planks

    def build_planks(self, planks: list):
        for plank in planks:
            self.planks.append(plank)

    def drawPlanks(self, canvas: pygame.Surface):
        for plank in self.planks:
            if plank.visible:
                canvas.blit(plank.image, (plank.rect.x, plank.rect.y))
        
    def getPlank(self):
        if self.planks[self.currentPlank].life > 0:
            return self.currentPlank

        self.currentPlank += 1  
        if self.currentPlank >= len(self.planks):
            self.currentPlank = 0
            return self.currentPlank 

        return self.currentPlank 
    
    def checkPlanks(self):
        for plank in self.planks:
            plank.breakUp()
        
        