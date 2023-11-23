from tools.graphic_tool import *
from tools.moving_tools import get_adjacent_tiles
import random
import math


class Bob:
    def __init__(self, world, x, y, velocity=None, mass=1):
        self.world = world

        image = pg.image.load("graphics/bob.png").convert_alpha()
        self.image = pg.transform.scale(image, (image.get_width() * 2, image.get_height() * 2))

        self.x = x
        self.y = y
        self.mass = mass

        self.energy = 100
        self.energy_max = 200
        self.energy_loss_for_duplicating = 150

        self.velocity = velocity if velocity is not None else 1
        self.velocity_buffer = 0
        self.effective_velocity = self.velocity + self.velocity_buffer

    def update(self):
        self.move()

        if self.energy <= 0:
            self.die()
        elif self.energy >= self.energy_max:
            self.duplicate()

        self.consume_energy()

    def move(self):
        for _ in range(math.floor(self.effective_velocity)):
            adjacent_tiles = get_adjacent_tiles(self.x, self.y, self.world.grid_length_x, self.world.grid_length_y)
            if adjacent_tiles:
                new_x, new_y = random.choice(adjacent_tiles)
                self.x = new_x
                self.y = new_y

                for food in self.world.foods:
                    if (food.x, food.y) == (self.x, self.y):
                        self.eat(food)

                for bob in self.world.bobs:
                    if bob != self and (bob.x, bob.y) == (self.x, self.y):
                        self.encounter(bob)

        self.velocity_buffer = round(self.effective_velocity - math.floor(self.effective_velocity), 2)
        self.effective_velocity = self.velocity + self.velocity_buffer

    def eat(self, food):
        energy_consumed = min(self.energy_max, self.energy + food.energy) - self.energy
        self.energy = min(self.energy_max, self.energy + food.energy)
        food.energy -= energy_consumed
        if food.energy == 0:
            self.world.foods.remove(food)

    def encounter(self, other_bob):
        size_ratio = other_bob.mass / self.mass

        if size_ratio < 2 / 3:
            # Big Bob can eat small bob
            energy_gained = min(0.5 * other_bob.energy, 0.5 * self.energy * (1 - size_ratio))
            self.energy += energy_gained
            self.world.bobs.remove(other_bob)

    def consume_energy(self):
        if self.energy > 0:
            kinetic_energy_cost = max(0.5, (self.effective_velocity ** 2) / 2)
            energy_consumption = max(0.5, kinetic_energy_cost)
            self.energy -= energy_consumption

    def duplicate(self):
        mutation_rate = 0.1
        mutation = random.uniform(-mutation_rate, mutation_rate)
        new_velocity = max(0.1, min(2, self.velocity + mutation))
        new_mass = max(0.1, min(5, self.mass + mutation))

        new_bob = Bob(self.world, self.x, self.y, new_velocity, new_mass)
        new_bob.energy = 50
        self.energy = self.energy_max - self.energy_loss_for_duplicating
        self.world.bobs.append(new_bob)

    def die(self):
        self.world.bobs.remove(self)
