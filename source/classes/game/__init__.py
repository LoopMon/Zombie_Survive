class Game:
    def __init__(self, doors: list):
        self.round = 1
        self.doors = doors
        self.roundZombies = 6
        self.zombies = []

    def countZombies(self):
        pass

    def nextRound(self):
        pass

    def updateZombies(self):
        for zombie in self.zombies:
            zombie.update()

    def spawnZombies(self, Zombie):
        for c, door in enumerate(self.doors):
            if c == 0:
                zombie = Zombie(door.rect.x-7, 320-80-128, 0)
            else:
                zombie = Zombie(door.rect.x+7, 320-80-128, 1)
            for i in range(0, int(self.roundZombies/2)):
                zombie.door = [door, c]
                self.zombies.append(zombie)

    def zombiesOut(self):
        for zombie in self.zombies:
            zombie.checkDoor()