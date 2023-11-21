# Texture templates: Author: Xuan Phuc
    # Import modules
    # Init templates
# Implementation et dévellopement: Émile Pétier

import pygame as pg

# Import libraries
from GameControl.settings import IMAGE_PATH
# import imgpath

def loadGrassImage():
    grass =pg.image.load(IMAGE_PATH + "grass.png").convert_alpha()
    grass = pg.transform.scale(grass, (grass.get_width()*0.5, grass.get_height()*0.5))
    flower = pg.image.load(IMAGE_PATH + "flower.png").convert_alpha()
    flower = pg.transform.scale(flower, (flower.get_width()*0.5, flower.get_height()*0.5))
    image = {
        "Grass": grass,
        "Flower": flower,
    }
    return image
def loadBobImage():
    bob = pg.image.load(IMAGE_PATH + "bob.png").convert_alpha()
    bob = pg.transform.scale(bob, (bob.get_width()*1, bob.get_height()*1))
    image = {
        "Bob": bob
    }
    return image

