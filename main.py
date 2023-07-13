import pygame
from pygame.locals import *
from source.funcs import *
from source.classes.game import *
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

img = pygame.image.load('source/imgs/wall_window.png')
wall: pygame.Surface = resizeImg(img, (W, H-80))

left_door: Door = Door(58, H-80-128)

plank_1: Plank = Plank(left_door.rect.x - 5, left_door.rect.y - 10, 75)
plank_2: Plank = Plank(left_door.rect.x + 50, left_door.rect.y - 10, 285)
plank_3: Plank = Plank(left_door.rect.x + 5, left_door.rect.y + 5, 10)
left_door.build_planks([plank_1, plank_2, plank_3])

right_door: Door = Door(W - 152, H-80-128)

plank_1: Plank = Plank(right_door.rect.x - 5, right_door.rect.y - 10, 75)
plank_2: Plank = Plank(right_door.rect.x + 50, right_door.rect.y - 10, 285)
plank_3: Plank = Plank(right_door.rect.x + 5, right_door.rect.y + 5, 10)
right_door.build_planks([plank_1, plank_2, plank_3])

left_light: Light = Light(80, 0)
right_light: Light = Light(W - 160, 0)

box: Box = Box(W//2-72, floor.y-67)

group_sprites = pygame.sprite.Group()

game: Game = Game([left_door, right_door])
game.spawnZombies(Zombie)

group_sprites.add(left_door)
group_sprites.add(right_door)
group_sprites.add(left_light)
group_sprites.add(right_light)
group_sprites.add(box)

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

    for zombie in game.zombies:
        zombie.draw(canvas)

    group_sprites.draw(canvas)

    left_door.drawPlanks(canvas)
    right_door.drawPlanks(canvas)

    group_sprites.update()

    left_door.checkPlanks()

    right_door.checkPlanks()

    game.zombiesOut()
    game.updateZombies()

    for zombie in game.zombies:
        zombie.moveToPlayer()

    pygame.display.flip()

print('Fim do programa...')