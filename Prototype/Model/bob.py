# from .logicMap import LogMap

class Bob ( ):
    def __init__(self, coordX, coordY):
        self.coordX = coordX
        self.coordY = coordY  

    def update(self, vectX, vectY):
        self.coordX += vectX
        self.coordY += vectY
    
    
        
{ "1": bob; }

bob = Bob( 1, 1 )