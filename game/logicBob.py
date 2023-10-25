
import random
import time

class Bot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def check_collision(bot, food):
    # Cette fonction vérifie si un Bot entre en collision avec de la nourriture.
    # Vous devez adapter la logique en fonction de votre modèle de données.

    if (bot.x == food.x) and (bot.y == food.y):
        return True
    return False

# Boucle principale de simulation
while True:
    # Vérifier si la nourriture doit apparaître
    if random.random() < 0.1:  # Par exemple, 10% de chance d'apparition
        food = spawn_food()

    # Vérifier si la nourriture doit disparaître
    if food and should_disappear(food):
        food = None  # La nourriture disparaît

    # Simuler des Bots et vérifier les collisions
    bots = [Bot(random.randint(0, 100), random.randint(0, 100)) for _ in range(10)]  # Exemple : 10 Bots
    for bot in bots:
        if food and check_collision(bot, food):
            # Gérer la consommation de la nourriture ici
            food = None  # La nourriture est consommée

    # Continuer la simulation
    time.sleep(1)  # Simulez une seconde d'écoulement du temps entre chaque itération