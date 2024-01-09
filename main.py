import pygame as pg
from GameControl.game import Game
from GameControl.EventManager import show_menu
from pygame.locals import *

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
    
    # implement menus
    show_menu(screen, clock)
    # implement game
    game = Game(screen, clock)

    while running:
        
        # start menu goes here

        while playing:
            # game loop here
            game.run()

if __name__ == "__main__":
    main()

