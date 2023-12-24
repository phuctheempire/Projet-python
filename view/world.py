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
        self.renderTick = 0
        self.surface = pg.Surface((SURFACE_WIDTH, SURFACE_HEIGHT)).convert_alpha()



    def draw(self, screen, camera):
        # self.drawBob(self.surface, Camera(self.width, self.height))
        self.drawStaticMap()
        self.drawFood(self.surface, Camera(self.width, self.height))
        self.drawBob(self.surface, Camera(self.width, self.height), self.gameController.renderTick)
        screen.blit(self.surface, (camera.scroll.x, camera.scroll.y))

    def drawBob(self, screen, camera, walkProgression ):
        for bob in self.gameController.listBobs:
            if bob not in self.gameController.diedQueue or self.gameController.newBornQueue:
                (x, y) = bob.getCurrentTile().getRenderCoord()
                (X, Y) = (x + self.surface.get_width()/2, y - (bob.getBobTexture().get_height() - TILE_SIZE ) + camera.scroll.y)
                position = (X, Y)
                # print(bob.getNextTile())
                (destX, destY) = bob.getNextTile().getRenderCoord()
                (desX, desY) = (destX + self.surface.get_width()/2, destY - ( + bob.getBobTexture().get_height() - TILE_SIZE ) + camera.scroll.y)
                # position1 = (X + (desX - X) * (2 *walkProgression/FPS), Y + (desY - Y) * (2* walkProgression/FPS))
                position2 = (X + (desX - X) * (2 *walkProgression/FPS -1), Y + (desY - Y) * (2* walkProgression/FPS -1))
                bar_width = int((bob.energy / bob.energyMax) * 50)
                if (walkProgression < FPS/2):
                    pg.draw.rect(screen, (255, 0, 0), (position[0], position[1] - 5, bar_width, 5))
                    screen.blit(bob.getBobTexture(), position)
                else:
                    pg.draw.rect(screen, (255, 0, 0), (position2[0], position2[1] - 5, bar_width, 5))
                    screen.blit(bob.getBobTexture(), position2)
        for bob in self.gameController.diedQueue:
            (x, y) = bob.getCurrentTile().getRenderCoord()
            (X, Y) = (x + self.surface.get_width()/2, y - (bob.getBobTexture().get_height() - TILE_SIZE ) + camera.scroll.y)
            position = (X, Y)
            # if walkProgression < FPS/2:
            screen.blit(bob.getBobTexture(), position) # need to change to dead bob texture later
  
        for bob in self.gameController.newBornQueue:
            if bob not in self.gameController.diedQueue:
                (x, y) = bob.getCurrentTile().getRenderCoord()
                (X, Y) = (x + self.surface.get_width()/2, y - (bob.getBobTexture().get_height() - TILE_SIZE ) + camera.scroll.y)
                (destX, destY) = bob.getNextTile().getRenderCoord()
                (desX, desY) = (destX + self.surface.get_width()/2, destY - ( + bob.getBobTexture().get_height() - TILE_SIZE ) + camera.scroll.y)
                position = (X, Y)
                position2 = (X + (desX - X) * (2 *walkProgression/FPS -1), Y + (desY - Y) * (2* walkProgression/FPS -1))
                if walkProgression < FPS/2:
                    screen.blit(bob.getBobTexture(), position) # need to change to newborn bob texture later
                    pg.draw.rect(screen, (255, 0, 0), (position[0], position[1] - 5, bar_width, 5))
                else:
                    screen.blit(bob.getBobTexture(), position2)
                    pg.draw.rect(screen, (255, 0, 0), (position2[0], position2[1] - 5, bar_width, 5))



    def drawFood(self, screen, camera):
        for food in self.gameController.getFoodTiles():
            (x, y) = food.getRenderCoord()
            (X, Y) = (x + self.surface.get_width()/2 , y - (food.getFoodImage().get_height() - TILE_SIZE ) + camera.scroll.y)
            position = (X, Y)
            bar_width = int((food.foodEnergy / FOOD_MAX_ENERGY) * 50)
            pg.draw.rect(screen, (0, 0, 255), (position[0] + 5, position[1]+ 20, bar_width, 5))
            screen.blit(food.getFoodImage(), position)


    def drawStaticMap(self):
        self.surface.fill(( 137, 207, 240))
        # for row in self.gameController.getMap(): # x is a list of a double list Map
        #     for tile in row: # tile is an object in list
        #         textureImg = tile.getGrassImage()
        #         (x, y) = tile.getRenderCoord()
        #         offset = (x + self.surface.get_width()/2, y)
        #         self.surface.blit(textureImg, offset)
        
    # def createWorld(self, lengthX, lengthY ):
    #     world = []
    #     for i in range(lengthX):
    #             world.append([])
    #             for j in range(lengthY):
    #                 tile = Tile(gridX=i,gridY= j)
    #                 world[i].append(tile)
    #     self.gameController.setMap(world)
        

