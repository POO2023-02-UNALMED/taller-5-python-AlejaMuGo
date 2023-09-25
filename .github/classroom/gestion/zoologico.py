from gestion.zona import Zona
class Zoologico:
    def __init__(self,nombre,ubicacion):
        self._zonas=[]
        self._nombre=nombre
        self._ubicacion=ubicacion
    def agregarZonas(self,zona):
        self._zonas.append(zona)
        zona.setZoo(self)
    def cantidadTotalAnimales(self):
        x = 0
        for i in self._zonas:
            x +=i.cantidadAnimales()
        return x
    def getNombre(self):
        return self._nombre
    def getUbicacion(self):
        return self._ubicacion
    def getZona(self):
        return self._zonas
    
