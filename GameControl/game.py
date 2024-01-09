from typing import TYPE_CHECKING
import pygame as pg
import sys
# from GameControl.gameControl import GameControl
from GameControl.settings import *
from view.utils import draw_text
from view.camera import Camera
from view.world import World
# from GameControl.settings import *
# import random

from GameControl.gameControl import GameControl


class Game:

    def __init__(self, screen, clock):

        self.gameController = GameControl.getInstance()
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()
        self.world = World(self.width, self.height)
        self.camera = Camera(self.width, self.height) 
        self.gameController.createWorld(GRID_LENGTH,GRID_LENGTH) 
        # self.gameController.initiateBobs(NB_BOB)
        self.gameController.eatingTest()
        self.gameController.respawnFood()
        
    
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(5*FPS)
            self.events()
            self.update()
            # self.draw()
            self.gameController.updateRenderTick()
            self.draw()
            


    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

    def update(self):
        self.camera.update()
        
        
    def draw(self):
        self.screen.fill((137, 207, 240))
        self.world.draw(self.screen, self.camera)
        draw_text(
            self.screen,
            'fps={}'.format(round(self.clock.get_fps())),
            25,
            (0,0,0),
            (10, 10)
        )  
        draw_text(
            self.screen,
            'gameTick={}'.format(round(self.gameController.getRenderTick())),
            25,
            (0,0,0),
            (10, 30)
        )  
        draw_text(
            self.screen,
            'Tick={}'.format(round(self.gameController.getTick())),
            25,
            (0,0,0),
            (10, 50)
        )  
        draw_text(
            self.screen,
            'Day={}'.format(round(self.gameController.getDay())),
            25,
            (0,0,0),
            (10, 70)
        )  
        draw_text(
            self.screen,
            'camera={}'.format([self.camera.scroll.x, self.camera.scroll.y]),
            25,
            (0,0,0),
            (10, 90)
        )

        pg.display.flip()
