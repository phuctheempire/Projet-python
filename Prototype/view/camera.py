import pygame as pg


class Camera:

    def __init__(self, width, height):

        self.width = width
        self.height = height

        self.scroll = pg.Vector2(0, 0) #scroll is a vector
        self.dx = 0
        self.dy = 0
        self.speed = 25 #speed of the camera

    def update(self):
        #DPI settings
        
        mouse_pos = pg.mouse.get_pos() #get the position of the mouse

        # x movement
        if mouse_pos[0] > self.width * 0.97:
            self.dx = -self.speed
        elif mouse_pos[0] < self.width * 0.03:
            self.dx = self.speed
        else:
            self.dx = 0

        # y movement
        if mouse_pos[1] > self.height * 0.97:
            self.dy = -self.speed
        elif mouse_pos[1] < self.height * 0.03:
            self.dy = self.speed
        else:
            self.dy = 0

        # update camera scroll
        self.scroll.x += self.dx
        self.scroll.y += self.dy