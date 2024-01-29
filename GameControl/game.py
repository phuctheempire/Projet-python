from typing import TYPE_CHECKING
import pygame as pg
import sys
# from GameControl.gameControl import GameControl
# from GameControl.settings import *
from GameControl.setting import Setting
from view.utils import draw_text
from view.camera import Camera
from view.world import World
# from GameControl.settings import *
# import random
from GameControl.EventManager import *
from GameControl.gameControl import GameControl
from GameControl.saveAndLoad import *
from view.graph import *


class Game:

    def __init__(self, screen, clock):
        self.setting = Setting.getSettings()
        self.gameController = GameControl.getInstance()
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()
        # self.gameController.createWorld(self.setting.getGridLength(),self.setting.getGridLength()) 
        self.world = None
        self.camera = None

        # self.gameController.initiateBobs(self.setting.getNbBob())
        # # self.gameController.eatingTest()
        # self.gameController.respawnFood()
        # self.createNewGame()
        print("Game: ", self.setting.getGridLength(), self.setting.getNbBob(), self.setting.getFps(), self.setting.getTileSize()) 
    
    def createNewGame(self):
        self.gameController.initiateGame()
        self.gameController.createWorld(self.setting.getGridLength(),self.setting.getGridLength()) 
        self.world = World(self.width, self.height)
        self.camera = Camera(self.width, self.height) 
        self.gameController.initiateBobs(self.setting.getNbBob())
        # self.gameController.eatingTest()
        self.gameController.respawnFood()
    
    def loadGame(self, saveNumber):
        loadSetting(saveNumber)
        # print("GridTile:" , self.setting.getGridLength())
        self.gameController.initiateGame()
        self.gameController.createWorld(self.setting.getGridLength(),self.setting.getGridLength()) 
        loadGameController(saveNumber)
        self.world = World(self.width, self.height)
        self.camera = Camera(self.width, self.height) 
        # self.gameController.initiateBobs(self.setting.getNbBob())
        loadBob(saveNumber)
        loadFood(saveNumber) 



    
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(5*self.setting.getFps())
            self.events()
            self.update()
            # self.draw()
            if self.setting.simuMode:
                self.gameController.increaseTick()
                self.drawSimu() 
            else:
                self.gameController.updateRenderTick()
                self.draw()
            # else:
            #     self.clock.tick(5*self.setting.getFps())
            #     self.events()
            #     self.update()
            #     # self.draw()
            #     self.gameController.updateRenderTick()
            #     self.draw()
            


    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_g:
                    self.gameController.renderTick = 0
                    #graph methods
                    save_graph_data()
                    save_born_data()
                    save_died_data()
                    save_mass_data()
                    save_veloce_data()
                    save_vision_data()
                    save_energy_data()

                    show_graph_data()
                    show_born_data()
                    show_died_data()
                    show_mass_data()
                    show_veloce_data()
                    show_vision_data()
                    show_energy_data()
                    #graph methods
                if event.key == pg.K_m:
                    i = show_menu(self.screen, self.clock)
                    if i == 0:
                        print("i = ", i )
                        print("new game")
                        self.createNewGame()
                    elif i == 1:
                        print("i = ", i )
                        print("load game")
                        self.loadGame(1)
                    elif i == 2:
                        self.loadGame(2)
                    elif i == 3:
                        self.loadGame(3)
                    elif i == 4:
                        self.loadGame(4)
                    elif i == 5:
                        self.loadGame(5)

                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                if event.key == pg.K_BACKSPACE:
                    self.gameController.renderTick = 0
                    openIngamesetting()
                if event.key == pg.K_SPACE:
                    self.gameController.renderTick = 0
                    pause(self.screen,self.camera)
                if event.key == pg.K_1:
                    print("save")
                    saveGame(1)
                if event.key == pg.K_2:
                    print("save")
                    saveGame(2)
                if event.key == pg.K_3:
                    print("save")
                    saveGame(3)
                if event.key == pg.K_4:
                    print("save")
                    saveGame(4)
                if event.key == pg.K_5:
                    print("save")
                    saveGame(5)
                if event.key == pg.K_s:
                    self.gameController.renderTick = 0
                    self.setting.simuMode = not self.setting.simuMode

    def update(self):
        self.camera.update()
        
    def drawSimu(self):
        self.screen.fill((137, 207, 240))
        self.world.drawSimu(self.screen, self.camera)
        self.drawIndex()
        pg.display.flip()


    def draw(self):
        self.screen.fill((137, 207, 240))
        self.world.draw(self.screen, self.camera)
        self.drawIndex()
        pg.display.flip()

    def drawIndex( self ):
        draw_text(
            self.screen,
            'FPS: {}'.format(round(self.clock.get_fps())),
            25,
            (0,0,0),
            (10, 10)
        )  
        draw_text(
            self.screen,
            'Tick: {}'.format(round(self.gameController.getTick())),
            25,
            (0,0,0),
            (10, 30)
        )  
        draw_text(
            self.screen,
            'Day: {}'.format(round(self.gameController.getDay())),
            25,
            (0,0,0),
            (10, 50)
        )  
        draw_text(
            self.screen,
            'Number of bobs: {}'.format(self.gameController.getNbBobs()) ,
            25,
            (0,0,0),
            (10, 70)
        )
        draw_text(
            self.screen,
            'Number of bob spawned: {}'.format(self.gameController.getNbBobsSpawned()) ,
            25,
            (0,0,0),
            (10, 90)
        )



