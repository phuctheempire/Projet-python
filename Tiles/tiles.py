from typing import TYPE_CHECKING
import pygame as pg
import random
from view.texture import *
from GameControl.settings import *
from GameControl.gameControl import GameControl
if TYPE_CHECKING:
    from Tiles.Bob.bob import Bob

class Tile:

    def __init__(self, gridX: int, gridY: int ):
        self.gameController = GameControl.getInstance()
        self.foodEnergy = 0
        self.grassImg = loadGrassImage()["Grass"] if random.randint(0,1) == 0 else loadGrassImage()["Flower"]
        self.foodImg = loadFoodImage()["Food"]
        self.showTile = True
        self.gridX = gridX
        self.gridY = gridY
        self.listBob : list['Bob'] = []
        # self.listFood : list["Food"] = []

        CartCoord = [(gridX*TILE_SIZE, gridY*TILE_SIZE), 
                     (gridX*TILE_SIZE + TILE_SIZE, gridY*TILE_SIZE), 
                     (gridX*TILE_SIZE + TILE_SIZE, gridY*TILE_SIZE + TILE_SIZE), 
                     (gridX*TILE_SIZE, gridY*TILE_SIZE + TILE_SIZE)]

        def CartToIso(x, y):
            return (x - y, (x + y) / 2)
        self.isoCoord = [CartToIso(x, y) for x, y in CartCoord]

        self.renderCoord = (min([x for x, y in self.isoCoord]), min([y for x, y in self.isoCoord]))

    # Setter and getter
    def getRenderCoord(self):
        return self.renderCoord
    def getIsoCoord(self):
        return self.isoCoord
    def getGameCoord(self):
        return (self.gridX, self.gridY)
    def distanceofTile(tile1: 'Tile', tile2:'Tile') -> 'int':
        return abs(tile1.gridX - tile2.gridX) + abs(tile1.gridY - tile2.gridY)
    def CountofTile(tile: 'Tile', tile2 = 'Tile') -> ('int', 'int'):
        return (tile.gridX - tile2.gridX, tile.gridY - tile2.gridY)
    #Texture calling
    def getGrassImage(self):
        return self.grassImg
    def getFoodImage(self):
        return self.foodImg
    def getEnergy(self):
        return self.foodEnergy
    def getBobs(self):
        return self.listBob
    def addBob( self, bob: 'Bob'):
        self.listBob.append(bob)
        # bob.CurrentTile = self
        # bob.NextTile = bob.setNextTile()
        # print(bob.CurrentTile)
        # print(bob.getNextTile())
    
    def removeFood(self):
        self.foodEnergy = 0
    def spawnFood(self):
        self.foodEnergy += FOOD_MAX_ENERGY
    def removeBob(self, bob: 'Bob'):
        self.listBob.remove(bob)
    
    # // Need a function that return the list of tiles in a certain radius ( get vision tiles )
    def getDirectionTiles(self, orientation: int)-> list['Tile']:
        tempmap = GameControl.getInstance().getMap()
        coord = {
            "Up": tempmap[self.gridX][self.gridY+1] if self.gridY+1 < GRID_LENGTH else None,
            "Down": tempmap[self.gridX][self.gridY-1] if self.gridY-1 >= 0 else None,
            "Left": tempmap[self.gridX-1][self.gridY] if self.gridX-1 >= 0 else None,
            "Right": tempmap[self.gridX+1][self.gridY] if self.gridX+1 < GRID_LENGTH else None
        }
        return coord[orientation]

    def getNearbyTiles(self, radius) -> list['Tile']:
        from GameControl.gameControl import GameControl
        tempMap = GameControl.getInstance().getMap();
        tempCoord = []
        if radius == 0:
            tempCoord = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        else:
            tempCoord = [(x, y) for x in range(-radius, radius+1) for y in range(-radius, radius+1) if abs(x) + abs(y) <= radius] 
            # tempCoord = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        tempTiles = []
        for coord in tempCoord:
            try:
                if self.gridX + coord[0] > GRID_LENGTH-1 or self.gridY + coord[1] > GRID_LENGTH-1 or self.gridX + coord[0] < 0 or self.gridY + coord[1] < 0:
                    continue
                tempTiles.append(tempMap[self.gridX + coord[0]][self.gridY + coord[1]])
            except IndexError:
                continue

        return tempTiles    

    # def getNearbyBobs(self, radius) -> list['Bob']:
        
    #     pass
    
    # def getNearbyFood(self, radius) -> list['Food']:
    #     pass 
    



    