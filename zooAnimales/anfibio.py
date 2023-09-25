from zooAnimales.animal import Animal
class Anfibio(Animal):
    ranas=0
    salamandras=0
    _listado = []
    def __init__(self,nombre,edad,habitat,genero,colorPiel,venenoso):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPiel=colorPiel
        self._venenoso=venenoso
        Anfibio._listado.append(1)
    @classmethod
    def cantidadAnfibios(cls):
        return len(Anfibio._listado)
    def movimiento(self):
        return "saltar"
    def crearRana(nombre,edad,genero):
        frog = Anfibio(nombre,edad,"selva",genero,"rojo",True)
        Anfibio.ranas+=1
        return frog
    def crearSalamandra(nombre,edad,genero):
        salamandra = Anfibio(nombre,edad,"selva",genero,"negro y amarillo",False)
        Anfibio.salamandras+=1
        return salamandra
    def getColorPiel(self):
        return self._colorPiel
    def isVenenoso(self):
        return self._venenoso
    