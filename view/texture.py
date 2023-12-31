# Texture templates: Author: Xuan Phuc
    # Import modules
    # Init templates
# Implementation et dévellopement: Émile Pétier

import pygame as pg

# Import libraries
# from GameControl.settings import IMAGE_PATH
from GameControl.settings import *
# import imgpath

def loadGrassImage():
    grass =pg.image.load(IMAGE_PATH + "grass.png").convert_alpha()
    grass = pg.transform.scale(grass, (grass.get_width()*0.5, grass.get_height()*0.5))
    return grass

def loadFlowerImage():
    flower = pg.image.load(IMAGE_PATH + "flower.png").convert_alpha()
    flower = pg.transform.scale(flower, (flower.get_width()*0.5, flower.get_height()*0.5))
    return flower

# def loadBobImage():
#     bob = pg.image.load(IMAGE_PATH + "bob.png").convert_alpha()
#     bob = pg.transform.scale(bob, (bob.get_width()*1, bob.get_height()*1))
#     image = {
#         "Bob": bob
#     }
#     return image
def loadMap():
    map = pg.image.load(IMAGE_PATH + "map.jpeg").convert_alpha()
    map = pg.transform.scale(map, (SURFACE_WIDTH, SURFACE_HEIGHT))
    return map

def loadPurpleRight():
    purpleRight = pg.image.load(IMAGE_PATH + "Purple1.png").convert_alpha()
    # purpleRight = pg.transform.scale(purpleRight, (purpleRight.get_width()*1, purpleRight.get_height()*1))
    return purpleRight
def loadPurpleLeft():
    purpleLeft = pg.image.load(IMAGE_PATH + "Purple.png").convert_alpha()
    # purpleLeft = pg.transform.scale(purpleLeft, (purpleLeft.get_width()*1, purpleLeft.get_height()*1))
    return purpleLeft
def loadGreenRight():
    greenRight = pg.image.load(IMAGE_PATH + "Green1.png").convert_alpha()
    # greenRight = pg.transform.scale(greenRight, (greenRight.get_width()*1, greenRight.get_height()*1))
    return greenRight
def loadGreenLeft():
    greenLeft = pg.image.load(IMAGE_PATH + "Green.png").convert_alpha()
    # greenLeft = pg.transform.scale(greenLeft, (greenLeft.get_width()*1, greenLeft.get_height()*1))
    return greenLeft
def loadBlueRight():
    blueRight = pg.image.load(IMAGE_PATH + "Blue1.png").convert_alpha()
    # blueRight = pg.transform.scale(blueRight, (blueRight.get_width()*1, blueRight.get_height()*1))
    return blueRight
def loadBlueLeft():
    blueLeft = pg.image.load(IMAGE_PATH + "Blue.png").convert_alpha()
    # blueLeft = pg.transform.scale(blueLeft, (blueLeft.get_width()*1, blueLeft.get_height()*1))
    return blueLeft

def loadFoodImage():
    food = pg.image.load(IMAGE_PATH + "food.png").convert_alpha()
    food = pg.transform.scale(food, (food.get_width()*0.25, food.get_height()*0.25))
    return food

def loadExplosionImage():
    explosion1 = pg.image.load(IMAGE_PATH + "Ex1.png").convert_alpha()
    # explosion1 = pg.transform.scale(explosion1, (explosion1.get_width()*1, explosion1.get_height()*1))
    explosion2 = pg.image.load(IMAGE_PATH + "Ex2.png").convert_alpha()
    # explosion2 = pg.transform.scale(explosion2, (explosion2.get_width()*1, explosion2.get_height()*1))
    explosion3 = pg.image.load(IMAGE_PATH + "Ex3.png").convert_alpha()
    # explosion3 = pg.transform.scale(explosion3, (explosion3.get_width()*1, explosion3.get_height()*1))
    explosion4 = pg.image.load(IMAGE_PATH + "Ex4.png").convert_alpha()
    # explosion4 = pg.transform.scale(explosion4, (explosion4.get_width()*1, explosion4.get_height()*1))
    explosion5 = pg.image.load(IMAGE_PATH + "Ex5.png").convert_alpha()
    # explosion5 = pg.transform.scale(explosion5, (explosion5.get_width()*1, explosion5.get_height()*1))
    explosion6 = pg.image.load(IMAGE_PATH + "Ex6.png").convert_alpha()
    # explosion6 = pg.transform.scale(explosion6, (explosion6.get_width()*1, explosion6.get_height()*1))
    explosion7 = pg.image.load(IMAGE_PATH + "Ex7.png").convert_alpha()
    # explosion7 = pg.transform.scale(explosion7, (explosion7.get_width()*1, explosion7.get_height()*1))
    explosion8 = pg.image.load(IMAGE_PATH + "Ex8.png").convert_alpha()
    # explosion8 = pg.transform.scale(explosion8, (explosion8.get_width()*1, explosion8.get_height()*1))
    image = {
        1: explosion1
        ,2: explosion2
        ,3: explosion3
        ,4: explosion4
        ,5: explosion5
        ,6: explosion6
        ,7: explosion7
        ,8: explosion8
    }
    return image

def loadSpawnImage():
    spawn1 = pg.image.load(IMAGE_PATH + "Spawn.png").convert_alpha()
    # spawn1 = pg.transform.scale(spawn1, (spawn1.get_width()*1, spawn1.get_height()*1))
    spawn2 = pg.image.load(IMAGE_PATH + "Spawn2.png").convert_alpha()
    # spawn2 = pg.transform.scale(spawn2, (spawn2.get_width()*1, spawn2.get_height()*1))
    spawn3 = pg.image.load(IMAGE_PATH + "Spawn3.png").convert_alpha()
    # spawn3 = pg.transform.scale(spawn3, (spawn3.get_width()*1, spawn3.get_height()*1))
    spawn4 = pg.image.load(IMAGE_PATH + "Spawn4.png").convert_alpha()
    # spawn4 = pg.transform.scale(spawn4, (spawn4.get_width()*1, spawn4.get_height()*1))
    spawn5 = pg.image.load(IMAGE_PATH + "Spawn5.png").convert_alpha()
    # spawn5 = pg.transform.scale(spawn5, (spawn5.get_width()*1, spawn5.get_height()*1))
    spawn6 = pg.image.load(IMAGE_PATH + "Spawn6.png").convert_alpha()
    # spawn6 = pg.transform.scale(spawn6, (spawn6.get_width()*1, spawn6.get_height()*1))
    spawn7 = pg.image.load(IMAGE_PATH + "Spawn7.png").convert_alpha()
    # spawn7 = pg.transform.scale(spawn7, (spawn7.get_width()*1, spawn7.get_height()*1))
    spawn8 = pg.image.load(IMAGE_PATH + "Spawn8.png").convert_alpha()
    # spawn8 = pg.transform.scale(spawn8, (spawn8.get_width()*1, spawn8.get_height()*1))
    image = {
        1: spawn1
        ,2: spawn2
        ,3: spawn3
        ,4: spawn4
        ,5: spawn5
        ,6: spawn6
        ,7: spawn7
        ,8: spawn8
    }
    return image