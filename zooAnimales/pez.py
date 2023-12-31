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
        return len(cls._listado)
    def movimiento(self):
        return "nadar"
    def crearSalmon(nombre,edad,genero):
        salmon = Pez(nombre,edad,"oceano",genero,"rojo",6)
        Pez.salmones+=1
        return salmon
    def crearBacalao(nombre,edad,genero):
        bacalao = Pez(nombre,edad,"oceano",genero,"gris",6)
        Pez.bacalaos+=1
        return bacalao
    def getColorEscamas(self):
        return self._colorEscamas
    def getCantidadAletas(self):
        return self._cantidadAletas