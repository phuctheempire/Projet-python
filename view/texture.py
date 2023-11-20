# Texture templates: Author: Xuan Phuc
    # Import modules
    # Init templates
# Implementation et dévellopement: Émile Pétier

import pygame as pg

from enum import Enum

from TextureLib.bobTexture import BobTexture
from TextureLib.foodTexture import FoodTexture
from TextureLib.directionTexture import DirectionTexture
from TextureLib.eatenTexture import EatenTexture
from TextureLib.grassTexture import GrassTexture
# Import libraries
from GameControl.settings import IMAGE_PATH
# import imgpath
class Texture:
    grass_texture: dict[GrassTexture, pg.Surface] = {}
    bob_texture: dict[BobTexture, dict[DirectionTexture, dict[int, pg.Surface]]] = {}
    food_texture: dict[FoodTexture, pg.Surface] = {}
    eaten_texture: dict[EatenTexture, pg.Surface] = {}

    # We make dictionaries of each component of the texture

    @staticmethod
    def getGrassTexture( ID: any, Number: int = 0) -> pg.surface:
        return Texture.grass_texture[ID]
    @staticmethod
    def getBobTexture( ID: BobTexture, direction: DirectionTexture, frame: int = 0) -> pg.surface:
        pass
    @staticmethod
    def getFoodTexture( ID: FoodTexture, Number: int = 0) -> pg.surface:
        pass
    #Continuez ici
    # @staticmethod
    # def getEatenTexture( ID: EatenTexture, Number: int = 0 ) -> pg.surface:

    @staticmethod
    def init(screen):
        Texture.grass_texture = {
            "Grass": pg.image.load(IMAGE_PATH + "grass.png").convert_alpha(screen),
            "Flower": pg.image.load(IMAGE_PATH + "flower.png").convert_alpha(screen),
        }
        Texture.food_texture = {
            FoodTexture.LARGE: pg.image.load(IMAGE_PATH + "apple.png").convert_alpha(screen), #example
            FoodTexture.MEDIUM: pg.image.load(IMAGE_PATH + "banana.png").convert_alpha(screen),
            FoodTexture.SMALL: pg.image.load(IMAGE_PATH + "pear.png").convert_alpha(screen),
        }

        # Gerer et implémenter Bobs et orientation ici 
        #Continuer ici

    