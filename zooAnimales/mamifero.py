from zooAnimales.animal import Animal
class Mamifero(Animal):
    caballos=0
    leones=0
    _listado = []
    def __init__(self,nombre,edad,habitat,genero,pelaje,patas):
        super().__init__(nombre,edad,habitat,genero)
        self._pelaje=pelaje
        self._patas=patas
        Mamifero._listado.append(self)
    @classmethod
    def cantidadMamiferos(cls):
        return Mamifero._listado.length
    def crearCaballo(nombre,edad,genero):
        horse = Mamifero(nombre,edad,"pradera",genero,True,4)
        caballos+=1
        return horse
    def crearLeon(nombre,edad,genero):
        lion = Mamifero(nombre,edad,"selva",genero,True,4)
        leones+=1
        return lion
    def getPatas(self):
        return self._patas
    def isPelaje(self):
        return self._pelaje

