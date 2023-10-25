import random

class logicBob:
    
    def __init__(self, initial_population=100, max_energy=200, food_spawn_rate=200, energy_per_food=100):
       self.population = [self.create_bob(max_energy) for _ in range(initial_population)]
       self.food_spawn_rate = food_spawn_rate
       self.energy_per_food = energy_per_food
       
    def create_bob(self, max_energy):
            return {
                "energy": random.randint(1, max_energy),
                "velocity": random.uniform(0.9, 1.1),
                "mass": random.uniform(0.9, 1.1),
                "perception": random.randint(0, 5),
                "memory": random.randint(0, 5),
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