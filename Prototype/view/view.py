import pygame as pg
# from .bob import CardiB
import random
from .settings import TILE_SIZE

class View:
    def __init__(self, lengthX, lengthY, width, height):
        self.lengthX = lengthX
        self.lengthY = lengthY
        self.width = width
        self.height = height
        self.map = self.createMap()
        self.pgCell = pg.Surface((lengthX* TILE_SIZE * 2, lengthY * TILE_SIZE + 2 * TILE_SIZE))
        self.images = self.load_images()
        self.drawMap()
        # pass
    
    def draw(self, screen, camera):
        screen.blit(self.pgCell, (camera.scroll.x, camera.scroll.y))

    def createMap(self):
        map = []
        for x in range(self.lengthX):
            map.append([])
            for y in range(self.lengthY):
                cell = self.cellStat(x, y)
                map[x].append(cell)
        return map
    
    def drawMap(self):
        self.pgCell.fill(( 137, 207, 240))
        for x in range(self.lengthX):
            for y in range(self.lengthY):
                render_position = self.map[x][y]["render_pos"]
                r = random.randint(1, 100)
                if r > 40:
                    self.pgCell.blit(self.images["block"] , (render_position[0] + self.pgCell.get_width()/2, render_position[1] )) #blit(surface, coordinates) to draw the surface with the block image
                #draw the surface with the block image+
                else:
                    self.pgCell.blit(self.images["flower"] , (render_position[0] + self.pgCell.get_width()/2, render_position[1] ))
                    

    def cart_to_iso(self, x, y):
        iso_x = x - y
        iso_y = (x + y)/2
        return iso_x, iso_y
    
    def cellStat(self, grid_x, grid_y):
        
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
        out = {
            "grid": [grid_x, grid_y],
            "cart_rect": rect,
            "iso_poly": iso_poly,
            "render_pos": [minx, miny], #render position 
            # "tile": tile
        }

        return out
    def load_images(self):

        block = pg.image.load("assets/graphics/grass.png").convert_alpha()
        flower = pg.image.load("assets/graphics/flower.png").convert_alpha()
        block = pg.transform.scale(block, (block.get_width()*0.5, block.get_height()*0.5))
        flower = pg.transform.scale(flower, (flower.get_width()*0.5, flower.get_height()*0.5))
        return {"block": block,  "flower": flower}