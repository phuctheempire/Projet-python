import pygame as pg
from typing import TYPE_CHECKING
from GameControl.gameControl import GameControl
from Tiles.tiles import Tile
from view.texture import *
from GameControl.settings import *
from view.camera import Camera
class World:
    def __init__(self, width, height ) -> None:
        self.gameController = GameControl.getInstance()
        self.width = width
        self.height = height

        self.surface = pg.Surface((SURFACE_WIDTH, SURFACE_HEIGHT)).convert_alpha()
        if ( GameControl.getInstance().getMap() != None):
            self.Map = GameControl.getInstance().getMap()
        else:
            self.createWorld(GRID_LENGTH,GRID_LENGTH)
        self.drawStaticMap()
        self.gameController.spawnBobs(10)
        self.drawBob(self.surface, Camera(self.width, self.height))


    def draw(self, screen, camera):
        screen.blit(self.surface, (camera.scroll.x, camera.scroll.y))

    def drawBob(self, screen, camera):
        for bob in self.gameController.listBobs:
            (x, y) = bob.getCurrentTile().getRenderCoord()
            offset = (x + self.surface.get_width()/2, y - (bob.getBobTexture().get_height() - TILE_SIZE ) + camera.scroll.y)
            screen.blit(bob.getBobTexture(), offset)

    def drawStaticMap(self):
        self.surface.fill(( 137, 207, 240))
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
                    tile = Tile(gridX=i,gridY= j)
                    world[i].append(tile)
        self.gameController.setMap(world)
        

