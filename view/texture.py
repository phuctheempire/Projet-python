# Texture templates: Author: Xuan Phuc
    # Import modules
    # Init templates
# Implementation et dévellopement: Émile Pétier

import pygame as pg

# Import libraries
from GameControl.settings import IMAGE_PATH
# import imgpath

def loadGrassImage():
    image = {
        "Grass": pg.image.load(IMAGE_PATH + "Grass.png").convert_alpha(),
        "Flower": pg.image.load(IMAGE_PATH + "Flower.png").convert_alpha(),
    }
    return image
