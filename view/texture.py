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
def loadFoodImage():
    food = pg.image.load(IMAGE_PATH + "food.png").convert_alpha()
    food = pg.transform.scale(food, (food.get_width()*0.25, food.get_height()*0.25))
    image = {
        "Food": food
    }
    return image

def loadExplosionImage():
    explosion1 = pg.image.load(IMAGE_PATH + "Ex1.png").convert_alpha()
    explosion1 = pg.transform.scale(explosion1, (explosion1.get_width()*1, explosion1.get_height()*1))
    explosion2 = pg.image.load(IMAGE_PATH + "Ex2.png").convert_alpha()
    explosion2 = pg.transform.scale(explosion2, (explosion2.get_width()*1, explosion2.get_height()*1))
    explosion3 = pg.image.load(IMAGE_PATH + "Ex3.png").convert_alpha()
    explosion3 = pg.transform.scale(explosion3, (explosion3.get_width()*1, explosion3.get_height()*1))
    explosion4 = pg.image.load(IMAGE_PATH + "Ex4.png").convert_alpha()
    explosion4 = pg.transform.scale(explosion4, (explosion4.get_width()*1, explosion4.get_height()*1))
    explosion5 = pg.image.load(IMAGE_PATH + "Ex5.png").convert_alpha()
    explosion5 = pg.transform.scale(explosion5, (explosion5.get_width()*1, explosion5.get_height()*1))
    explosion6 = pg.image.load(IMAGE_PATH + "Ex6.png").convert_alpha()
    explosion6 = pg.transform.scale(explosion6, (explosion6.get_width()*1, explosion6.get_height()*1))
    explosion7 = pg.image.load(IMAGE_PATH + "Ex7.png").convert_alpha()
    explosion7 = pg.transform.scale(explosion7, (explosion7.get_width()*1, explosion7.get_height()*1))
    explosion8 = pg.image.load(IMAGE_PATH + "Ex8.png").convert_alpha()
    explosion8 = pg.transform.scale(explosion8, (explosion8.get_width()*1, explosion8.get_height()*1))
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
