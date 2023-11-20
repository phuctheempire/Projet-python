# Texture templates: Author: Xuan Phuc
    # Import modules
    # Init templates
# Implementation et dévellopement: Émile Pétier

import pygame as pg

from enum import Enum

# from TextureLib.bobTexture import BobTexture
# from TextureLib.foodTexture import FoodTexture
# from TextureLib.directionTexture import DirectionTexture
# from TextureLib.eatenTexture import EatenTexture
# from TextureLib.grassTexture import GrassTexture
# Import libraries
from GameControl.settings import IMAGE_PATH
# import imgpath
class Texture:
    grass_texture: dict[int , pg.Surface] = {}
    # bob_texture: dict[BobTexture, dict[DirectionTexture, dict[int, pg.Surface]]] = {}
    # food_texture: dict[FoodTexture, pg.Surface] = {}
    # eaten_texture: dict[EatenTexture, pg.Surface] = {}

    # # We make dictionaries of each component of the texture

    @staticmethod
    def getGrassTexture( ID: any) -> pg.surface:
        return Texture.grass_texture[ID]
    # @staticmethod
    # def getBobTexture( ID: BobTexture, direction: DirectionTexture, frame: int = 0) -> pg.surface:
    #     pass
    # @staticmethod
    # def getFoodTexture( ID: FoodTexture, Number: int = 0) -> pg.surface:
    #     pass
    # #Continuez ici
    # # @staticmethod
    # # def getEatenTexture( ID: EatenTexture, Number: int = 0 ) -> pg.surface:

    def init(screen):
        Texture.grass_texture = {
            1: pg.image.load(IMAGE_PATH + "grass.png").convert_alpha(screen),
            2: pg.image.load(IMAGE_PATH + "flower.png").convert_alpha(screen),
        }
        # Texture.food_texture = {
        #     "Large": pg.image.load(IMAGE_PATH + "apple.png").convert_alpha(screen), #example
        #     "Medium": pg.image.load(IMAGE_PATH + "banana.png").convert_alpha(screen),
        #     "Small": pg.image.load(IMAGE_PATH + "pear.png").convert_alpha(screen),
        # }

        # Gerer et implémenter Bobs et orientation ici 
        #Continuer ici

    