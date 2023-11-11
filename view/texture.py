import pygame as pg

from enum import Enum

from ..TextureLib.bobTexture import BobTexture
from ..TextureLib.foodTexture import FoodTexture
from ..TextureLib.directionTexture import DirectionTexture
from ..TextureLib.eatenTexture import EatenTexture
from ..TextureLib.grassTexture import GrassTexture

from GameControl.settings import IMAGE_PATH

class Texture:
    grass_texture: dict[GrassTexture, pg.Surface] = {}
    bob_texture: dict[BobTexture, dict[DirectionTexture, dict[int, pg.Surface]]] = {}
    food_texture: dict[FoodTexture, pg.Surface] = {}
    eaten_texture: dict[EatenTexture, pg.Surface] = {}


    @staticmethod
    def getTexture( ID: any, Number: int = 0) -> pg.surface:

    @staticmethod
    def getBobTexture( ID: BobTexture, direction: DirectionTexture, frame: int = 0) -> pg.surface:

    @staticmethod
    def getFoodTexture( ID: FoodTexture, Number: int = 0) -> pg.surface:
    # @staticmethod
    # def getEatenTexture( ID: EatenTexture, Number: int = 0 ) -> pg.surface:
    
    @staticmethod
    def init(screen):
        Texture.texture{
            grassTexture.GRASS: pg.image.load(IMAGE_PATH + "grass.png").convert_alpha(screen),
        }