# define visual Bob:
import pygame as pg
import random

class Bob:

    def __init__(self, tile, world):

        # Bob(self.world.world[5][5], self.world)
        self.world = world # become World class
        self.tile = tile 
        # == self.world.world[5][5]
        # self.world.world is a double list of dictionaries
        # self.world.world[5][5] is a dictionary >> self.tile is a dictionary
        #
        image = pg.image.load("assets/graphics/bob.png").convert_alpha()
        self.image = pg.transform.scale(image, (image.get_width()*1, image.get_height()*1))
        self.name = "bob"
        self.world.bob[tile["grid"][0]][tile["grid"][1]] = self # assign bob to the attribute bob in the world class
        # self.world.bob is a double list of dictionaries of NONE (innitially)
        # tiles are dictionaries
        # tiles["grid"] is a list of grid coordinates
        # tiles["grid"][0] is x coordinate
        # tiles["grid"][1] is y coordinate
        # self.world.bob[tile["grid"][0]][tile["grid"][1]] = self ( we assign a bob into this dictionary of none)
    #def color(self, image):
        

        

    #def __init__(self, initial_population=100, max_energy=200, food_spawn_rate=200, energy_per_food=100):
    #   self.population = [self.create_bob(max_energy) for _ in range(initial_population)]
    #    self.food_spawn_rate = food_spawn_rate
    #    self.energy_per_food = energy_per_food

    def create_bob(self, max_energy):
        return {
            "energy": random.randint(1, max_energy),
            "velocity": random.uniform(0.9, 1.1),
            "mass": random.uniform(0.9, 1.1),
            "perception": random.randint(0, 5),
            "memory": random.randint(0, 5),
        }

    def spawn_food(self):
        food_energy = random.randint(1, self.energy_per_food)
        return {
            "energy": food_energy,
            "x": random.randint(0, 100),
            "y": random.randint(0, 100),
        }

    def simulate(self, num_days):
        for day in range(num_days):
            if day % self.food_spawn_rate == 0:
                food = self.spawn_food()
                # Add food to the world

            #for bob in self.population:
                # Implement Bob's behaviors here

            # Remove uneaten food at the end of the day

