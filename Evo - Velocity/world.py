import pygame as pg
from tools.graphic_tool import *
from tools.logical_tool import *
from entities.Bob import Bob
from entities.Food import Food
import random


class World:

    def __init__(self, grid_length_x, grid_length_y, width, height):
        self.grid_length_x = grid_length_x
        self.grid_length_y = grid_length_y
        self.width = width
        self.height = height

        self.grass_tiles = pg.Surface((grid_length_x * TILE_SIZE * 4,
                                       grid_length_y * TILE_SIZE + 4 * TILE_SIZE)).convert_alpha()

        self.tiles = load_images()
        self.world = self.create_world()

        self.tick_count = 0
        self.day_count = 0

        self.day = 100
        self.food_quantity = 10

        self.bobs = []
        for _ in range(2):
            bob_x = random.randint(0, self.grid_length_x - 1)
            bob_y = random.randint(0, self.grid_length_y - 1)
            bob = Bob(self, bob_x, bob_y)
            self.bobs.append(bob)

        self.foods = []
        for _ in range(self.food_quantity):
            food_x = random.randint(0, self.grid_length_x - 1)
            food_y = random.randint(0, self.grid_length_y - 1)
            food = Food(self, food_x, food_y)
            self.foods.append(food)

    def create_world(self):

        world = []

        for grid_x in range(self.grid_length_x):  # x run from 0 to grid_length_x (1 -> 10)
            world.append([])
            for grid_y in range(self.grid_length_y):  # y run from 0 to grid_length_y (1 -> 10)
                world_tile = grid_to_world(grid_x, grid_y)
                world[grid_x].append(world_tile)

                render_pos = world_tile["render_pos"]
                self.grass_tiles.blit(self.tiles["block"],
                                      (render_pos[0] + self.width / 2,
                                       render_pos[1] + self.height / 8))

        return world

    def update(self):

        self.bobs.sort(key=lambda bob: bob.effective_velocity, reverse=True)

        for bob in self.bobs:
            bob.update()
        if self.tick_count % self.day == 0:
            self.day_count += 1
            self.cleanup_food()
            self.spawn_food()

    def cleanup_food(self):
        self.foods = []

    def spawn_food(self):
        for _ in range(self.food_quantity):
            food_x = random.randint(0, self.grid_length_x - 1)
            food_y = random.randint(0, self.grid_length_y - 1)
            food = Food(self, food_x, food_y)
            self.foods.append(food)

    def draw(self, screen):
        screen.blit(self.grass_tiles, (0, 0))

        for x in range(self.grid_length_x):
            for y in range(self.grid_length_y):
                # sq = self.world[x][y]["cart_rect"]
                # rect = pg.Rect(sq[0][0], sq[0][1], TILE_SIZE, TILE_SIZE)
                # pg.draw.rect(screen, (0, 0, 255), rect, 1)

                p = self.world[x][y]["iso_poly"]
                p = [(x + self.width / 2, y + self.height / 8) for x, y in p]
                pg.draw.polygon(screen, (255, 0, 0), p, 1)

        for food in self.foods:
            food.draw(screen)

        for bob in self.bobs:
            draw_bob(screen, bob)
