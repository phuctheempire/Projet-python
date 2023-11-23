import pygame as pg
from .graphic_tool import TILE_SIZE


def isometric_convert(x, y):
    iso_x = x - y
    iso_y = (x + y) / 2
    return iso_x, iso_y


def grid_to_world(x, y):
    rect = [
        (x * TILE_SIZE, y * TILE_SIZE),
        (x * TILE_SIZE + TILE_SIZE, y * TILE_SIZE),
        (x * TILE_SIZE + TILE_SIZE, y * TILE_SIZE + TILE_SIZE),
        (x * TILE_SIZE, y * TILE_SIZE + TILE_SIZE)
    ]

    iso_poly = [isometric_convert(x, y) for x, y in rect]

    minx = min([x for x, y in iso_poly])
    miny = min([y for x, y in iso_poly])

    return {
        "grid": [x, y],
        "cart_rect": rect,
        "iso_poly": iso_poly,
        "render_pos": [minx, miny],
    }
