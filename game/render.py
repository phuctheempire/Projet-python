import pygame as pg
from .bob import Bob
from .food import Food

class Renderer:
    def __init__(self, screen, clock, world):
        self.screen = screen
        self.clock = clock
        self.world = world

    def draw_world(self):
        # Dessiner le monde
        self#commentaire 


    def draw_bob(self, bob):
        self.screen.blit(bob.image, (bob.x, bob.y))

    def draw_food(self, food):
        if food.energy > 75:
            food_image = pg.image.load("chemin").convert_alpha()
        elif 50 <= food.energy <= 75:
            food_image = pg.image.load("").convert_alpha()
        elif 25 <= food.energy < 50:
            food_image = pg.image.load("").convert_alpha()
        else:
            food_image = pg.image.load("").convert_alpha()

        food_image = pg.transform.scale(food_image, (food_image.get_width()*1, food_image.get_height()*1))
        self.screen.blit(food_image, (food.x, food.y))


    def render_frame(self):
        self.draw_world()

        for row in self.world:
            for tile in row:
                if tile is not None:
                    if isinstance(tile, Bob):
                        self.draw_bob(tile) 
                    elif isinstance(tile, Food):
                        self.draw_food(tile)

        pg.display.flip()
        self.clock.tick(60)
