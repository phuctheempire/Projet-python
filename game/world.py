
import pygame as pg
import random
from .settings import TILE_SIZE



class World:
    #grid_length is the total length of the grid
    def __init__(self, grid_length_x, grid_length_y, width, height): #self.world = World(10, 10, self.width, self.height)
        self.grid_length_x = grid_length_x
        self.grid_length_y = grid_length_y
        self.width = width
        self.height = height
        self.bob = [[None for x in range(self.grid_length_x)] for y in range(self.grid_length_y)]
        #TODO générer des Bobs
        self.grass_tiles = pg.Surface((grid_length_x* TILE_SIZE * 2, grid_length_y * TILE_SIZE + 2 * TILE_SIZE)) #create a surface with the render area of the grids
        self.tiles = self.load_images() #dictionary of images
        self.world = self.create_world() #world to be a double list

    def create_world(self):
        world = []
        #grid_length: total length of the grid

        self.grass_tiles.fill(( 137, 207, 240)) #fill the surface with a color
        for grid_x in range(self.grid_length_x):
            world.append([]) # initiate an empty list then let grid_x run
            for grid_y in range(self.grid_length_y): #let grid_y run
                world_tile = self.grid_to_world(grid_x, grid_y) #create a dictionary
                world[grid_x].append(world_tile) #append the dictionary to the list

                render_pos = world_tile["render_pos"]  #get the render position of the tile
                r = random.randint(1, 100)
                if r > 40:
                    self.grass_tiles.blit(self.tiles["block"] , (render_pos[0] + self.grass_tiles.get_width()/2, render_pos[1] )) #blit(surface, coordinates) to draw the surface with the block image
                #draw the surface with the block image+
                else:
                    self.grass_tiles.blit(self.tiles["flower"] , (render_pos[0] + self.grass_tiles.get_width()/2, render_pos[1] ))
                    
        return world
    def draw(self, screen, camera):
        screen.blit(self.grass_tiles, (camera.scroll.x, camera.scroll.y))
        for x in range(self.grid_length_x): # 10
            for y in range(self.grid_length_y): # 10

                # sq = self.world.world[x][y]["cart_rect"]
                # rect = pg.Rect(sq[0][0], sq[0][1], TILE_SIZE, TILE_SIZE)
                # pg.draw.rect(self.screen, (0, 0, 255), rect, 1)

                render_pos =  self.world[x][y]["render_pos"]
                #self.screen.blit(self.world.tiles["block"], (render_pos[0] + self.width/2, render_pos[1] + self.height/4))
                # the render position of the coordinate x, y of the world ( world is a dictionary)


                tile = self.world[x][y]["tile"]
                # call for random tile 
                if tile != "":
                    screen.blit(self.tiles[tile], # in the class World: self.tiles = self.load_images()
                                    (render_pos[0] + self.grass_tiles.get_width()/2 + camera.scroll.x,
                                     render_pos[1]  - (self.tiles[tile].get_height() - TILE_SIZE) + camera.scroll.y))
                    # draw the trees and the rocks following the camera movement and in the range of the map 

                # p = self.world.world[x][y]["iso_poly"]
                # p = [(x + self.width/2, y + self.height/4) for x, y in p]
                # pg.draw.polygon(self.screen, (255, 0, 0), p, 1)
                bob = self.bob[x][y]
                if bob is not None:
                    screen.blit(bob.image,
                                    (render_pos[0] + self.grass_tiles.get_width()/2 + camera.scroll.x,
                                     render_pos[1] - (bob.image.get_height() - TILE_SIZE) + camera.scroll.y))
    def grid_to_world(self, grid_x, grid_y):

        rect = [
            (grid_x * TILE_SIZE, grid_y * TILE_SIZE),
            (grid_x * TILE_SIZE + TILE_SIZE, grid_y * TILE_SIZE),
            (grid_x * TILE_SIZE + TILE_SIZE, grid_y * TILE_SIZE + TILE_SIZE),
            (grid_x * TILE_SIZE, grid_y * TILE_SIZE + TILE_SIZE)
        ]

        #coordinate needed for creating a rectangle

        iso_poly = [self.cart_to_iso(x, y) for x, y in rect]

        #convert the coordinate of a rectangle to isometric coordinates

        minx = min([x for x, y in iso_poly])
        miny = min([y for x, y in iso_poly])

        #from there we can get the minimum x and y coordinates

        r = random.randint(1, 100)

        if r <= 5:
            tile = "tree"
        elif 5 < r <= 10:
            tile = "rock"
        else:
            tile = ""

        #randomly assign a tree (10%), rock (10%) or nothing (80%) to the tile

        out = {
            "grid": [grid_x, grid_y],
            "cart_rect": rect,
            "iso_poly": iso_poly,
            "render_pos": [minx, miny], #render position 
            "tile": tile
        }

        return out

    def cart_to_iso(self, x, y):
        iso_x = x - y
        iso_y = (x + y)/2
        return iso_x, iso_y

    def load_images(self):

        block = pg.image.load("assets/graphics/grass.png").convert_alpha()
        tree = pg.image.load("assets/graphics/tree.png").convert_alpha()
        rock = pg.image.load("assets/graphics/rock.png").convert_alpha()
        flower = pg.image.load("assets/graphics/flower.png").convert_alpha()

        return {"block": block, "tree": tree, "rock": rock, "flower": flower}


