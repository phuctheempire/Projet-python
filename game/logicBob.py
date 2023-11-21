import random

class logicBob:
    
    def __init__(self, initial_population=100, max_energy=200, food_spawn_rate=200, energy_per_food=100):
       self.population = [self.create_bob(max_energy) for _ in range(initial_population)]
       self.food_spawn_rate = food_spawn_rate
       self.energy_per_food = energy_per_food
       
    def create_bob(self, max_energy):
            return {
                "energy":100,
                "velocity": 1,
                "mass": random.uniform(0.9, 1.1),
                "perception": random.randint(0, 5),
                "memory": random.randint(0, 5),
                "x": random.randint(0, 100),
                "y": random.randint(0, 100),
            }
    
    def move(self, bob):
        velocity = bob["velocity"]
        energy_cost = velocity ** 2  
        bob["energy"] -= energy_cost
        # Implémentez la logique pour déplacer le Bob dans le monde, par exemple, en mettant à jour ses coordonnées (x, y).
        # Assurez-vous que le déplacement reste dans les limites de votre monde.

    #def eat(self, bob):
        # Mangez de la nourriture et augmentez l'énergie
        #food_energy = random.randint(1, self.energy_per_food)
        #bob["energy"] += food_energy
        # Implémentez la logique pour gérer la consommation de nourriture, par exemple, en supprimant la nourriture du monde.

    def reproduce(self, parent):
        child = {
            "energy": 50,
            "velocity": random.uniform(parent.velocity-0.1, parent.velocity+0.1),
            #"mass": (parent["mass"] + parent2["mass"]) / 2,
            #"perception": random.randint(0, 5),
            #"memory": random.randint(0, 5), 
            "x":parent.x,
            "y": parent.y, 
        }
        parent.energy =150
        return child
