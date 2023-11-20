import pygame as pg

from GameControl.gameControl import gameControl
from ..Model.tiles import Tile
from GameControl.settings import *

class World:
    def __init__(self, width, height ) -> None:
        self.gameController = gameControl.getInstance()
        self.width = width
        self.height = height
        # self.overlay.getInstance()
        self.surface = pg.Surface(SURFACE_WIDTH, SURFACE_HEIGHT).convert_alpha()
        if ( gameControl.getInstance().getMap() == None):
            self.Map = gameControl.getInstance().getMap()
        else:
            self.createWorld(GRID_LENGTH, GRID_LENGTH)
        # self.createStaticMap()


    def drawStaticMap(self):
        for row in self.gameController.getMap(): # x is a list of a double list Map
            for tile in row: # tile is an object in list
                textureImg = tile.getGrassImage()
                (x, y) = tile.getRenderCoord()
                offset = (x + self.surface.get_width()/2, y - textureImg.get_height() + TILE_SIZE)
                self.surface.blit(textureImg, offset)
        
    def createWorld(self, lengthX, lengthY ):
        world = []
        for i in range(lengthX):
                world.append([])
                for j in range(lengthY):
                    world[i].append(Tile(i, j))
        self.gameController.setMap(world)
        

