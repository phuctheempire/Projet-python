import pygame as pg

from enum import Enum

from ..TextureLib.bobTexture import BobTexture
from ..TextureLib.foodTexture import FoodTexture
from ..TextureLib.orientTexture import OrientTexture

from GameControl.settings import IMAGE_PATH

class Texture:
    texture: dict[Enum, pg.Surface | dict[int, pg.Surface]] = {}
    bob_texture: dict[BobTexture, dict[OrientTexture, dict[int, pg.Surface]]] = {}
    eatenTexture: dict[pg.Surface] = {}

    @staticmethod
    def getTexture( ID: any, Number: int = 0) -> pg.surface:

    @staticmethod
    def getBobTexture( ID: BobTexture, orient: OrientTexture, frame: int = 0) -> pg.surface:

