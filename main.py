import pygame as pg
from GameControl.game import Game
from GameControl.EventManager import show_menu
from pygame.locals import *

from GameControl.setting import Setting
# from GameControl.gameControl import GameControl
import sys

flags = HWSURFACE | DOUBLEBUF

def main():

    running = True
    playing = True

    pg.init()
    pg.mixer.init()
    # screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    screen = pg.display.set_mode((1920,1080), flags)
    #screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    clock = pg.time.Clock()
    # setting = Setting.getSettings()
    # implement menus
    i = show_menu(screen, clock)
    # implement game 
    game = Game(screen, clock)
    if i == 0:
        print("i = ", i )
        print("new game")
        game.createNewGame()
    elif i == 1:
        print("i = ", i )
        print("load game")
        game.loadGame(1)
    elif i == 2:
        print("i = ", i )
        print("load game")
        game.loadGame(2)
    elif i == 3:
        print("i = ", i )
        print("load game")
        game.loadGame(3)
    elif i == 4:
        print("i = ", i )
        print("load game")
        game.loadGame(4)
    elif i == 5:
        print("i = ", i )
        print("load game")
        game.loadGame(5)

    while running:
        
        # start menu goes here

        while playing:
            # game loop here
            game.run()

        #     # pg.display.flip()
        #     # clock.tick(5*setting.getFps())
        # if not game.in_game:  # Vérifier si vous êtes dans le menu principal
        #     # draw_graph()

if __name__ == "__main__":
    main()

