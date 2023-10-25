import random

class logicBob:
    
    def __init__(self, initial_population=100, max_energy=200, food_spawn_rate=200, energy_per_food=100):
       self.population = [self.create_bob(max_energy) for _ in range(initial_population)]
       self.food_spawn_rate = food_spawn_rate
       self.energy_per_food = energy_per_food
       
    def create_bob(self, max_energy):
            return {
                "energy":100,
                "velocity": random.uniform(0.9, 1.1),
                "mass": random.uniform(0.9, 1.1),
                "perception": random.randint(0, 5),
                "memory": random.randint(0, 5),
                "x": random.randint(0, 100),
                "y": random.randint(0, 100),
            }
 