import pygame as pg
from typing import TYPE_CHECKING
from GameControl.gameControl import GameControl
from Tiles.tiles import Tile
from view.texture import *
from GameControl.settings import *
from view.camera import Camera
import random
class World:
    def __init__(self, width, height ) -> None:
        self.gameController = GameControl.getInstance()
        self.width = width
        self.height = height
        self.renderTick = 0
        self.surface = pg.Surface((SURFACE_WIDTH, SURFACE_HEIGHT)).convert_alpha()
        self.zoom : 'float' = 1



    def draw(self, screen, camera):
        # self.drawBob(self.surface, Camera(self.width, self.height))
        self.drawStaticMap(self.surface, camera)
        self.drawFood(self.surface, camera)
        self.drawBob(self.surface, camera, self.gameController.renderTick)
        # newSf = pg.Surface((SURFACE_WIDTH * self.zoom, SURFACE_HEIGHT * self.zoom)).convert_alpha()
        # pg.transform.smoothscale_by(self.surface, self.zoom, newSf)
        # screen.blit(newSf, (camera.scroll.x, camera.scroll.y))
        screen.blit(self.surface, (camera.scroll.x, camera.scroll.y))
        


    def drawBob(self, surface, camera, walkProgression ):
        greenLeft = loadGreenLeft()
        greenRight = loadGreenRight()
        blueLeft = loadBlueLeft()
        blueRight = loadBlueRight()
        purpleLeft = loadPurpleLeft()
        purpleRight = loadPurpleRight()
        
        for bob in self.gameController.listBobs:
            if (bob not in self.gameController.diedQueue) and (bob not in self.gameController.newBornQueue):
                # if(self.gameController.getTick() % 2 == 0 ):
                    nbInteval = len(bob.getPreviousTiles()) - 1
                    if ( walkProgression < FPS/2):
                        if nbInteval == 0:
                            (destX, destY) = bob.getCurrentTile().getRenderCoord()
                            (desX, desY) = (destX + self.surface.get_width()/2 , destY - ( + 50 - TILE_SIZE ) )
                            finish = (desX, desY + TILE_SIZE)
                            a,b = finish
                            if 0 <= (a * self.zoom + camera.scroll.x) <= 1920 and 0 <= (b * self.zoom + camera.scroll.y)  <= 1080:
                                bar_width = int((bob.energy / bob.energyMax) * 50)
                                pg.draw.rect(surface, (255, 0, 0), (finish[0], finish[1] - 5, bar_width, 5))
                                if bob.isHunting:
                                    surface.blit(purpleLeft, finish)
                                else: surface.blit(greenLeft, finish)
                            else: pass
                        else:
                            for i in range( nbInteval):
                                if ( i*FPS) / (nbInteval * 2) <= walkProgression < (i+1)*FPS / (nbInteval * 2):
                                    (x, y) = bob.getPreviousTiles()[i].getRenderCoord()
                                    (X, Y) = (x + self.surface.get_width()/2 , y - (50 - TILE_SIZE ) )
                                    (destX, destY) = bob.getPreviousTiles()[i+1].getRenderCoord()
                                    (desX, desY) = (destX + self.surface.get_width()/2 , destY - ( + 50 - TILE_SIZE ) )
                                    pos = (X + (desX - X) * (walkProgression - (i*FPS)/(2 * nbInteval)) * (2 * nbInteval) / FPS , Y + (desY - Y) * (walkProgression - (i*FPS)/(2 * nbInteval) ) * (2 * nbInteval) / FPS  + TILE_SIZE  )
                                    a,b = pos
                                    if 0 <= (a * self.zoom + camera.scroll.x) <= 1920 and 0 <= (b * self.zoom + camera.scroll.y)  <= 1080:
                                        bar_width = int((bob.energy / bob.energyMax) * 50)
                                        pg.draw.rect(surface, (255, 0, 0), (pos[0], pos[1] - 5, bar_width, 5))
                                        if bob.isHunting:
                                            surface.blit(purpleLeft, pos)
                                        else: surface.blit(greenLeft, pos)
                                    else: pass
                                else: pass
                    else:
                        (destX, destY) = bob.getCurrentTile().getRenderCoord()
                        (desX, desY) = (destX + self.surface.get_width()/2 , destY - ( + 50 - TILE_SIZE ) )
                        finish = (desX, desY + TILE_SIZE)
                        a,b = finish
                        if 0 <= (a * self.zoom + camera.scroll.x) <= 1920 and 0 <= (b * self.zoom + camera.scroll.y)  <= 1080:
                            bar_width = int((bob.energy / bob.energyMax) * 50)
                            pg.draw.rect(surface, (255, 0, 0), (finish[0], finish[1] - 5, bar_width, 5))
                            if bob.isHunting:
                                surface.blit(purpleLeft, finish)
                            else: surface.blit(greenLeft, finish)
                        else: pass



        for bob in self.gameController.diedQueue:
            (x, y) = bob.getPreviousTile().getRenderCoord()
            (X, Y) = (x + self.surface.get_width()/2 , y - (50 - TILE_SIZE ) )
            position = (X, Y)
            # print(bob.getNextTile())
            (destX, destY) = bob.getCurrentTile().getRenderCoord()
            (desX, desY) = (destX + self.surface.get_width()/2 , destY - ( + 50 - TILE_SIZE ) )
            start = (X + (desX - X) * (2 *walkProgression/FPS), Y + (desY - Y) * (2* walkProgression/FPS) + TILE_SIZE)
            finish = (desX, desY + TILE_SIZE)
            a , b = finish
            if 0 <= (a * self.zoom + camera.scroll.x) <= 1920 and 0 <= (b * self.zoom + camera.scroll.y)  <= 1080:
                if (walkProgression < FPS/2):
                    surface.blit(greenLeft, start)
                elif FPS/2 <= walkProgression < FPS/2 + FPS/16:
                    surface.blit(bob.getExplodeTexture(1), finish)
                elif FPS/2 + FPS/16 <= walkProgression < FPS/2 + 2*FPS/16:
                    surface.blit(bob.getExplodeTexture(2), finish)
                elif FPS/2 + 2*FPS/16 <= walkProgression < FPS/2 + 3*FPS/16:
                    surface.blit(bob.getExplodeTexture(3), finish)
                elif FPS/2 + 3*FPS/16 <= walkProgression < FPS/2 + 4*FPS/16:
                    surface.blit(bob.getExplodeTexture(4), finish)
                elif FPS/2 + 4*FPS/16 <= walkProgression < FPS/2 + 5*FPS/16:
                    surface.blit(bob.getExplodeTexture(5), finish)
                elif FPS/2 + 5*FPS/16 <= walkProgression < FPS/2 + 6*FPS/16:
                    surface.blit(bob.getExplodeTexture(6), finish)
                elif FPS/2 + 6*FPS/16 <= walkProgression < FPS/2 + 7*FPS/16:
                    surface.blit(bob.getExplodeTexture(7), finish)
                else:
                    surface.blit(bob.getExplodeTexture(8), finish)
            else: pass
  
        for bob in self.gameController.newBornQueue:
            if bob not in self.gameController.diedQueue:
                # (x, y) = bob.getPreviousTile().getRenderCoord()
                # (X, Y) = (x + self.surface.get_width()/2 , y - (greenLeftt_height() - TILE_SIZE ) )
                (destX, destY) = bob.getCurrentTile().getRenderCoord()
                (desX, desY) = (destX + self.surface.get_width()/2 , destY - ( + 50 - TILE_SIZE ) )
                # position = (X, Y + TILE_SIZE)
                # start = (X + (desX - X) * (2 *walkProgression/FPS), Y + (desY - Y) * (2* walkProgression/FPS) + TILE_SIZE)
                finish = (desX, desY + TILE_SIZE)
                a,b = finish
                if 0 <= (a * self.zoom + camera.scroll.x) <= 1920 and 0 <= (b * self.zoom + camera.scroll.y)  <= 1080:
                    if walkProgression < FPS/2:
                        # screen.blit(greenLefttart) # need to change to newborn bob texture later
                        # pg.draw.rect(screen, (255, 0, 0), (start[0], start[1] - 5, bar_width, 5))
                        pass
                    # else:
                    #     screen.blit(greenLeftinish)
                    #     pg.draw.rect(screen, (255, 0, 0), (finish[0], finish[1] - 5, bar_width, 5))
                    elif FPS/2 <= walkProgression < FPS/2 + FPS/16:
                        surface.blit(bob.getSpawnTexture(1), finish)
                    elif FPS/2 + FPS/16 <= walkProgression < FPS/2 + 2*FPS/16:
                        surface.blit(bob.getSpawnTexture(2), finish)
                    elif FPS/2 + 2*FPS/16 <= walkProgression < FPS/2 + 3*FPS/16:
                        surface.blit(bob.getSpawnTexture(3), finish)
                    elif FPS/2 + 3*FPS/16 <= walkProgression < FPS/2 + 4*FPS/16:
                        surface.blit(bob.getSpawnTexture(4), finish)
                    elif FPS/2 + 4*FPS/16 <= walkProgression < FPS/2 + 5*FPS/16:
                        surface.blit(bob.getSpawnTexture(5), finish)
                    elif FPS/2 + 5*FPS/16 <= walkProgression < FPS/2 + 6*FPS/16:
                        surface.blit(bob.getSpawnTexture(6), finish)
                    elif FPS/2 + 6*FPS/16 <= walkProgression < FPS/2 + 7*FPS/16:
                        surface.blit(bob.getSpawnTexture(7), finish)
                    else:
                        surface.blit(bob.getSpawnTexture(8), finish)
                else: pass


    def drawFood(self, surface, camera):
        foodTexture = loadFoodImage()
        for food in self.gameController.getFoodTiles():
            (x, y) = food.getRenderCoord()
            (X, Y) = (x + self.surface.get_width()/2  , y - (foodTexture.get_height() - TILE_SIZE ) )
            position = (X , Y + TILE_SIZE )
            a,b = position
            if 0 <= (a * self.zoom + camera.scroll.x) <= 1920 and 0 <= (b * self.zoom + camera.scroll.y)  <= 1080:
                bar_width = int((food.foodEnergy / FOOD_ENERGY) * 50)
                pg.draw.rect(surface, (0, 0, 255), (position[0] + 5, position[1]+ 20, bar_width, 5))
                surface.blit(foodTexture, position)
            else: pass


    def drawStaticMap(self, surface, camera):
        surface.fill((195, 177, 225))
        # surface.blit(loadMap(), (0,0))
        textureImg = loadGrassImage()
        for row in self.gameController.getMap(): # x is a list of a double list Map
            for tile in row: # tile is an object in list
                (x, y) = tile.getRenderCoord()
                offset = (x + self.surface.get_width()/2 , y + TILE_SIZE)
                a,b = offset
                if 0 <= (a * self.zoom + camera.scroll.x) <= 1920 and 0 <= (b * self.zoom + camera.scroll.y)  <= 1080:
                    surface.blit(textureImg, offset)
                else: pass
  