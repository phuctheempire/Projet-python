from typing import TYPE_CHECKING
import pygame as pg
import random
from view.texture import *
from GameControl.gameControl import GameControl
from view.texture import Texture
# from TextureLib.grassTexture import GrassTexture
# from TextureLib.foodTexture import FoodTexture
from GameControl.settings import GRID_LENGTH, TILE_SIZE

if TYPE_CHECKING:
    from Tiles.Bob.bob import Bob
    from Tiles.Food.food import Food

class Tile:

    def __init__(self, gridX: int, gridY: int ):

        self.grassImg = loadGrassImage()["Grass"] if random.randint(0,1) == 0 else Texture.loadGrassImage()["Flower"]
        self.showTile = True
        self.gridX = gridX
        self.gridY = gridY
        
        self.listBob = list["Bob"]
        self.listFood = list["Food"]

        CartCoord = [(gridX*TILE_SIZE, gridY*TILE_SIZE), 
                     (gridX*TILE_SIZE + TILE_SIZE, gridY*TILE_SIZE), 
                     (gridX*TILE_SIZE + TILE_SIZE, gridY*TILE_SIZE + TILE_SIZE), 
                     (gridX*TILE_SIZE, gridY*TILE_SIZE + TILE_SIZE)]
        def CartToIso(x, y):
            return (x - y, (x + y) // 2)
        
        self.isoCoord = [CartToIso(x, y) for x, y in CartCoord]

        self.renderCoord = (min([x for x, y in self.isoCoord]), min([y for x, y in self.isoCoord]))

        # Setter and getter
        def getRenderCoord(self):
            return self.renderCoord
        def getIsoCoord(self):
            return self.isoCoord
        def getGameCoord(self):
            return (self.gridX, self.gridY)
        def distanceofTile(tile1: 'Tile', tile2:'Tile'):
            return abs(tile1.gridX - tile2.gridX) + abs(tile1.gridY - tile2.gridY)


        #Texture calling
        def getGrassTexture(self):
            return self.grassImg
        
        def addBob( self, bob: 'Bob'):
            self.listBob.append(bob)
        
        def removeBob(self, bob: 'Bob'):
            self.listBob.remove(bob)
        
        # // Need a function that return the list of tiles in a certain radius ( get vision tiles )

        def getNearbyTiles(self, radius) -> list['Tile']:
            from GameControl.gameControl import GameControl
            tempMap = GameControl.getInstance().getMap();
            tempCoord = []
            if radius == 0:
                tempCoord = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            else:
                tempCoord = [(x, y) for x in range(-radius, radius+1) for y in range(-radius, radius+1) if abs(x) + abs(y) <= radius] 

            for coord in tempCoord:
                try:
                    if self.x + coord[0] > GRID_LENGTH-1 or self.y + coord[1] > GRID_LENGTH-1 or self.x + coord[0] < 0 or self.y + coord[1] < 0:
                        continue
                    tempCoord.append(tempMap[self.x + coord[0]][self.y + coord[1]])
                except IndexError:
                    continue

            return tempCoord    

        # def getNearbyBobs(self, radius) -> list['Bob']:
            
        #     pass
        
        # def getNearbyFood(self, radius) -> list['Food']:
        #     pass 
        



    