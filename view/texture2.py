import pygame as pg
from GameControl.settings import IMAGE_PATH

class Texture:
    grass_texture: {
        1: pg.image.load(IMAGE_PATH + "grass.png").convert_alpha(),
        2: pg.image.load(IMAGE_PATH + "flower.png").convert_alpha(),
    }
    
    def __init__(s) -> None:
        pass