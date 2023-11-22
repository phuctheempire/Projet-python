# For path pinding purposes
from typing import Optional
from Tiles.tiles import Tile
from GameControl.gameControl import GameControl
from view.texture import loadBobImage
import random
# from Tiles.Food.food import Food
# We need a function that search for the source of energy in the map ( both bob and tiles ): We need to call the visionTiles function
# We need a function that compare the mass of the other bob ( call the other tile ) 
# Function that make bob move according to the vision, the memory and the predator 
class Bob: 
    def __init__( self, id: 'int' = 0, velocity = 1, mass = 1  ):
        self.energy = 100
        self.energyMax = 200
        self.mass = mass
        self.memory = Optional[Tile]; 
        self.vision: 'int' = 0
        self.velocity = velocity
        self.id = id
        self.CurrentTile : Optional[Tile] = None
        self.TargetTile : Optional[Tile] = None
        self.NextTile : Optional[Tile] = None
        self.PredatorTile : Optional[Tile] = None
        # self.huntOrRun: 'int'= 1 # 1 for hunt, 0 for run
        # self.targetTile : Optional[Tile] = None
        self.memory: 'int' = 0
        self.memoryTile = Optional[Tile]
        self.image = self.getBobTexture()

    def spawn(self, tile: 'Tile'):
        self.CurrentTile = tile
        self.CurrentTile.addBob(self)
        GameControl.getInstance().addBob(self)
        self.TargetTile = self.setTargetTile()
        self.NextTile = self.setNextTile()

    def eat(self, other: 'Bob'):
        if self.energy + other.energy <=  self.energyMax:
            self.energy += other.energy
            other.die()
        else:
            self.energy = self.energyMax
            other.die()

    def Consumefood(self):
        food = self.CurrentTile.getFood()
        if ( food == None):
            pass
        else:
            if(self.energy == self.energyMax):
                pass
            else:
                if ( self.energy + food.energy <= self.energyMax):
                    self.energy += food.energy
                    food.energy = 0
                else:
                    self.energy = self.energyMax
                    food.energy -= self.energyMax - self.energy
        bobs = self.CurrentTile.getBobs()
        if ( bobs == []):
            pass
        else:
            unluckyBob = random.choice(self.getPrayInSameTile())
            self.eat(unluckyBob)
            
            
    def getPrayInSameTile(self):
        bobs = self.CurrentTile.getBobs()
        if ( bobs == []):
            pass
        else:
            preyBob : list['Bob'] = None
            for bob in bobs:
                if ( bob.mass * 3 / 2 < self.mass):
                    preyBob.append(bob)
            return preyBob
        
    
    def die(self):
        self.CurrentTile.removeBob(self)
        GameControl.getInstance().removeBob(self)

    def getBobTexture(self):
        match self.mass:
            case 1: return loadBobImage()["Bob"]

    def getCurrentTile(self) -> Tile:
        return self.CurrentTile
    def getNextTile(self) -> Tile:
        return self.NextTile
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
        else: return None

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
    
    def setNextTile(self):
        #Temporary
        target = self.TargetTile
        if self.CurrentTile == self.TargetTile:
            return self.TargetTile
        elif ( target == self.CurrentTile.getNearbyTiles(0)):
            return target
        else:
            (x,y) = Tile.CountofTile(target, self.CurrentTile)
            if ( y == 0 and x != 0 ):
                if ( x > 0):
                    return self.CurrentTile.getDirectionTiles("Right")
                else:
                    return self.CurrentTile.getDirectionTiles("Left")
            elif ( x == 0 and y != 0):
                if ( y > 0):
                    return self.CurrentTile.getDirectionTiles("Up")
                else:
                    return self.CurrentTile.getDirectionTiles("Down")
            else:
                if ( x > 0 and y > 0):
                    upright = (self.CurrentTile.getDirectionTiles("Up"), self.CurrentTile.getDirectionTiles("Right"))
                    return random.choice (upright)
                elif ( x > 0 and y < 0):
                    downRight = (self.CurrentTile.getDirectionTiles("Down"), self.CurrentTile.getDirectionTiles("Right"))
                    return random.choice (downRight)
                elif ( x < 0 and y > 0):
                    upLeft = (self.CurrentTile.getDirectionTiles("Up"), self.CurrentTile.getDirectionTiles("Left"))
                    return random.choice(upLeft)
                else:
                    downLeft = (self.CurrentTile.getDirectionTiles("Down"), self.CurrentTile.getDirectionTiles("Left"))
                    return random.choice(downLeft)
    def setTargetTile(self):     
        nearbyTiles = self.CurrentTile.getNearbyTiles(0)
        return random.choice(nearbyTiles)
        # return GameControl.getInstance().getMap()[0][0]

        # there are many logic here
    def move(self):
        self.CurrentTile.removeBob(self)
        self.NextTile.addBob(self)
        self.CurrentTile = self.NextTile
        self.TargetTile = self.setTargetTile()
        self.NextTile = self.setNextTile()
        
    # def update(self):
    #     self.move()
    #     self.setNextTile()


        
        

