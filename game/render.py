import pygame as pg
from .bob import Bob
from .food import Food

class Render:
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
        energy_levels = {
            (76, 100): "chemin1.png",
            (50, 75): "chemin2.png",
            (25, 49): "chemin3.png",
            (0, 24): "chemin4.png"
        }

        for energy_range, image_path in energy_levels.items():
            if energy_range[0] <= food.energy <= energy_range[1]:
                food_image = pg.image.load(image_path).convert_alpha()
                self.screen.blit(food_image, (food.x, food.y))
                break
        else:
            default_image = pg.image.load("default_path.png").convert_alpha()
            self.screen.blit(default_image, (food.x, food.y)) 


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
