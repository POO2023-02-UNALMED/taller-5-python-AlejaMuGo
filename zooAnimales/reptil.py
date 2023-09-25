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
        return Reptil._listado.length
    def movimiento(self):
        return "reptar"
    def crearIguana(self,nombre,edad,genero):
        iguana = Reptil.__init__(self,nombre,edad,"humedal",genero,"verde",3)
        iguanas+=1
        return iguana
    def crearSerpiente(self,nombre,edad,genero):
        snake = Reptil.__init__(self,nombre,edad,"jungla",genero,"blanco",1)
        serpientes+=1
        return snake
    def getColorEscamas(self):
        return self._colorEscamas
    def getLargoCola(self):
        return self._largoCola