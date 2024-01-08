import random
from GameControl.settings import *
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Tiles.Bob.bob import Bob
    # from Tiles.Food import Food
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
        self.listFoods: set['Tile'] = set()
        self.newBornQueue : list['Bob'] = []
        self.diedQueue: list['Bob'] = []
        self.currentTick = 0
        self.currentDay = 0
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

    def initiateBobs(self, nbBobs):
        from Tiles.Bob.bob import Bob
        for _ in range(nbBobs):
            print("Adding bob")
            x = random.randint(0, GRID_LENGTH - 1)
            y = random.randint(0, GRID_LENGTH - 1)
            tile = self.getMap()[x][y]
            bob = Bob()
            bob.spawn(tile)
        # self.pushToList()

    def eatingTest(self):
        from Tiles.Bob.bob import Bob
        x1 = random.randint(0, GRID_LENGTH - 1)
        y1 = random.randint(0, GRID_LENGTH - 1)
        tile1 = self.getMap()[x1][y1]
        bob1 = Bob()
        bob1.spawn(tile1)
        bob1.mass = 2
        bob1.velocity = 1.5
        x2 = random.randint(0, GRID_LENGTH - 1)
        y2 = random.randint(0, GRID_LENGTH - 1)
        tile2 = self.getMap()[x2][y2]
        bob2 = Bob()
        bob2.spawn(tile2)
        bob2.mass = 1
        bob2.velocity = 1
        x3 = random.randint(0, GRID_LENGTH - 1)
        y3 = random.randint(0, GRID_LENGTH - 1)
        tile3 = self.getMap()[x3][y3]
        bob3 = Bob()
        bob3.spawn(tile3)
        bob3.mass = 4
        bob3.velocity = 2
        # self.pushToList()


    def pushToList(self):
        for bob in self.newBornQueue:
            self.listBobs.append(bob)
            self.nbBobs += 1
            self.nbBobsSpawned += 1
        self.newBornQueue.clear()

    def addToNewBornQueue(self, bob: 'Bob'):
        self.newBornQueue.append(bob)
    def addToDiedQueue(self, bob: 'Bob'):
        self.diedQueue.append(bob)

    def wipeBobs(self):
        for bob in self.diedQueue:
            self.listBobs.remove(bob)
            self.nbBobs -= 1
        self.diedQueue.clear()

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
        # for row in self.getInstance().getMap():
        #     for tile in row:
        for tile in self.listFoods:
            # if tile.getEnergy() == FOOD_ENERGY:
            tile.removeFood()
        self.listFoods.clear()
    def respawnFood(self):
        # couples: list[tuple] = []
        for _ in range(NB_SPAWN_FOOD):
            x = random.randint(0,GRID_LENGTH-1)
            y = random.randint(0,GRID_LENGTH-1)
            # while (x, y) in couples:
            #     x = random.randint(0,GRID_LENGTH-1)
            #     y = random.randint(0,GRID_LENGTH-1)
            self.getMap()[x][y].spawnFood()
            self.listFoods.add(self.getMap()[x][y])
            # couples.append((x, y))

    def updateRenderTick(self):
        self.renderTick += 1
        if self.renderTick == FPS:
            self.renderTick = 0
            self.increaseTick()
        

    def increaseTick(self):
        self.pushToList()
        self.wipeBobs()
        self.listBobs.sort(key=lambda x: x.velocity, reverse=True)
        for bob in self.listBobs:
            bob.clearPreviousTiles()
        for bob in self.listBobs:
            if bob not in self.diedQueue:
                bob.action()
        # for bob in self.listBobs:
        #     if bob not in self.diedQueue:
                
        self.currentTick += 1
        if self.currentTick == TICKS_PER_DAY:
            self.currentTick = 0
            self.increaseDay()

        # At the end of the tick, we have listBob, newBornQueue, diedQueue
        
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
    def getDiedQueue(self):
        return self.diedQueue


    @staticmethod
    def getInstance():
        if GameControl.instance is None:
            if (GameControl.instance is not None):
                raise Exception("This class is a singleton!")
            GameControl.instance = GameControl()
        return GameControl.instance

    # def update():




