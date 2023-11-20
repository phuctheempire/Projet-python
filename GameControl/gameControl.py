from ..Model.tiles import Tile
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..Model.Bob import Bob
    from ..Model.Food import Food
    from ..Model.tiles import Tile


class gameControl:
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
    

    # def update():




