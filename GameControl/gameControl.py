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
        self.grid : list[list['Tile']] = None
        self.nbBobs: 'int'= 0
        self.nbBobsSpawned = 0
        self.listBobs : list['Bob'] = []
        self.currentTick = 0
        self.currentDay = 0

    def setMap(self, map):
        self.grid = map
    def getMap(self):
        return self.grid
    def updateTick(self):
        self.currentTick += 1
    
    def spawnBobs(self, nbBobs):
        from Tiles.Bob.bob import Bob
        for _ in range(nbBobs):
            x = random.randint(0, GRID_LENGTH - 1)
            y = random.randint(0, GRID_LENGTH - 1)
            tile = self.getMap()[x][y]
            bob = Bob(random.randint(0, 1000))
            tile.addBob(bob)
            self.nbBobs += nbBobs
    
    

    # def updateNbBobs(self):
    #     for i in range(GRID_LENGTH):
    #         for j in range(GRID_LENGTH):
    #             listBob = self.grid[i][j].listBob
    #             if (listBob != []):
    #                 for x in listBob:
    #                     self.listBobs.append(x)
    #                     self.nbBobs += 1



    def getTick(self):
        return self.currentTick
    def getDay(self):
        return self.currentDay
    @staticmethod
    def getInstance():
        if GameControl.instance is None:
            GameControl.instance = GameControl()
        return GameControl.instance

    # def update():




