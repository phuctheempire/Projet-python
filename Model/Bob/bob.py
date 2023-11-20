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
        self.vision: 'int' = 0
        self.velocity = -1
        self.id
        self.CurrentTile = Optional[Tile]
        self.PreviousTile = Optional[Tile]
        self.Nexttile = Optional[Tile]
        self.huntOrRun: 'int'= 1 # 1 for hunt, 0 for run
        self.targetTile = Optional[Tile]
        self.memory: 'int' = 0
        self.memoryTile = Optional[Tile]
        
    def getCurrentTile(self) -> Tile:
        return self.CurrentTile
    
    def getNearbyBobs(self) -> list['Bob']:
        NearTiles = self.CurrentTile.getNearbyTile(self.vision)
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
    
    def ListPredator(self) -> list['Bob']:
        listBobs = self.getNearbyBobs()
        listPredator = []
        for bob in listBobs:
            if ( bob.mass > (3/2)*self.mass):
                listPredator.append(bob)
        if ( listPredator == []):
            self.huntOrRun = 1
        else:
            self.huntOrRun = 0
        return listPredator
    
    def NearestPredatorTarget(self) -> Tile:
        listPredator = self.ListPredator()
        if ( listPredator != []):
            predator = listPredator[0]
            for pred in listPredator:
                if ( Tile.distanceofTile(self.CurrentTile, pred.CurrentTile) < Tile.distanceofTile(self.CurrentTile, predator.CurrentTile)):
                    predator = pred
            return predator.CurrentTile
        else: pass

    def scanForTarget(self) -> Tile:
        listFood = self.getNearbyFood()
        if ( listFood != []):
            temp = listFood[0]
            for food in listFood:
                if ( food.energy > temp):
                    temp = food
            temp.getCurrentTile()
        else:
            listBobs = self.getNearbyBobs()
            temp = listBobs[0]
            for bob in listBobs:
                if ( bob.mass < temp.mass):
                    temp = bob
            temp.getCurrentTile()
    
    def getNextTile(self):
        
        # there are many logic here
        
        

        
        

