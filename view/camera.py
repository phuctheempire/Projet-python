import pygame as pg
from GameControl.setting import Setting


class Camera:

    def __init__(self, width, height):
        self.setting = Setting.getSettings()
        self.width = width
        self.height = height

        self.scroll = pg.Vector2(0, 0) #scroll is a vector
        self.scroll.x = - self.setting.getSurfaceWidth()/2 + self.width / 2
        self.scroll.y = - self.setting.getSurfaceHeight()/2 + self.height / 2
        self.dx = 0 #change in x
        self.dy = 0
        self.speed = 25 #speed of the camera

    def update(self):
        #DPI settings
        key = pg.key.get_pressed()

        # for event in pg.event.get():
        #     if event.type == pg.KEYDOWN:
        if key[pg.K_RIGHT]:
            self.dx = -self.speed
            # print("left")
        elif key[pg.K_LEFT]:
            self.dx = self.speed
            # print("right")
        else:
            self.dx = 0

        if key[pg.K_DOWN]:
            self.dy = -self.speed
            # print("up")
        elif key[pg.K_UP]:
            self.dy = self.speed
            # print("down")
        else:
            self.dy = 0
        # mouse_pos = pg.mouse.get_pos() #get the position of the mouse

        # # x movement
        # if mouse_pos[0] > self.width * 0.97:
        #     self.dx = -self.speed
        # elif mouse_pos[0] < self.width * 0.03:
        #     self.dx = self.speed
        # else:
        #     self.dx = 0

        # # y movement
        # if mouse_pos[1] > self.height * 0.97:
        #     self.dy = -self.speed
        # elif mouse_pos[1] < self.height * 0.03:
        #     self.dy = self.speed
        # else:
        #     self.dy = 0
        # update camera scroll
        self.scroll.x += self.dx
        self.scroll.y += self.dy