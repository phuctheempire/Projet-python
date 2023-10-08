# define visual Bob:
import pygame as pg

class Bob:

    def __init__(self, tile, world):
        self.world = world
        self.tile = tile
        image = pg.image.load("Map/assets/graphics/bob.png").convert_alpha()
        self.image = pg.transform.scale(image, (image.get_width()*2, image.get_height()*2))
        self.name = "bob"
        self.world.bob[tile["grid"][0]][tile["grid"][1]] = self

    


