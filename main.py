import pygame
from pygame.locals import *
from source.funcs import *
from source.classes.floor import *
from source.classes.light import *
from source.classes.door import *
from source.classes.plank import *
from source.classes.box import *
from source.classes.zombie import *


W: int = 1040 # 13 * 8
H: int = 320  #  4 * 8

clock: pygame.time.Clock = pygame.time.Clock()
tick: int = 60

canvas: pygame.Surface = pygame.display.set_mode((W, H))
pygame.display.set_caption('Zombie Survive')

floor: Floor = Floor(0, H-80, 0, 13)

img = pygame.image.load('source/imgs/wall.png')
wall: pygame.Surface = resizeImg(img, (W, H-80))

left_door: Door = Door(40, H-80-128)
left_door_bg: pygame.Rect = pygame.Rect(left_door.rect.x + 20, left_door.rect.y, 90, 100)

plank_1: Plank = Plank(left_door.rect.x + 10, left_door.rect.y - 10, 75)
plank_2: Plank = Plank(left_door.rect.x + 60, left_door.rect.y - 10, 285)
plank_3: Plank = Plank(left_door.rect.x + 20, left_door.rect.y + 5, 10)
left_door.build_planks([plank_1, plank_2, plank_3])

right_door: Door = Door(W - 180, H-80-128)
right_door_bg: pygame.Rect = pygame.Rect(right_door.rect.x + 20, right_door.rect.y, 90, 100)

plank_1: Plank = Plank(right_door.rect.x + 10, right_door.rect.y - 10, 75)
plank_2: Plank = Plank(right_door.rect.x + 60, right_door.rect.y - 10, 285)
plank_3: Plank = Plank(right_door.rect.x + 20, right_door.rect.y + 5, 10)
right_door.build_planks([plank_1, plank_2, plank_3])

left_light: Light = Light(80, 0)
right_light: Light = Light(W - 160, 0)

box: Box = Box(W//2-72, floor.y-75)

zombie: Zombie = Zombie(200, floor.y - 80)

group_sprites = pygame.sprite.Group()

group_sprites.add(left_door)
group_sprites.add(right_door)
group_sprites.add(left_light)
group_sprites.add(right_light)
group_sprites.add(box)
group_sprites.add(zombie)

done: bool = False
while not done:
    clock.tick(tick)
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                done = True

    floor.drawFloor(canvas)
    canvas.blit(wall, (0, 0))

    pygame.draw.rect(canvas, ('black'), left_door_bg)
    pygame.draw.rect(canvas, ('black'), right_door_bg)

    group_sprites.draw(canvas)

    left_door.drawPlanks(canvas)
    right_door.drawPlanks(canvas)

    group_sprites.update()

    pygame.display.flip()

print('Fim do programa...')

# https://github.com/LoopMon/Zombie_Survive.git