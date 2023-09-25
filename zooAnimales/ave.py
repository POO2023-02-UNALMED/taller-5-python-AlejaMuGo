from zooAnimales.animal import Animal
class Ave(Animal):
    halcones=0
    aguilas=0
    _listado = []
    def __init__(self,nombre,edad,habitat,genero,colorPlumas):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPlumas=colorPlumas
        Ave._listado.append(self)
    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)
    def movimiento(self):
        return "volar"
    def crearHalcon(nombre,edad,genero):
        halcon = Ave(nombre,edad,"montanas",genero,"cafe glorioso")
        Ave.halcones+=1
        return halcon
    def crearAguila(nombre,edad,genero):
        aguila = Ave(nombre,edad,"montanas",genero,"blanco y amarillo")
        Ave.aguilas+=1
        return aguila
    def getColorPlumas(self):
        return self._colorPlumas
    

