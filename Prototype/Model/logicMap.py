from .bob import Bob
import random

class logicMap:
    def __init__(self, lengthX, lengthY):
        self.logicMap = self.createLogicMap(lengthX, lengthY)
        self.lengthX = lengthX
        self.lengthY = lengthY
        self.implementBob()
        print(self.logicMap)

    def createLogicMap(self, lengthX, lengthY):
        logicMap = []
        for x in range(lengthX):
            logicMap.append([])
            for y in range(lengthY):
                logicMap[x].append()
        return logicMap

    def implementBob(self):
        for _ in range(10):
            x = random.randint(0, self.lengthX -1)
            y = random.randint(0, self.lengthY -1)
            bob = Bob(x,y)
            self.logicMap[x][y].append(bob)
    




    