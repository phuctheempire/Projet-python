import pygame as pg

from GameControl.game import Game

from GameControl.settings import *

class World:
    def __init__(self, width, height, ) -> None:
        # self.gameController = GameController.getInstance()
        self.width = width
        self.height = height
        # self.overlay.getInstance()
        self.surface = pg.Surface(SURFACE_WIDTH, SURFACE_HEIGHT).convert_alpha()

        # if not savedGame:
        #     self.loadMap()
        
        self.createStaticMap()
        
        def createStaticMap(self):
            for row in self.gameController.getMap(): # x is a list of a double list Map
                for tile in row: # tile is an object in list
                    # textureImg = tile.getTexture(tile.type)
                    (x, y) = tile.getRenderCoord()
                    offset = (x + self.surface.get_width()/2, y - textureImg.get_height() + TILE_SIZE)
                    # self.surface.blit(textureImg, offset)
