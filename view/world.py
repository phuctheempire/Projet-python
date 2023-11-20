import pygame as pg

from GameControl.gameControl import gameControl
from ..Model.tiles import Tile
from GameControl.settings import *
from ..view.camera import Camera
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
            self.createWorld(width, height)
        # self.createStaticMap()

    def draw(self, screen, camera):
        screen.blit(self.surface, Camera.scroll.x, Camera.scroll.y)

    def drawStaticMap(self):
        for row in self.gameController.getMap(): # x is a list of a double list Map
            for tile in row: # tile is an object in list
                textureImg = tile.getGrassImage()
                (x, y) = tile.getRenderCoord()
                offset = (x + self.surface.get_width()/2, y)
                self.surface.blit(textureImg, offset)
        
    def createWorld(self, lengthX, lengthY ):
        world = []
        for i in range(lengthX):
                world.append([])
                for j in range(lengthY):
                    world[i].append(Tile(i, j))
        self.gameController.setMap(world)
        

