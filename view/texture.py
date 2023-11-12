# Texture templates: Author: Xuan Phuc
    # Import modules
    # Init templates
# Implementation et dévellopement: Émile Pétier

import pygame as pg

from enum import Enum

from ..TextureLibrary.bobTexture import BobTexture
from ..TextureLibrary.foodTexture import FoodTexture
from ..TextureLibrary.directionTexture import DirectionTexture
from ..TextureLibrary.eatenTexture import EatenTexture
from ..TextureLibrary.grassTexture import GrassTexture
# Import Library
#raries
from GameControl.settings import IMAGE_PATH
# import imgpath
class Texture:
    grass_texture: dict[GrassTexture, pg.Surface] = {}
    bob_texture: dict[BobTexture, dict[DirectionTexture, dict[int, pg.Surface]]] = {}
    food_texture: dict[FoodTexture, pg.Surface] = {}
    eaten_texture: dict[EatenTexture, pg.Surface] = {}

    # We make dictionaries of each component of the texture

    @staticmethod
    def getTexture( ID: any, Number: int = 0) -> pg.surface:
        pass
        # Il faut return la surface
    @staticmethod
    def getBobTexture( ID: BobTexture, direction: DirectionTexture, frame: int = 0) -> pg.surface:
        pass
        # Il faut return la surface
    @staticmethod
    def getFoodTexture( ID: FoodTexture, Number: int = 0) -> pg.surface:
        pass
        # Il faut return la surface
    #Continuez ici
    # @staticmethod
    # def getEatenTexture( ID: EatenTexture, Number: int = 0 ) -> pg.surface:

    @staticmethod
    def init(screen):
        # See Texturelibrary for more info
        Texture.grass_texture = {
            GrassTexture.GRASS: pg.image.load(IMAGE_PATH + "grass.png").convert_alpha(screen),
            GrassTexture.FLOWER: pg.image.load(IMAGE_PATH + "flower.png").convert_alpha(screen),
        }
        Texture.food_texture = {
            FoodTexture.LARGE: pg.image.load(IMAGE_PATH + "apple.png").convert_alpha(screen), #example
            FoodTexture.MEDIUM: pg.image.load(IMAGE_PATH + "banana.png").convert_alpha(screen),
            FoodTexture.SMALL: pg.image.load(IMAGE_PATH + "pear.png").convert_alpha(screen),
        }

        # Gerer et implémenter Bobs et orientation ici 
        #Continuer ici

    