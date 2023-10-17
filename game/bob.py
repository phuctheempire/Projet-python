# define visual Bob:
import pygame as pg

class Bob:

    def __init__(self, tile, world):

        # Bob(self.world.world[5][5], self.world)
        self.world = world # become World class
        self.tile = tile 
        # == self.world.world[5][5]
        # self.world.world is a double list of dictionaries
        # self.world.world[5][5] is a dictionary >> self.tile is a dictionary
        #
        image = pg.image.load("assets/graphics/bob.png").convert_alpha()
        self.image = pg.transform.scale(image, (image.get_width()*1, image.get_height()*1))
        self.name = "bob"
        self.world.bob[tile["grid"][0]][tile["grid"][1]] = self # assign bob to the attribute bob in the world class
        # self.world.bob is a double list of dictionaries of NONE (innitially)
        # tiles are dictionaries
        # tiles["grid"] is a list of grid coordinates
        # tiles["grid"][0] is x coordinate
        # tiles["grid"][1] is y coordinate
        # self.world.bob[tile["grid"][0]][tile["grid"][1]] = self ( we assign a bob into this dictionary of none)
    #def color(self, image):
        

        

    


