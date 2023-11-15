from typing import TYPE_CHECKING
import pygame as pg

from view.texture import Texture
from ..TextureLib.grassTexture import GrassTexture
from ..TextureLib.foodTexture import FoodTexture
from GameControl.settings import GRID_LENGTH, TILE_SIZE

if TYPE_CHECKING:
    from Bob.bob import Bob
    from Food.food import Food

class Tile:
    def __init__(self, gridX: int, gridY: int, grass_type: GrassTexture = GrassTexture.GRASS ):
        self.grassType = grass_type
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
        


        #Texture calling
        def getTexture(self):
            return Texture.getTexture(self.grassType,)
        
        def addBob( self, bob: 'Bob'):
            self.listBob.append(bob)
        
        def removeBob(self, bob: 'Bob'):
            self.listBob.remove(bob)
        
        # // Need a function that return the list of tiles in a certain radius ( get vision tiles )

        def getNearbyBobs(self, radius) -> list['Bob']:
            pass
        
        def getNearbyFood(self, radius) -> list['Food']:
            pass 
        



    