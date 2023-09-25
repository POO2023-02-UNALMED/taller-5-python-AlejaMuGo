from zooAnimales.animal import Animal
class Pez(Animal):
    salmones=0
    bacalaos=0
    _listado = []
    def __init__(self,nombre,edad,habitat,genero,colorEscamas,cantidadAletas):
        super().__init__(nombre,edad,habitat,genero)
        self._colorEscamas=colorEscamas
        self._cantidadAletas=cantidadAletas
        Pez._listado.append(self)
    @classmethod
    def cantidadPeces(cls):
        return Pez._listado.length
    def movimiento(self):
        return "nadar"
    def crearSalmon(self,nombre,edad,genero):
        salmon = Pez.__init__(self,nombre,edad,"oceano",genero,"rojo",6)
        salmones+=1
        return salmon
    def crearBacalao(self,nombre,edad,genero):
        bacalao = Pez.__init__(self,nombre,edad,"oceano",genero,"gris",6)
        bacalaos+=1
        return bacalao
    def getColorEscamas(self):
        return self._colorEscamas
    def getCantidadAletas(self):
        return self._cantidadAletas