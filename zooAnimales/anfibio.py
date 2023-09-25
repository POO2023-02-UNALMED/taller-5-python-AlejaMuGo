from zooAnimales.animal import Animal
class Anfibio(Animal):
    ranas=0
    salamandras=0
    _listado = []
    def __init__(self,nombre,edad,habitat,genero,colorPiel,venenoso):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPiel=colorPiel
        self._venenoso=venenoso
        Anfibio._listado.append(self)
    @classmethod
    def cantidadAnfibios(cls):
        return Anfibio._listado.length
    def movimiento(self):
        return "saltar"
    @classmethod
    def crearRana(cls,nombre,edad,genero):
        frog = Anfibio.__init__(nombre,edad,"selva",genero,"rojo",True)
        ranas+=1
        return frog
    @classmethod
    def crearSalamandra(cls,nombre,edad,genero):
        salamandra = Anfibio.__init__(nombre,edad,"selva",genero,"negro y amarillo",False)
        salamandras+=1
        return salamandra
    def getColorPiel(self):
        return self._colorPiel
    def isVenenoso(self):
        return self._venenoso
    