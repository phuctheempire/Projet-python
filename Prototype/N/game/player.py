import pygame as pg
from pygame.sprite import _Group

import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load("player.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

pg.init()
screen = pg.display.set_mode((800, 600))
player = Player(400, 300)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    screen.fill((255, 255, 255))
    screen.blit(player.image, player.rect)
    pg.display.update()