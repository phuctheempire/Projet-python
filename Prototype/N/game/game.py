import pygame as pg
import sys
from .world import World
from .settings import TILE_SIZE
from .utils import draw_text
from .camera import Camera
from .bob import Bob
import random

class Game:

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

        # Initialize the world
        self.world = World(20, 20, self.width, self.height) 

        # Put the bobs in the world
        check = []
        # for _ in range(10):
        #     r = random.randint(0, 19)
        #     h = random.randint(0, 19)
        #     while (r, h) in check:
        #         r = random.randint(0, 19)
        #         h = random.randint(0, 19)
        #     check.append((r, h))
        #     Bob(self.world.world[r][h], self.world)
        Bob(self.world.world[5][5], self.world)
        
        # Initialize the camera
        self.camera = Camera(self.width, self.height)
        
        

    def run(self):
        self.playing = True
        while self.playing:
            # self.clock.tick(60)
            self.clock.tick(1)
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
        r = random.randint(0, 3)
        match r:
            case 0:
                self.world.updateGraphicBob(0,1);
            case 1:
                self.world.updateGraphicBob(1,0);
            case 2:
                self.world.updateGraphicBob(0,-1);
            case 3:
                self.world.updateGraphicBob(-1,0);
        self.camera.update()
        
        
    def draw(self):
        self.screen.fill((137, 207, 240))
        self.world.draw(self.screen, self.camera)
        
        # self.world = World(20, 20, self.width, self.height) 

        draw_text(
            self.screen,
            'fps={}'.format(round(self.clock.get_fps())),
            25,
            (255, 255, 255),
            (10, 10)
        )  

        pg.display.flip()



