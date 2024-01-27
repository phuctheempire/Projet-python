import matplotlib.pyplot as plt
from GameControl.gameControl import GameControl
import pygame as pg


# class Graph:
#     def __init__():
#         gameControl.gameControl = GameControl.getInstance()
gameControl = GameControl.getInstance() 

# def draw_graph():
#     if gameControl.graphData:
#         ticks, bob_counts = zip(*gameControl.graphData)
#         plt.plot(ticks, bob_counts)
#         plt.xlabel('Ticks')
#         plt.ylabel('Number of Bobs')
#         plt.title('Number of Bobs vs Ticks')
#         plt.show()
#     if gameControl.diedData:
#         ticks, died_counts = zip(*gameControl.diedData)
#         plt.plot(ticks, died_counts)
#         plt.xlabel('Ticks')
#         plt.ylabel('Number of dead')
#         plt.title('Number of dead vs Ticks')
#         plt.show()


def show_graph_data(filename='graph_data.txt'):
    if not gameControl.graphData:
        print("Aucune donnée à afficheer")
        return
    if filename:
        save_graph_data(filename)

    ticks, bob_counts = zip(*gameControl.graphData)
    plt.plot(ticks, bob_counts)
    plt.xlabel('Ticks')
    plt.ylabel('Nombre de Bobs')
    plt.title('Nombre de Bobs vs Ticks')
    plt.show()

def show_died_data(filename='died_data.txt'):
    if not gameControl.diedData:
        print("Aucune donnée à afficheer")
        return
    if filename:
        save_died_data(filename)
    ticks, died_counts = zip(*gameControl.diedData)
    plt.plot(ticks, died_counts)
    plt.xlabel('Ticks')
    plt.ylabel('Nombre de dead')
    plt.title('Nombre de dead vs Ticks')
    plt.show()

def show_mass_data(filename='mass_data.txt'):
    if not gameControl.massData:
        print("Aucune donnée à afficheer")
        return
    if filename:
        save_mass_data(filename)
    ticks, mass_counts = zip(*gameControl.massData)
    plt.plot(ticks, mass_counts)
    plt.xlabel('Ticks')
    plt.ylabel('Masse moyenne')
    plt.title('Masse moyenne vs Ticks')
    plt.show()

def show_born_data(filename='born_data.txt'):
    if not gameControl.graphData:
        print("Aucune donnée à afficher")
        return
    if filename:
        save_born_data(filename)

    ticks, bob_counts = zip(*gameControl.bornData)
    plt.plot(ticks, bob_counts)
    plt.xlabel('Ticks')
    plt.ylabel('Nombre de born')
    plt.title('Nombre de born vs Ticks')
    plt.show()

def show_veloce_data(filename='veloce_data.txt'):
    if not gameControl.veloceData:
        print("Aucune donnée à afficheer")
        return
    if filename:
        save_veloce_data(filename)
    ticks, veloce_counts = zip(*gameControl.veloceData)
    plt.plot(ticks, veloce_counts)
    plt.xlabel('Ticks')
    plt.ylabel('vélocité moyenne')
    plt.title('vélocité moyenne vs Ticks')
    plt.show()

def show_vision_data(filename='vision_data.txt'):
    if not gameControl.visionData:
        print("Aucune donnée à afficheer")
        return
    if filename:
        save_vision_data(filename)
    ticks, vision_counts = zip(*gameControl.visionData)
    plt.plot(ticks, vision_counts)
    plt.xlabel('Ticks')
    plt.ylabel('vison moyenne')
    plt.title('vision moyenne vs Ticks')
    plt.show()
    
def show_energy_data(filename='energy_data.txt'):
    if not gameControl.energyData:
        print("Aucune donnée à afficheer")
        return
    if filename:
        save_energy_data(filename)
    ticks, energy_counts = zip(*gameControl.energyData)
    plt.plot(ticks, energy_counts)
    plt.xlabel('Ticks')
    plt.ylabel('Energy moyenne')
    plt.title('Energy moyenne vs Ticks')
    plt.show()

def save_graph_data(filename='graph_data.txt'):
    with open(filename, 'w') as file:
        for tick, count in gameControl.graphData:
            file.write(f"{tick}\t{count}\n")

def save_died_data(filename='died_data.txt'):
    with open(filename, 'w') as file:
        for tick, count in gameControl.diedData:
            file.write(f"{tick}\t{count}\n")

def save_mass_data(filename='mass_data.txt'):
    with open(filename, 'w') as file:
        for tick, count in gameControl.massData:
            file.write(f"{tick}\t{count}\n")

def save_born_data(filename='born_data.txt'):
    with open(filename, 'w') as file:
        for tick, count in gameControl.bornData:
            file.write(f"{tick}\t{count}\n")

def save_veloce_data(filename='veloce_data.txt'):
    with open(filename, 'w') as file:
        for tick, count in gameControl.veloceData:
            file.write(f"{tick}\t{count}\n")

def save_vision_data(filename='vision_data.txt'):
    with open(filename, 'w') as file:
        for tick, count in gameControl.visionData:
            file.write(f"{tick}\t{count}\n")


def save_energy_data(filename='energy_data.txt'):
    with open(filename, 'w') as file:
        for tick, count in gameControl.energyData:
            file.write(f"{tick}\t{count}\n")

#