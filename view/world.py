import pygame as pg
from typing import TYPE_CHECKING
from GameControl.gameControl import GameControl
from Tiles.tiles import Tile
from view.texture import *
from GameControl.setting import Setting
from view.camera import Camera
import random
class World:
    def __init__(self, width, height ) -> None:
        self.setting = Setting.getSettings()
        self.gameController = GameControl.getInstance()
        self.width = width
        self.height = height
        self.renderTick = 0
        self.zoom : 'float' = self.width / self.setting.getSurfaceWidth()
        self.mapSurface = pg.Surface((self.setting.getSurfaceWidth(), self.setting.getSurfaceHeight())).convert_alpha()
        self.surface = pg.Surface((self.setting.getSurfaceWidth(), self.setting.getSurfaceHeight())).convert_alpha()
        self.newSf = pg.Surface((self.setting.getSurfaceWidth() * self.zoom, self.setting.getSurfaceHeight() * self.zoom)).convert_alpha()
        self.simuSf = pg.Surface((self.setting.getSurfaceWidth() * self.zoom, self.setting.getSurfaceHeight() * self.zoom)).convert_alpha()

        self.initSimuStaticMap(self.mapSurface, Camera(self.width, self.height))
        pg.transform.smoothscale(self.mapSurface, (self.setting.getSurfaceWidth() * self.zoom, self.setting.getSurfaceHeight() * self.zoom), self.newSf)

########################################## Draw a normal map ##########################################



    def draw(self, screen, camera):
        # self.drawBob(self.surface, Camera(self.width, self.height))
        # self.surface = pg.Surface((self.setting.getSurfaceWidth(), self.setting.getSurfaceHeight())).convert_alpha()
        self.drawStaticMap(self.surface, camera)
        # self.surface.fill((195, 177, 225))
        # self.surface.blit(self.mapSurface, (0,0))
        self.drawFood(self.surface, camera)
        self.drawBob(self.surface, camera, self.gameController.renderTick)
        # newSf = pg.Surface((self.setting.getSurfaceWidth() * self.zoom, self.setting.getSurfaceHeight() * self.zoom)).convert_alpha()
        # pg.transform.smoothscale_by(self.surface, self.zoom, newSf)
        # screen.blit(newSf, (camera.scroll.x, camera.scroll.y))
        screen.blit(self.surface, (camera.scroll.x, camera.scroll.y))

    def drawStaticMap(self, surface, camera):
        surface.fill((195, 177, 225))
        # surface.blit(loadMap(), (0,0))
        textureImg = loadGrassImage()
        flowImg = loadFlowerImage()
        for row in self.gameController.getMap(): # x is a list of a double list Map
            for tile in row: # tile is an object in list
                (x, y) = tile.getRenderCoord()
                offset = (x + self.surface.get_width()/2 , y + self.setting.getTileSize())
                a,b = offset
                if -64 <= (a + camera.scroll.x) <= 1920 and -64 <= (b + camera.scroll.y)  <= 1080:
                    if tile.flower:
                        surface.blit(flowImg, offset)
                    else:
                        surface.blit(textureImg, offset)
                else: pass
        # surface.blit(self.mapSurface, (0,0))

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
                    if ( walkProgression < self.setting.getFps()/2):
                        if nbInteval == 0:
                            (destX, destY) = bob.getCurrentTile().getRenderCoord()
                            (desX, desY) = (destX + self.surface.get_width()/2 , destY - ( + 50 - self.setting.getTileSize() ) )
                            finish = (desX, desY + self.setting.getTileSize())
                            a,b = finish
                            if -64 <= (a + camera.scroll.x) <= 1920 and -64 <= (b + camera.scroll.y)  <= 1080:
                                bar_width = int((bob.energy / bob.energyMax) * 50)
                                pg.draw.rect(surface, (255, 0, 0), (finish[0], finish[1] - 5, bar_width, 5))
                                if bob.isHunting:
                                    surface.blit(purpleLeft, finish)
                                else: surface.blit(greenLeft, finish)
                            else: pass
                        else:
                            for i in range( nbInteval):
                                if ( i*self.setting.getFps()) / (nbInteval * 2) <= walkProgression < (i+1)*self.setting.getFps() / (nbInteval * 2):
                                    (x, y) = bob.getPreviousTiles()[i].getRenderCoord()
                                    (X, Y) = (x + self.surface.get_width()/2 , y - (50 - self.setting.getTileSize() ) )
                                    (destX, destY) = bob.getPreviousTiles()[i+1].getRenderCoord()
                                    (desX, desY) = (destX + self.surface.get_width()/2 , destY - ( + 50 - self.setting.getTileSize() ) )
                                    pos = (X + (desX - X) * (walkProgression - (i*self.setting.getFps())/(2 * nbInteval)) * (2 * nbInteval) / self.setting.getFps() , Y + (desY - Y) * (walkProgression - (i*self.setting.getFps())/(2 * nbInteval) ) * (2 * nbInteval) / self.setting.getFps()  + self.setting.getTileSize()  )
                                    a,b = pos
                                    if -64 <= (a + camera.scroll.x) <= 1920 and -64 <= (b + camera.scroll.y)  <= 1080:
                                        bar_width = int((bob.energy / bob.energyMax) * 50)
                                        pg.draw.rect(surface, (255, 0, 0), (pos[0], pos[1] - 5, bar_width, 5))
                                        if bob.isHunting:
                                            surface.blit(purpleLeft, pos)
                                        else: surface.blit(greenLeft, pos)
                                    else: pass
                                else: pass
                    else:
                        (destX, destY) = bob.getCurrentTile().getRenderCoord()
                        (desX, desY) = (destX + self.surface.get_width()/2 , destY - ( + 50 - self.setting.getTileSize() ) )
                        finish = (desX, desY + self.setting.getTileSize())
                        a,b = finish
                        if -64 <= (a + camera.scroll.x) <= 1920 and -64 <= (b + camera.scroll.y)  <= 1080:
                            bar_width = int((bob.energy / bob.energyMax) * 50)
                            pg.draw.rect(surface, (255, 0, 0), (finish[0], finish[1] - 5, bar_width, 5))
                            if bob.isHunting:
                                surface.blit(purpleLeft, finish)
                            else: surface.blit(greenLeft, finish)
                        else: pass



        for bob in self.gameController.diedQueue:
            (x, y) = bob.getPreviousTile().getRenderCoord()
            (X, Y) = (x + self.surface.get_width()/2 , y - (50 - self.setting.getTileSize() ) )
            position = (X, Y)
            # print(bob.getNextTile())
            (destX, destY) = bob.getCurrentTile().getRenderCoord()
            (desX, desY) = (destX + self.surface.get_width()/2 , destY - ( + 50 - self.setting.getTileSize() ) )
            start = (X + (desX - X) * (2 *walkProgression/self.setting.getFps()), Y + (desY - Y) * (2* walkProgression/self.setting.getFps()) + self.setting.getTileSize())
            finish = (desX, desY + self.setting.getTileSize())
            a , b = finish
            if -64 <= (a + camera.scroll.x) <= 1920 and -64 <= (b + camera.scroll.y)  <= 1080:
                if (walkProgression < self.setting.getFps()/2):
                    surface.blit(greenLeft, start)
                elif self.setting.getFps()/2 <= walkProgression < self.setting.getFps()/2 + self.setting.getFps()/16:
                    surface.blit(bob.getExplodeTexture(1), finish)
                elif self.setting.getFps()/2 + self.setting.getFps()/16 <= walkProgression < self.setting.getFps()/2 + 2*self.setting.getFps()/16:
                    surface.blit(bob.getExplodeTexture(2), finish)
                elif self.setting.getFps()/2 + 2*self.setting.getFps()/16 <= walkProgression < self.setting.getFps()/2 + 3*self.setting.getFps()/16:
                    surface.blit(bob.getExplodeTexture(3), finish)
                elif self.setting.getFps()/2 + 3*self.setting.getFps()/16 <= walkProgression < self.setting.getFps()/2 + 4*self.setting.getFps()/16:
                    surface.blit(bob.getExplodeTexture(4), finish)
                elif self.setting.getFps()/2 + 4*self.setting.getFps()/16 <= walkProgression < self.setting.getFps()/2 + 5*self.setting.getFps()/16:
                    surface.blit(bob.getExplodeTexture(5), finish)
                elif self.setting.getFps()/2 + 5*self.setting.getFps()/16 <= walkProgression < self.setting.getFps()/2 + 6*self.setting.getFps()/16:
                    surface.blit(bob.getExplodeTexture(6), finish)
                elif self.setting.getFps()/2 + 6*self.setting.getFps()/16 <= walkProgression < self.setting.getFps()/2 + 7*self.setting.getFps()/16:
                    surface.blit(bob.getExplodeTexture(7), finish)
                else:
                    surface.blit(bob.getExplodeTexture(8), finish)
            else: pass
  
        for bob in self.gameController.newBornQueue:
            if bob not in self.gameController.diedQueue:
                # (x, y) = bob.getPreviousTile().getRenderCoord()
                # (X, Y) = (x + self.surface.get_width()/2 , y - (greenLeftt_height() - self.setting.getTileSize() ) )
                (destX, destY) = bob.getCurrentTile().getRenderCoord()
                (desX, desY) = (destX + self.surface.get_width()/2 , destY - ( + 50 - self.setting.getTileSize() ) )
                # position = (X, Y + self.setting.getTileSize())
                # start = (X + (desX - X) * (2 *walkProgression/self.setting.getFps()), Y + (desY - Y) * (2* walkProgression/self.setting.getFps()) + self.setting.getTileSize())
                finish = (desX, desY + self.setting.getTileSize())
                a,b = finish
                if -64 <= (a  + camera.scroll.x) <= 1920 and -64 <= (b  + camera.scroll.y)  <= 1080:
                    if walkProgression < self.setting.getFps()/2:
                        # screen.blit(greenLefttart) # need to change to newborn bob texture later
                        # pg.draw.rect(screen, (255, 0, 0), (start[0], start[1] - 5, bar_width, 5))
                        pass
                    # else:
                    #     screen.blit(greenLeftinish)
                    #     pg.draw.rect(screen, (255, 0, 0), (finish[0], finish[1] - 5, bar_width, 5))
                    elif self.setting.getFps()/2 <= walkProgression < self.setting.getFps()/2 + self.setting.getFps()/16:
                        surface.blit(bob.getSpawnTexture(1), finish)
                    elif self.setting.getFps()/2 + self.setting.getFps()/16 <= walkProgression < self.setting.getFps()/2 + 2*self.setting.getFps()/16:
                        surface.blit(bob.getSpawnTexture(2), finish)
                    elif self.setting.getFps()/2 + 2*self.setting.getFps()/16 <= walkProgression < self.setting.getFps()/2 + 3*self.setting.getFps()/16:
                        surface.blit(bob.getSpawnTexture(3), finish)
                    elif self.setting.getFps()/2 + 3*self.setting.getFps()/16 <= walkProgression < self.setting.getFps()/2 + 4*self.setting.getFps()/16:
                        surface.blit(bob.getSpawnTexture(4), finish)
                    elif self.setting.getFps()/2 + 4*self.setting.getFps()/16 <= walkProgression < self.setting.getFps()/2 + 5*self.setting.getFps()/16:
                        surface.blit(bob.getSpawnTexture(5), finish)
                    elif self.setting.getFps()/2 + 5*self.setting.getFps()/16 <= walkProgression < self.setting.getFps()/2 + 6*self.setting.getFps()/16:
                        surface.blit(bob.getSpawnTexture(6), finish)
                    elif self.setting.getFps()/2 + 6*self.setting.getFps()/16 <= walkProgression < self.setting.getFps()/2 + 7*self.setting.getFps()/16:
                        surface.blit(bob.getSpawnTexture(7), finish)
                    else:
                        surface.blit(bob.getSpawnTexture(8), finish)
                else: pass

    def drawFood(self, surface, camera):
        foodTexture = loadFoodImage()
        for food in self.gameController.getFoodTiles():
            (x, y) = food.getRenderCoord()
            (X, Y) = (x + self.surface.get_width()/2  , y - ( 50 - self.setting.getTileSize() ) )
            position = (X , Y + self.setting.getTileSize() )
            a,b = position
            if -64 <= (a + camera.scroll.x) <= 1920 and -64 <= (b + camera.scroll.y)  <= 1080:
                bar_width = int((food.foodEnergy / self.setting.getFoodEnergy()) * 50)
                pg.draw.rect(surface, (0, 0, 255), (position[0] + 5, position[1] - 5, bar_width, 5))
                surface.blit(foodTexture, position)
            else: pass

################################################### Simu Mode ###################################################

    def drawSimu(self, screen, camera):
        # self.initSimuStaticMap(self.surface, camera)
        # screen.blit(newSf, (0, (1080-( self.setting.getSurfaceHeight()*1920/self.setting.getSurfaceWidth()))/2))
        self.simuSf.fill((195, 177, 225))
        self.simuSf.blit(self.newSf, (0,0))
        self.drawSimuFood(self.simuSf, camera)
        self.drawSimuBob(self.simuSf, camera)
        screen.blit(self.simuSf, (0, (1080-( self.setting.getSurfaceHeight()*1920/self.setting.getSurfaceWidth()))/2))
        # screen.blit(self.surface, (camera.scroll.x, camera.scroll.y))


    def drawSimuBob(self,surface, camera):
        greenLeft = loadGreenLeft()
        greenRight = loadGreenRight()
        blueLeft = loadBlueLeft()
        blueRight = loadBlueRight()
        purpleLeft = loadPurpleLeft()
        purpleRight = loadPurpleRight()
        greenLeft = pg.transform.scale(greenLeft, (int(greenLeft.get_width() * self.zoom), int(greenLeft.get_height() * self.zoom)))
        greenRight = pg.transform.scale(greenRight, (int(greenRight.get_width() * self.zoom), int(greenRight.get_height() * self.zoom)))
        blueLeft = pg.transform.scale(blueLeft, (int(blueLeft.get_width() * self.zoom), int(blueLeft.get_height() * self.zoom)))
        blueRight = pg.transform.scale(blueRight, (int(blueRight.get_width() * self.zoom), int(blueRight.get_height() * self.zoom)))
        purpleLeft = pg.transform.scale(purpleLeft, (int(purpleLeft.get_width() * self.zoom), int(purpleLeft.get_height() * self.zoom)))
        purpleRight = pg.transform.scale(purpleRight, (int(purpleRight.get_width() * self.zoom), int(purpleRight.get_height() * self.zoom)))
        for bob in self.gameController.listBobs:
            (destX, destY) = bob.getCurrentTile().getRenderCoord()
            (desX, desY) = (destX + self.surface.get_width()/2 , destY - ( + 50 - self.setting.getTileSize() ) )
            finish = (desX, desY + self.setting.getTileSize())
            a,b = finish
            # bar_width = int((bob.energy / bob.energyMax) * 50)
            # pg.draw.rect(surface, (255, 0, 0), (finish[0], finish[1] - 5, bar_width, 5))
            if bob.isHunting:
                surface.blit(purpleLeft, (a*self.zoom, b*self.zoom))
            else: surface.blit(greenLeft, (a*self.zoom, b*self.zoom))


    def drawSimuFood(self, surface, camera):
        foodTexture = loadFoodImage()
        foodTexture = pg.transform.scale(foodTexture, (int(foodTexture.get_width() * self.zoom), int(foodTexture.get_height() * self.zoom)))
        for food in self.gameController.getFoodTiles():
            (x, y) = food.getRenderCoord()
            (X, Y) = (x + self.surface.get_width()/2  , y - (50 - self.setting.getTileSize() ) )
            position = (X , Y + self.setting.getTileSize() )
            a,b = position
            # bar_width = int((food.foodEnergy / self.setting.getFoodEnergy()) * 50)
            # pg.draw.rect(surface, (0, 0, 255), (position[0] + 5, position[1]+ 20, bar_width, 5))
            surface.blit(foodTexture, (a*self.zoom, b*self.zoom))



  
    def initSimuStaticMap(self, surface, camera):
        surface.fill((195, 177, 225))
        textureImg = loadGrassImage()
        flowImg = loadFlowerImage()
        for row in self.gameController.getMap(): # x is a list of a double list Map
            for tile in row: # tile is an object in list
                (x, y) = tile.getRenderCoord()
                offset = (x + self.surface.get_width()/2 , y + self.setting.getTileSize())
                a,b = offset
                if tile.flower:
                    surface.blit(flowImg, offset)
                else:
                    surface.blit(textureImg, offset)

##################################################################################################################################################

    # def drawPause(self, screen, camera):
    #     self.drawStaticPauseMap(self.surface, camera)
    #     self.drawPauseFood(self.surface, camera)
    #     self.drawPauseBob(self.surface, camera)