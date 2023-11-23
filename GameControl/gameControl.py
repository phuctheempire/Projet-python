import random
from GameControl.settings import *
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Tiles.Bob.bob import Bob
    from Tiles.Food import Food
    from Tiles.tiles import Tile


class GameControl:
    instance = None
    #initialisation of grids:
    def __init__(self):
        # raise Exception("This class is a singleton!")
        self.grid : list[list['Tile']] = None
        self.nbBobs: 'int'= 0
        self.nbBobsSpawned = 0
        self.listBobs : list['Bob'] = []
        self.currentTick = 0
        self.currentDay = 0
        # self.createWorld(GRID_LENGTH,GRID_LENGTH)
        # self.spawnBobs(10)
        self.renderTick = 0

    def setMap(self, map):
        self.grid = map
    def getMap(self):
        return self.grid
    def getFoodTiles(self) -> list['Tile']:
        foodTiles = []
        for row in self.getMap():
            for tile in row:
                if tile.getEnergy() > 0:
                    foodTiles.append(tile)
        return foodTiles
    def updateTick(self):
        self.currentTick += 1
    
    def spawnBobs(self, nbBobs):
        from Tiles.Bob.bob import Bob
        for _ in range(nbBobs):
            print("Adding bob")
            x = random.randint(0, GRID_LENGTH - 1)
            y = random.randint(0, GRID_LENGTH - 1)
            tile = self.getMap()[x][y]
            bob = Bob(random.randint(0, 1000))
            bob.spawn(tile)
            # bob.initiateNextTiles()
    

    def addBob(self, bob: 'Bob'):
        self.listBobs.append(bob)
        self.nbBobs += 1
        self.nbBobsSpawned += 1
    def removeBob(self, bob: 'Bob'):
        print("Removing bob:", bob.id)
        self.listBobs.remove(bob)
        self.nbBobs -= 1

    def createWorld(self, lengthX, lengthY ):
        from Tiles.tiles import Tile 
        world = []
        for i in range(lengthX):
                world.append([])
                for j in range(lengthY):
                    tile = Tile(gridX=i,gridY= j)
                    world[i].append(tile)
        self.setMap(world)
    
    def wipeFood(self):
        for row in self.getInstance().getMap():
            for tile in row:
                if tile.getEnergy() == FOOD_MAX_ENERGY:
                    tile.removeFood()
    def respawnFood(self):
        couples: list[tuple] = []
        for _ in range(NB_SPAWN_FOOD):
            x = random.randint(0,GRID_LENGTH-1)
            y = random.randint(0,GRID_LENGTH-1)
            while (x, y) in couples:
                x = random.randint(0,GRID_LENGTH-1)
                y = random.randint(0,GRID_LENGTH-1)
            self.getMap()[x][y].spawnFood()
            couples.append((x, y))
            

    def updateRenderTick(self):
        self.renderTick += 1
        if self.renderTick == FPS:
            self.renderTick = 0
            self.increaseTick()
        



    def increaseTick(self):
        # we must do something here
        i = 0
        bobs = self.listBobs
        while i < len(bobs):
            bob = bobs[i]
            bob.move()
            print("Length of bobs:", len(bobs))
            if bob not in bobs:
                pass
            else: i += 1
            

        self.currentTick += 1
        if self.currentTick == TICKS_PER_DAY:
            self.currentTick = 0
            self.increaseDay()
    def increaseDay(self):
        self.wipeFood()
        self.respawnFood()
        self.currentDay += 1
    
    def getRenderTick(self):
        return self.renderTick
    def getTick(self):
        return self.currentTick
    def getDay(self):
        return self.currentDay
    

    @staticmethod
    def getInstance():
        if GameControl.instance is None:
            if (GameControl.instance is not None):
                raise Exception("This class is a singleton!")
            GameControl.instance = GameControl()
        return GameControl.instance

    # def update():




