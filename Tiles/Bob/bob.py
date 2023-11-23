# For path pinding purposes
from typing import Optional
from Tiles.tiles import Tile
from GameControl.gameControl import GameControl
from view.texture import loadBobImage
import random
from GameControl.settings import *
# from Tiles.Food.food import Food
# We need a function that search for the source of energy in the map ( both bob and tiles ): We need to call the visionTiles function
# We need a function that compare the mass of the other bob ( call the other tile ) 
# Function that make bob move according to the vision, the memory and the predator 
class Bob: 
    def __init__( self, id: 'int' = 0  ):
        self.energy = 100
        self.energyMax = 200
        self.mass = 1
        self.memory = Optional[Tile]; 
        self.vision: 'int' = 0
        self.velocity = 1
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
        self.TargetTile = self.setRandomTile()
        self.NextTile = self.HuntNextTile()

    def initiateNextTiles(self):
        self.TargetTile = self.setTargetTile()
        self.NextTile = self.setNextTile()

    def eat(self, other: 'Bob'):
        if self.energy + other.energy <=  self.energyMax:
            self.energy += other.energy # need rework here
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
        if self.energy != self.energyMax:
            preyBobs = self.getPraysInListBob(self.CurrentTile.getBobs())
            if ( preyBobs == []):
                pass
            else:
                unluckyBob = self.getSmallestPrey(preyBobs)
                if ( unluckyBob == None):
                    pass
                else:
                    self.eat(unluckyBob)
        else: pass

        
    def reproduce(self):
        newBob = Bob(random.randint(0, 1000))
        newBob.energy = 50
        newBob.mass = random.uniform(self.mass - VAR_MASS, self.mass + VAR_MASS)
        newBob.velocity = random.uniform(self.velocity - VAR_VELO, self.velocity + VAR_VELO)
        newBob.spawn(self.CurrentTile)
        self.energy = 150
        
    def interact(self):
        self.Consumefood() # si possible
        # needto Have sex if possible 
        if ( self.energy == self.energyMax):
            self.reproduce() # si possible
        
    def getPraysInListBob(self, listBob: list['Bob']) -> list['Bob']:
        if ( listBob == []):
            return None
        else:
            preyBob : list['Bob'] = None
            for bob in listBob:
                if ( bob.mass * 3 / 2 < self.mass):
                    preyBob.append(bob)
            return preyBob
    def getSmallestPrey(self, listPray: list['Bob']) -> 'Bob':
        preyBob = self.getPraysInListBob(listPray)
        if ( preyBob == None):
            return None
        else:
            smallestBob = preyBob[0]
            for bob in preyBob:
                if ( bob.mass < smallestBob.mass):
                    smallestBob = bob
            return smallestBob
    
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
    
    def HuntNextTile(self):
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
    def setRandomTile(self):     
        nearbyTiles = self.CurrentTile.getNearbyTiles(0)
        return random.choice(nearbyTiles)
        # return GameControl.getInstance().getMap()[0][0]
        pass
        # there are many logic here
    def move(self):
        self.CurrentTile.removeBob(self)
        self.NextTile.addBob(self)
        self.CurrentTile = self.NextTile
        # self.interact()
        # self.Hunt()
        # pred = self.NearestPredatorTarget()
        # if ( pred != None):
        #     self.Run
        # else:
        #     self.Hunt
        self.TargetTile = self.setRandomTile()
        self.NextTile = self.HuntNextTile()
        
    def Hunt(self):
        Target = self.getLargestFoodTiles()
        if ( Target != None):
            self.TargetTile = Target
            self.NextTile = self.HuntNextTile()
        else:
        # We find prey :
            Prey = self.getSmallestPrey(self.getPraysInListBob(self.getNearbyBobs()))
            if Prey != None:
                self.TargetTile = Prey.CurrentTile
                self.NextTile = self.HuntNextTile()
            else:
                self.TargetTile = self.setRandomTile()
                self.NextTile = self.HuntNextTile()

        
    # def SpotSmallestPrey(self) -> 'Bob':
    #     preyBob = self.getPraysInListBob(self.getNearbyBobs())
    #     if ( preyBob == None):
    #         return None
    #     else:
    #         smallestBob = preyBob[0]
    #         for bob in preyBob:
    #             if ( bob.mass < smallestBob.mass):
    #                 smallestBob = bob
    #         return smallestBob

    def chooseTargetTile(self):
        pass


    def getMostEnergyPreyBob(self):
        NearbyPrays = self.getPraysInListBob(self.getNearbyBobs)
        target = NearbyPrays[0]
        for prey in NearbyPrays:
            if prey.energy > target.energy : 
                target = prey
            else: pass
        return target
    

            

    def getLargestFoodTiles(self) -> list['Tile']:
        NearTiles = self.CurrentTile.getNearbyTile(self.vision)
        NearTiles.append(self.CurrentTile)
        seenFood = []
        for tile in NearTiles:
            if ( tile.getEnergy() != 0):
                seenFood.append(tile)
        if ( seenFood == []):
            return None
        else:
            largestFoodTile = seenFood[0]
            for foodTile in seenFood:
                if ( foodTile.getEnergy() > largestFoodTile.getEnergy()):
                    largestFoodTile = foodTile
            return largestFoodTile
    def getNearbyBobs(self) -> list['Bob']:
        NearTiles = self.CurrentTile.getNearbyTile(self.vision)
        NearTiles.append(self.CurrentTile)
        seenBobs = []
        for tile in NearTiles:
            if ( tile.listBob != []):
                for bob in tile.listBob:
                    seenBobs.append(bob)
            else: pass
        return seenBobs
    def HuntNextTile(self):
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
    
        



        
        

