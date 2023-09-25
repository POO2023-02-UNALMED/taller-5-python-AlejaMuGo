from zooAnimales.animal import Animal
class Reptil(Animal):
    iguanas=0
    serpientes=0
    _listado = []
    def __init__(self,nombre,edad,habitat,genero,colorEscamas,largoCola):
        super().__init__(nombre,edad,habitat,genero)
        self._colorEscamas=colorEscamas
        self._largoCola=largoCola
        Reptil._listado.append(self)
    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)
    def movimiento(self):
        return "reptar"
    def crearIguana(nombre,edad,genero):
        iguana = Reptil(nombre,edad,"humedal",genero,"verde",3)
        Reptil.iguanas+=1
        return iguana
    def crearSerpiente(nombre,edad,genero):
        snake = Reptil(nombre,edad,"jungla",genero,"blanco",1)
        Reptil.serpientes+=1
        return snake
    def getColorEscamas(self):
        return self._colorEscamas
    def getLargoCola(self):
        return self._largoCola