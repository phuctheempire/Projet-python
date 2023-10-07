import pygame as pg
import sys
from .world import World
from .settings import TILE_SIZE
from .utils import draw_text
from .camera import Camera

class Game:

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

        # Initialize the world
        self.world = World(50, 50, self.width, self.height) 
        
        # Initialize the camera
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
        self.screen.fill( (137, 207, 240)) #fill the screen with a color
        
        self.screen.blit(self.world.grass_tiles , (self.camera.scroll.x, self.camera.scroll.y)) #pg.surface to be self.world.grass_tiles, coordinates to be the movement of the camera

        for x in range(self.world.grid_length_x): # 10
            for y in range(self.world.grid_length_y): # 10

                # sq = self.world.world[x][y]["cart_rect"]
                # rect = pg.Rect(sq[0][0], sq[0][1], TILE_SIZE, TILE_SIZE)
                # pg.draw.rect(self.screen, (0, 0, 255), rect, 1)

                render_pos =  self.world.world[x][y]["render_pos"]
                #self.screen.blit(self.world.tiles["block"], (render_pos[0] + self.width/2, render_pos[1] + self.height/4))
                # the render position of the coordinate x, y of the world ( world is a dictionary)


                tile = self.world.world[x][y]["tile"]
                # call for random tile 
                if tile != "":
                    self.screen.blit(self.world.tiles[tile], # in the class World: self.tiles = self.load_images()
                                    (render_pos[0] + self.world.grass_tiles.get_width()/2 + self.camera.scroll.x,
                                     render_pos[1]  - (self.world.tiles[tile].get_height() - TILE_SIZE) + self.camera.scroll.y))
                    # draw the trees and the rocks following the camera movement and in the range of the map 

                # p = self.world.world[x][y]["iso_poly"]
                # p = [(x + self.width/2, y + self.height/4) for x, y in p]
                # pg.draw.polygon(self.screen, (255, 0, 0), p, 1)
        draw_text(
            self.screen,
            'fps={}'.format(round(self.clock.get_fps())),
            25,
            (0, 0, 0),
            (10, 10)
        )            

        pg.display.flip()



