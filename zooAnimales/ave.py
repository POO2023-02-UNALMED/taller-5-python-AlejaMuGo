from animal import Animal
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
        return Ave._listado.length
    def movimiento(self):
        return "volar"
    @classmethod
    def crearHalcon(cls,nombre,edad,genero):
        halcon = Ave.__init__(nombre,edad,"montanas",genero,"cafe glorioso")
        halcones+=1
        return halcon
    @classmethod
    def crearAguila(cls,nombre,edad,genero):
        aguila = Ave.__init__(nombre,edad,"montanas",genero,"blanco y amarillo")
        aguilas+=1
        return aguila
    def getColorPlumas(self):
        return self._colorPlumas
    

