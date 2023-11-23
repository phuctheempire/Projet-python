import pygame as pg
import random
from tools.graphic_tool import *


class Food:
    def __init__(self, world, x, y):
        self.world = world

        image = pg.image.load("graphics/rock.png").convert_alpha()
        self.image = pg.transform.scale(image, (image.get_width(), image.get_height()))

        self.x = x
        self.y = y

        self.energy = 100

    def draw(self, screen):
        render_pos = self.world.world[self.x][self.y]["render_pos"]
        screen.blit(self.image,
                    (render_pos[0] + self.world.width / 2,
                     render_pos[1] + TILE_SIZE))

        # draw the energy bar
        bar_width = int((self.energy / 100) * 50)

        pg.draw.rect(screen, (0, 255, 0), (render_pos[0] + self.world.width / 2 + TILE_SIZE / 2,
                                           render_pos[1] + TILE_SIZE,
                                           bar_width, 5))

    def accumulate_energy(self, other_food):
        self.energy += other_food.energy

    # def add_up_energy(self, foods):
    #     # Check for collisions between bobs and food
    #     food_in_cell = [food for food in foods if (food.x, food.y) == (self.x, self.y)]
    #
    #     if food_in_cell:
    #         for i in range(1, len(food_in_cell)):
    #             food_in_cell[0].accumulate_energy(food_in_cell[i])
    #             foods.remove(food_in_cell[i])
