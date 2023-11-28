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
        self.vision: 'int' = VISION
        self.velocity = 1
        self.id = id
        self.alive = True
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
        self.TargetTile = self.CurrentTile
        self.NextTile = self.CurrentTile

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
        energy = self.CurrentTile.getEnergy()
        if ( energy == 0):
            pass
        else:
            print("Spot food energy = ", energy, "Current Energy is ", self.energy)
            if(self.energy < FOOD_MAX_ENERGY):
                if ( self.energy + energy < FOOD_MAX_ENERGY):
                    self.energy += energy
                    self.CurrentTile.foodEnergy = 0
                else:
                    self.CurrentTile.foodEnergy -= (self.energyMax - self.energy)
                    self.energy = FOOD_MAX_ENERGY


        # if self.energy != self.energyMax:
        #     preyBobs = self.getPraysInListBob(self.CurrentTile.getBobs())
        #     if ( preyBobs == None):
        #         pass
        #     else:
        #         unluckyBob = self.getSmallestPrey(preyBobs)
        #         if ( unluckyBob == None):
        #             pass
        #         else:
        #             self.eat(unluckyBob)
        # else: pass
        while ( self.energy != self.energyMax):
            preyBobs = self.getPraysInListBob(self.CurrentTile.getBobs())
            if ( preyBobs == []):
                break
            else:
                unluckyBob = random.choice(preyBobs)
                self.eat(unluckyBob)

        
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
            return []
        else:
            preyBob : list['Bob'] = []
            for bob in listBob:
                if ( bob.mass * 3 / 2 < self.mass):
                    preyBob.append(bob)
            return preyBob
    def getSmallestPreys(self, listPray: list['Bob']) -> 'Bob':
        preyBob = self.getPraysInListBob(listPray)
        if ( preyBob == []):
            return None
        else:
            smallestMass = preyBob[0]
            for bob in preyBob:
                if ( bob.mass < smallestMass.mass):
                    smallestMass = bob
            return smallestMass
    
    def dyingBob(self):
        GameControl.getInstance().diedBobs.append(self)
        self.alive = False
        # self.CurrentTile.removeBob()


    def getBobTexture(self):
        return loadBobImage()["Bob"]

    def getCurrentTile(self) -> Tile:
        return self.CurrentTile
    def getNextTile(self) -> Tile:
        return self.NextTile

    # def die(self):
    #     self.CurrentTile.removeBob(self)
    #     GameControl.getInstance().removeBob(self)
        
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

    def move(self):
        self.CurrentTile.removeBob(self)
        self.NextTile.addBob(self)
        self.CurrentTile = self.NextTile
        self.energy -= 3
        self.interact()
        # print("interacting")
        if ( self.energy <= 0):
            # print("At tick ", GameControl.getInstance().currentTick, " Bob ", self.id, " died")
            self.die()
        # print("At tick ", GameControl.getInstance().currentTick, " Bob ", self.id, " moved to ", self.CurrentTile.gridX, self.CurrentTile.gridY)
        self.Hunt()


        # self.interact()
        # self.Hunt()
        # pred = self.NearestPredatorTarget()
        # if ( pred != None):
        #     self.Run
        # else:
        #     self.Hunt
        # self.TargetTile = self.setRandomTile()
        # self.NextTile = self.HuntNextTile()
        


    def Hunt(self):
        Target = self.getLargestAndNearestFoodTile()
        if ( Target != None):
            self.TargetTile = Target
            self.NextTile = self.HuntNextTile()
        else:
        # We find prey :
            Prey = self.getSmallestPreys(self.getPraysInListBob(self.getNearbyBobs()))
            if Prey != None:
                self.TargetTile = Prey.CurrentTile
                self.NextTile = self.HuntNextTile()
            else:
                self.TargetTile = self.setRandomTile()
                self.NextTile = self.HuntNextTile()
    
    def getLargestAndNearestFoodTile(self) -> Tile:
        # Get the list of nearby tiles
        NearbyTiles = self.CurrentTile.getNearbyTiles(self.vision)
        NearbyTiles.append(self.CurrentTile)
        # Get the list of food tiles
        seenFood: list['Tile'] = []
        for tile in NearbyTiles:
            if ( tile.getEnergy() != 0):
                seenFood.append(tile)
        if ( seenFood == []): #seen food is list of spotted food tiles
            return None
        else:
            # Get the largestFoodTile
            energy = seenFood[0].getEnergy()
            largestFoodTiles: list['Tile'] = []
            for foodTile in seenFood:
                if ( foodTile.getEnergy() > energy):
                    energy = foodTile.getEnergy()
                else: pass
            for foodTile in seenFood:
                if ( foodTile.getEnergy() == energy):
                    largestFoodTiles.append(foodTile)
                else: pass
            # Get the nearestFoodTiles
            distance = Tile.distanceofTile(self.CurrentTile, largestFoodTiles[0])
            nearestLargeFoodTiles : list['Tile'] = []
            for tile in largestFoodTiles:
                if ( Tile.distanceofTile(self.CurrentTile, tile) < distance):
                    distance = Tile.distanceofTile(self.CurrentTile, tile)
            for tile in largestFoodTiles:
                if ( Tile.distanceofTile(self.CurrentTile, tile) == distance):
                    nearestLargeFoodTiles.append(tile)
                else: pass
            #random the nearestFoodTile in the list
            return random.choice(nearestLargeFoodTiles)
        

    def getNearbyBobs(self) -> list['Bob']:
        NearTiles = self.CurrentTile.getNearbyTiles(self.vision)
        NearTiles.append(self.CurrentTile)
        seenBobs: list['Bob'] = []
        for tile in NearTiles:
            if ( tile.listBob != []):
                for bob in tile.listBob:
                    seenBobs.append(bob)
            else: pass
        return seenBobs        
            

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


    # def getMostEnergyPreyBob(self):
    #     NearbyPrays = self.getPraysInListBob(self.getNearbyBobs)
    #     target = NearbyPrays[0]
    #     for prey in NearbyPrays:
    #         if prey.energy > target.energy : 
    #             target = prey
    #         else: pass
    #     return target
    
            

    # def getLargestFoodTiles(self) -> list['Tile']:
    #     NearTiles = self.CurrentTile.getNearbyTile(self.vision)
    #     NearTiles.append(self.CurrentTile)
    #     seenFood = []
    #     for tile in NearTiles:
    #         if ( tile.getEnergy() != 0):
    #             seenFood.append(tile)
    #     if ( seenFood == []): #seen food is list of spotted food tiles
    #         return None
    #     else:
    #         listLargestFoodTiles = []
    #         largestFoodTile = seenFood[0]
    #         for foodTile in seenFood:
    #             if ( foodTile.getEnergy() > largestFoodTile.getEnergy()):
    #                 largestFoodTile = foodTile
    #         return largestFoodTile

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
    
        



        
        

