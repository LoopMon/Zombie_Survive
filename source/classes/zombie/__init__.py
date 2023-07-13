import pygame
from random import choice


class Zombie(pygame.sprite.Sprite):
    id: int = 0
    def __init__(self, x: int, y: int, direction: int):
        pygame.sprite.Sprite.__init__(self)

        self.id += 1
        self.zombieColors = ['Blue', 'Gray']
        self.color = choice(self.zombieColors)
        self.direction = direction

        self.sprites = [
            [pygame.image.load(f'source/imgs/Zombies/Blue/Attack_new/zombie{i}.png') for i in range(1, 4)],
            [pygame.image.load(f'source/imgs/Zombies/{self.color}/Running/zombie{i}.png') for i in range(1, 7)],
            [pygame.image.load(f'source/imgs/Zombies/{self.color}/Spawn/zombie{i}.png') for i in range(1, 8)],
            [pygame.image.load(f'source/imgs/Zombies/{self.color}/Stand/zombie{i}.png') for i in range(1, 5)],
        ]

        self.frame = 0
        self.state = 3
        self.image = self.sprites[self.state][self.frame]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.damage = 40
        self.place = 0
        self.onFloor = False
        self.door = None

    def update(self):
        self.frame += 0.05

        if self.place == 0 and self.frame >= len(self.sprites[self.state]):
            self.frame = 0
            self.breakPlank()   

        if self.place == 1 and self.frame >= len(self.sprites[self.state]):
            self.frame = 0
            self.onFloor = True
            self.state = 3

        if self.direction == 0:
            self.image = self.sprites[self.state][int(self.frame)] 
            if self.state == 0:
                self.image = pygame.transform.scale(self.image, (110, 128))    
            else:
                self.image = pygame.transform.scale(self.image, (128, 128))
        else:
            self.image = self.sprites[self.state][int(self.frame)] 
            if self.state == 0:
                self.image = pygame.transform.scale(self.image, (110, 128))    
            else:
                self.image = pygame.transform.scale(self.image, (128, 128))
            self.image = pygame.transform.flip(self.image, True, False)

    def draw(self, canvas):
        canvas.blit(self.image, self.rect)

    def breakPlank(self):
        self.rect.topleft = (self.door[0].rect.x, self.door[0].rect.y)
        self.state = 0 #attack
        indice = self.door[0].getPlank()
        self.door[0].planks[indice].life -= self.damage

    def checkDoor(self):
        count = 0
        for planks in self.door[0].planks:
            if not planks.visible:
                count += 1

        if count == len(self.door[0].planks) and self.place == 0:
            count = 0
            self.state = 2
            self.place = 1
            if self.door[1] == 0:
                print(self.door[1])
                self.rect.topleft = (
                    self.door[0].rect.right - 15, self.door[0].rect.top + 40
                )
            else:
                print(self.door[1])
                self.rect.topright = (
                    self.door[0].rect.left - self.rect.w - 50, self.door[0].rect.top + 40
                )
            
    def moveToPlayer(self):
        if self.place == 1 and self.onFloor:
            if self.direction == 0:
                self.state = 1
                self.rect.move_ip(1, 0)
            else:
                self.state = 1
                self.rect.move_ip(-1, 0)