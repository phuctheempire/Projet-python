import pygame as pg
import sys
# from view.view import View
from GameControl.settings import *
from view.utils import draw_text
from view.camera import Camera
# from Model.logicMap import logicMap
from view.world import World
# import random
from .gameControl import gameControl


class Game:

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()
        # self.view = View(20, 20, self.width, self.height) 
        # self.logicMap = logicMap(20, 20)
        # self.view = View(self.logicMap, self.width,self.height)
        self.world = World(self.width, self.height)
        self
        self.camera = Camera(self.width, self.height)
        
    
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(60)
            self.events()
            self.update()
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
        # self.view.drawBob(self.screen,self.camera)
        draw_text(
            self.screen,
            'fps={}'.format(round(self.clock.get_fps())),
            25,
            (255, 255, 255),
            (10, 10)
        )  

        pg.display.flip()



