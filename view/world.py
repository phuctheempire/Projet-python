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

    # def drawBob(self, screen, camera, walkProgression ):
    #     for bob in self.gameController.listBobs:
    #         if (bob not in self.gameController.diedQueue) and (bob not in self.gameController.newBornQueue):
    #             (x, y) = bob.getCurrentTile().getRenderCoord()
    #             (X, Y) = (x + self.surface.get_width()/2, y - (bob.getBobTexture().get_height() - TILE_SIZE ) + camera.scroll.y)
    #             position = (X, Y)
    #             # print(bob.getNextTile())
    #             (destX, destY) = bob.getNextTile().getRenderCoord()
    #             (desX, desY) = (destX + self.surface.get_width()/2, destY - ( + bob.getBobTexture().get_height() - TILE_SIZE ) + camera.scroll.y)
    #             # position1 = (X + (desX - X) * (2 *walkProgression/FPS), Y + (desY - Y) * (2* walkProgression/FPS))
    #             start = (X + (desX - X) * (2 *walkProgression/FPS -1), Y + (desY - Y) * (2*walkProgression/FPS -1))
    #             bar_width = int((bob.energy / bob.energyMax) * 50)
    #             if (walkProgression < FPS/2):
    #                 pg.draw.rect(screen, (255, 0, 0), (position[0], position[1] - 5, bar_width, 5))
    #                 screen.blit(bob.getBobTexture(), position)
    #             else:
    #                 pg.draw.rect(screen, (255, 0, 0), (start[0], start[1] - 5, bar_width, 5))
    #                 screen.blit(bob.getBobTexture(), start)

    #     for bob in self.gameController.diedQueue:
    #         (x, y) = bob.getCurrentTile().getRenderCoord()
    #         (X, Y) = (x + self.surface.get_width()/2, y - (bob.getBobTexture().get_height() - TILE_SIZE ) + camera.scroll.y)
    #         position = (X, Y)
    #         if walkProgression < FPS/8:
    #             screen.blit(bob.getExplodeTexture(1), position)
    #         elif FPS/8 <= walkProgression < FPS/4:
    #             screen.blit(bob.getExplodeTexture(2), position)
    #         elif FPS/4 <= walkProgression < 3*FPS/8:
    #             screen.blit(bob.getExplodeTexture(3), position)
    #         elif 3*FPS/8 <= walkProgression < FPS/2:
    #             screen.blit(bob.getExplodeTexture(4), position)
    #         elif FPS/2 <= walkProgression < 5*FPS/8:
    #             screen.blit(bob.getExplodeTexture(5), position)
    #         elif 5*FPS/8 <= walkProgression < 3*FPS/4:
    #             screen.blit(bob.getExplodeTexture(6), position)
    #         elif 3*FPS/4 <= walkProgression < 7*FPS/8:
    #             screen.blit(bob.getExplodeTexture(7), position)
    #         else:
    #             screen.blit(bob.getExplodeTexture(8), position)
  
    #     for bob in self.gameController.newBornQueue:
    #         if bob not in self.gameController.diedQueue:
    #             (x, y) = bob.getCurrentTile().getRenderCoord()
    #             (X, Y) = (x + self.surface.get_width()/2, y - (bob.getBobTexture().get_height() - TILE_SIZE ) + camera.scroll.y)
    #             (destX, destY) = bob.getNextTile().getRenderCoord()
    #             (desX, desY) = (destX + self.surface.get_width()/2, destY - ( + bob.getBobTexture().get_height() - TILE_SIZE ) + camera.scroll.y)
    #             position = (X, Y)
    #             start = (X + (desX - X) * (2 *walkProgression/FPS -1), Y + (desY - Y) * (2* walkProgression/FPS -1))
    #             if walkProgression < FPS/2:
    #                 screen.blit(bob.getBobTexture(), position) # need to change to newborn bob texture later
    #                 pg.draw.rect(screen, (255, 0, 0), (position[0], position[1] - 5, bar_width, 5))
    #             else:
    #                 screen.blit(bob.getBobTexture(), start)
    #                 pg.draw.rect(screen, (255, 0, 0), (start[0], start[1] - 5, bar_width, 5))


    # def drawBob(self, screen, camera, walkProgression ):
    #     for bob in self.gameController.listBobs:
    #         if (bob not in self.gameController.diedQueue) and (bob not in self.gameController.newBornQueue):
    #             (x, y) = bob.getPreviousTile().getRenderCoord()
    #             (X, Y) = (x + self.surface.get_width()/2, y - (bob.getBobTexture().get_height() - TILE_SIZE ) + camera.scroll.y)
    #             position = (X, Y)
    #             # print(bob.getNextTile())
    #             (destX, destY) = bob.getCurrentTile().getRenderCoord()
    #             (desX, desY) = (destX + self.surface.get_width()/2, destY - ( + bob.getBobTexture().get_height() - TILE_SIZE ) + camera.scroll.y)
    #             # position1 = (X + (desX - X) * (2 *walkProgression/FPS), Y + (desY - Y) * (2* walkProgression/FPS))
    #             start = (X + (desX - X) * (2 *walkProgression/FPS), Y + (desY - Y) * (2* walkProgression/FPS) + TILE_SIZE)
    #             finish = (desX, desY + TILE_SIZE)
    #             bar_width = int((bob.energy / bob.energyMax) * 50)
    #             if (walkProgression < FPS/2):
    #                 pg.draw.rect(screen, (255, 0, 0), (start[0], start[1] - 5, bar_width, 5))
    #                 screen.blit(bob.getBobTexture(), start)
    #             else:
    #                 pg.draw.rect(screen, (255, 0, 0), (finish[0], finish[1] - 5, bar_width, 5))
    #                 screen.blit(bob.getBobTexture(), finish)
    #     for bob in self.gameController.diedQueue:
    #         (x, y) = bob.getPreviousTile().getRenderCoord()
    #         (X, Y) = (x + self.surface.get_width()/2, y - (bob.getBobTexture().get_height() - TILE_SIZE ) + camera.scroll.y)
    #         position = (X, Y)
    #         # print(bob.getNextTile())
    #         (destX, destY) = bob.getCurrentTile().getRenderCoord()
    #         (desX, desY) = (destX + self.surface.get_width()/2, destY - ( + bob.getBobTexture().get_height() - TILE_SIZE ) + camera.scroll.y)
    #         start = (X + (desX - X) * (2 *walkProgression/FPS), Y + (desY - Y) * (2* walkProgression/FPS) + TILE_SIZE)
    #         finish = (desX, desY + TILE_SIZE)
    #         if (walkProgression < FPS/2):
    #             screen.blit(bob.getBobTexture(), start)
    #         elif FPS/2 <= walkProgression < FPS/2 + FPS/16:
    #             screen.blit(bob.getExplodeTexture(1), finish)
    #         elif FPS/2 + FPS/16 <= walkProgression < FPS/2 + 2*FPS/16:
    #             screen.blit(bob.getExplodeTexture(2), finish)
    #         elif FPS/2 + 2*FPS/16 <= walkProgression < FPS/2 + 3*FPS/16:
    #             screen.blit(bob.getExplodeTexture(3), finish)
    #         elif FPS/2 + 3*FPS/16 <= walkProgression < FPS/2 + 4*FPS/16:
    #             screen.blit(bob.getExplodeTexture(4), finish)
    #         elif FPS/2 + 4*FPS/16 <= walkProgression < FPS/2 + 5*FPS/16:
    #             screen.blit(bob.getExplodeTexture(5), finish)
    #         elif FPS/2 + 5*FPS/16 <= walkProgression < FPS/2 + 6*FPS/16:
    #             screen.blit(bob.getExplodeTexture(6), finish)
    #         elif FPS/2 + 6*FPS/16 <= walkProgression < FPS/2 + 7*FPS/16:
    #             screen.blit(bob.getExplodeTexture(7), finish)
    #         else:
    #             screen.blit(bob.getExplodeTexture(8), finish)
  
    #     for bob in self.gameController.newBornQueue:
    #         if bob not in self.gameController.diedQueue:
    #             (x, y) = bob.getPreviousTile().getRenderCoord()
    #             (X, Y) = (x + self.surface.get_width()/2, y - (bob.getBobTexture().get_height() - TILE_SIZE ) + camera.scroll.y)
    #             (destX, destY) = bob.getCurrentTile().getRenderCoord()
    #             (desX, desY) = (destX + self.surface.get_width()/2, destY - ( + bob.getBobTexture().get_height() - TILE_SIZE ) + camera.scroll.y)
    #             position = (X, Y + TILE_SIZE)
    #             start = (X + (desX - X) * (2 *walkProgression/FPS), Y + (desY - Y) * (2* walkProgression/FPS) + TILE_SIZE)
    #             finish = (desX, desY + TILE_SIZE)
    #             if walkProgression < FPS/2:
    #                 # screen.blit(bob.getBobTexture(), start) # need to change to newborn bob texture later
    #                 # pg.draw.rect(screen, (255, 0, 0), (start[0], start[1] - 5, bar_width, 5))
    #                 pass
    #             # else:
    #             #     screen.blit(bob.getBobTexture(), finish)
    #             #     pg.draw.rect(screen, (255, 0, 0), (finish[0], finish[1] - 5, bar_width, 5))
    #             elif FPS/2 <= walkProgression < FPS/2 + FPS/16:
    #                 screen.blit(bob.getSpawnTexture(1), finish)
    #             elif FPS/2 + FPS/16 <= walkProgression < FPS/2 + 2*FPS/16:
    #                 screen.blit(bob.getSpawnTexture(2), finish)
    #             elif FPS/2 + 2*FPS/16 <= walkProgression < FPS/2 + 3*FPS/16:
    #                 screen.blit(bob.getSpawnTexture(3), finish)
    #             elif FPS/2 + 3*FPS/16 <= walkProgression < FPS/2 + 4*FPS/16:
    #                 screen.blit(bob.getSpawnTexture(4), finish)
    #             elif FPS/2 + 4*FPS/16 <= walkProgression < FPS/2 + 5*FPS/16:
    #                 screen.blit(bob.getSpawnTexture(5), finish)
    #             elif FPS/2 + 5*FPS/16 <= walkProgression < FPS/2 + 6*FPS/16:
    #                 screen.blit(bob.getSpawnTexture(6), finish)
    #             elif FPS/2 + 6*FPS/16 <= walkProgression < FPS/2 + 7*FPS/16:
    #                 screen.blit(bob.getSpawnTexture(7), finish)
    #             else:
    #                 screen.blit(bob.getSpawnTexture(8), finish)

    def drawBob(self, screen, camera, walkProgression ):
        for bob in self.gameController.listBobs:
            if (bob not in self.gameController.diedQueue) and (bob not in self.gameController.newBornQueue):
                nbInteval = len(bob.getPreviousTiles()) - 1
                if ( walkProgression < FPS/2):
                    for i in range( nbInteval):
                        if ( i*FPS) / (nbInteval * 2) <= walkProgression < (i+1)*FPS / (nbInteval * 2):
                            (x, y) = bob.getPreviousTiles()[i].getRenderCoord()
                            (X, Y) = (x + self.surface.get_width()/2, y - (bob.getBobTexture().get_height() - TILE_SIZE ) + camera.scroll.y)
                            (destX, destY) = bob.getPreviousTiles()[i+1].getRenderCoord()
                            (desX, desY) = (destX + self.surface.get_width()/2, destY - ( + bob.getBobTexture().get_height() - TILE_SIZE ) + camera.scroll.y)
                            pos = (X + (desX - X) * (walkProgression - (i*FPS)/(2 * nbInteval)) * (2 * nbInteval) / FPS , Y + (desY - Y) * (walkProgression - (i*FPS)/(2 * nbInteval) ) * (2 * nbInteval) / FPS  + TILE_SIZE  )
                            bar_width = int((bob.energy / bob.energyMax) * 50)
                            pg.draw.rect(screen, (255, 0, 0), (pos[0], pos[1] - 5, bar_width, 5))
                            screen.blit(bob.getBobTexture(), pos)
                        else: pass
                else:
                    (destX, destY) = bob.getCurrentTile().getRenderCoord()
                    (desX, desY) = (destX + self.surface.get_width()/2, destY - ( + bob.getBobTexture().get_height() - TILE_SIZE ) + camera.scroll.y)
                    finish = (desX, desY + TILE_SIZE)
                    bar_width = int((bob.energy / bob.energyMax) * 50)
                    pg.draw.rect(screen, (255, 0, 0), (finish[0], finish[1] - 5, bar_width, 5))
                    screen.blit(bob.getBobTexture(), finish)

        for bob in self.gameController.diedQueue:
            (x, y) = bob.getPreviousTile().getRenderCoord()
            (X, Y) = (x + self.surface.get_width()/2, y - (bob.getBobTexture().get_height() - TILE_SIZE ) + camera.scroll.y)
            position = (X, Y)
            # print(bob.getNextTile())
            (destX, destY) = bob.getCurrentTile().getRenderCoord()
            (desX, desY) = (destX + self.surface.get_width()/2, destY - ( + bob.getBobTexture().get_height() - TILE_SIZE ) + camera.scroll.y)
            start = (X + (desX - X) * (2 *walkProgression/FPS), Y + (desY - Y) * (2* walkProgression/FPS) + TILE_SIZE)
            finish = (desX, desY + TILE_SIZE)
            if (walkProgression < FPS/2):
                screen.blit(bob.getBobTexture(), start)
            elif FPS/2 <= walkProgression < FPS/2 + FPS/16:
                screen.blit(bob.getExplodeTexture(1), finish)
            elif FPS/2 + FPS/16 <= walkProgression < FPS/2 + 2*FPS/16:
                screen.blit(bob.getExplodeTexture(2), finish)
            elif FPS/2 + 2*FPS/16 <= walkProgression < FPS/2 + 3*FPS/16:
                screen.blit(bob.getExplodeTexture(3), finish)
            elif FPS/2 + 3*FPS/16 <= walkProgression < FPS/2 + 4*FPS/16:
                screen.blit(bob.getExplodeTexture(4), finish)
            elif FPS/2 + 4*FPS/16 <= walkProgression < FPS/2 + 5*FPS/16:
                screen.blit(bob.getExplodeTexture(5), finish)
            elif FPS/2 + 5*FPS/16 <= walkProgression < FPS/2 + 6*FPS/16:
                screen.blit(bob.getExplodeTexture(6), finish)
            elif FPS/2 + 6*FPS/16 <= walkProgression < FPS/2 + 7*FPS/16:
                screen.blit(bob.getExplodeTexture(7), finish)
            else:
                screen.blit(bob.getExplodeTexture(8), finish)
  
        for bob in self.gameController.newBornQueue:
            if bob not in self.gameController.diedQueue:
                # (x, y) = bob.getPreviousTile().getRenderCoord()
                # (X, Y) = (x + self.surface.get_width()/2, y - (bob.getBobTexture().get_height() - TILE_SIZE ) + camera.scroll.y)
                (destX, destY) = bob.getCurrentTile().getRenderCoord()
                (desX, desY) = (destX + self.surface.get_width()/2, destY - ( + bob.getBobTexture().get_height() - TILE_SIZE ) + camera.scroll.y)
                # position = (X, Y + TILE_SIZE)
                # start = (X + (desX - X) * (2 *walkProgression/FPS), Y + (desY - Y) * (2* walkProgression/FPS) + TILE_SIZE)
                finish = (desX, desY + TILE_SIZE)
                if walkProgression < FPS/2:
                    # screen.blit(bob.getBobTexture(), start) # need to change to newborn bob texture later
                    # pg.draw.rect(screen, (255, 0, 0), (start[0], start[1] - 5, bar_width, 5))
                    pass
                # else:
                #     screen.blit(bob.getBobTexture(), finish)
                #     pg.draw.rect(screen, (255, 0, 0), (finish[0], finish[1] - 5, bar_width, 5))
                elif FPS/2 <= walkProgression < FPS/2 + FPS/16:
                    screen.blit(bob.getSpawnTexture(1), finish)
                elif FPS/2 + FPS/16 <= walkProgression < FPS/2 + 2*FPS/16:
                    screen.blit(bob.getSpawnTexture(2), finish)
                elif FPS/2 + 2*FPS/16 <= walkProgression < FPS/2 + 3*FPS/16:
                    screen.blit(bob.getSpawnTexture(3), finish)
                elif FPS/2 + 3*FPS/16 <= walkProgression < FPS/2 + 4*FPS/16:
                    screen.blit(bob.getSpawnTexture(4), finish)
                elif FPS/2 + 4*FPS/16 <= walkProgression < FPS/2 + 5*FPS/16:
                    screen.blit(bob.getSpawnTexture(5), finish)
                elif FPS/2 + 5*FPS/16 <= walkProgression < FPS/2 + 6*FPS/16:
                    screen.blit(bob.getSpawnTexture(6), finish)
                elif FPS/2 + 6*FPS/16 <= walkProgression < FPS/2 + 7*FPS/16:
                    screen.blit(bob.getSpawnTexture(7), finish)
                else:
                    screen.blit(bob.getSpawnTexture(8), finish)


    def drawFood(self, screen, camera):
        for food in self.gameController.getFoodTiles():
            (x, y) = food.getRenderCoord()
            (X, Y) = (x + self.surface.get_width()/2 , y - (food.getFoodImage().get_height() - TILE_SIZE ) + camera.scroll.y)
            position = (X , Y + TILE_SIZE )
            bar_width = int((food.foodEnergy / FOOD_MAX_ENERGY) * 50)
            pg.draw.rect(screen, (0, 0, 255), (position[0] + 5, position[1]+ 20, bar_width, 5))
            screen.blit(food.getFoodImage(), position)


    def drawStaticMap(self):
        self.surface.fill(( 0, 0, 0))
        for row in self.gameController.getMap(): # x is a list of a double list Map
            for tile in row: # tile is an object in list
                textureImg = tile.getGrassImage()
                (x, y) = tile.getRenderCoord()
                offset = (x + self.surface.get_width()/2, y + TILE_SIZE)
                self.surface.blit(textureImg, offset)
        
    # def createWorld(self, lengthX, lengthY ):
    #     world = []
    #     for i in range(lengthX):
    #             world.append([])
    #             for j in range(lengthY):
    #                 tile = Tile(gridX=i,gridY= j)
    #                 world[i].append(tile)
    #     self.gameController.setMap(world)
        

