from Tiles.tiles import Tile
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Tiles.Bob import Bob
    # from Tiles.Food import Food
    # from Tiles.tiles import Tile


class GameControl:
    instance = None
    #initialisation of grids:
    def __init__(self):
        self.grid = list[list[Tile]]
        self.nbBobs = 0
        self.nbBobsSpawned = 0
        self.listBobs = list['Bob']

        self.currentTick = 0
        self.currentDay = 0

    def setMap(self, map):
        self.grid = map
    def getMap(self):
        return self.grid
    @staticmethod
    def getInstance():
        if GameControl.instance is None:
            GameControl.instance = GameControl()
        return GameControl.instance

    # def update():




