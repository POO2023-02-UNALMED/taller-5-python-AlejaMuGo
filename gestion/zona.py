from zooAnimales.animal import Animal
class Zona:
    def __init__(self,nombre,zoo=None):
        self._nombre=nombre
        self._zoo=zoo
        self._animales=[]
    def agregarAnimales(self,animal):
        self._animales.append(animal)
        animal.setZona(self)
    def cantidadAnimales(self,animal):
        return self._animales.lenght
    def getNombre(self):
        return self._nombre
    def getZoo(self):
        return self._zoo
    def setZoo(self,zoo):
        self._zoo=zoo