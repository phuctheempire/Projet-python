import random


def randomDistinguish(nbTimes, ranging) -> list(tuple):
    couples: list(tuple) = []
    for _ in range(nbTimes):
        x = random.randint(0,ranging)
        y = random.randint(0,ranging)
        while (x, y) in couples:
            x = random.randint(0,ranging)
            y = random.randint(0,ranging)
        couples.append((x, y))
    return couples

def randomDuplicatable(nbTimes, ranging) -> list(tuple):
    couples: list(tuple) = []
    for _ in range(nbTimes):
        x = random.randint(0,ranging)
        y = random.randint(0,ranging)
        couples.append((x, y))
    return couples