# For path pinding purposes
from typing import Optional
from ..tiles import Tile
from ..Food.food import Food
# We need a function that search for the source of energy in the map ( both bob and tiles ): We need to call the visionTiles function
# We need a function that compare the mass of the other bob ( call the other tile ) 
# Function that make bob move according to the vision, the memory and the predator 
class Bob: 
    def __init__( self, id: 'int' = 0,  ):
        self.energy = 100
        self.mass: 'int' = 1
        self.memory = Optional[Tile]; 
        self.vision = Optional[list[Tile]]
        self.velocity = -1
        self.id
        self.CurrentTile = Optional[Tile]
        self.PreviousTile = Optional[Tile]
        self.Nexttile = Optional[Tile]
        self.huntOrRun: 'int'= 1 # 1 for hunt, 0 for run
        self.targetTile = Optional[Tile]

    
    def getNearbyBobs(self) -> list['Bob']:
        NearTiles = self.CurrentTile.getNearbyBobs(self.vision)
        seenBobs = []
        for listBobs in NearTiles:
            if ( listBobs != []):
                for bob in listBobs:
                    seenBobs.append(bob)

        return seenBobs
    
    def getNearbyFood(self) -> list['Food']:
        NearTiles = self.CurrentTile.getNearbyFood(self.vision)
        seenFood = []
        for listFood in NearTiles:
            if ( listFood != []):
                for food in listFood:
                    seenFood.append(food)

        return seenFood
    
    def getTargetTile(self):
        

        
        

