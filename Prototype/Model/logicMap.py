from .bob import Bob

class logicMap:
    def __init__(self, lengthX, lengthY):
        self.logicMap = self.createLogicMap(lengthX, lengthY)
        self.lengthX = lengthX
        self.lengthY = lengthY

    def createLogicMap(self, lengthX , lengthY):
        logicMap = []
        for x in range(lengthX):
            logicMap.append([])
            for y in range(lengthY):
                logicMap[x].append([])
    




    