class Animal:
    _totalAnimales=0
    def __init__(self,nombre,edad,habitat,genero):
        Animal._totalAnimales +=1
        self._nombre=nombre
        self._edad=edad
        self._habitat=habitat
        self._genero=genero
        self._zona=None
    def movimiento(self):
        return "desplazarse"
    def totalPorTipo():
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.ave import Ave
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil
        from zooAnimales.anfibio import Anfibio
        return "Mamiferos: "+str(Mamifero.cantidadMamiferos)+"\n"+"Aves: "+str(Ave.cantidadAves)+"\n"+"Reptiles: "+str(Reptil.cantidadReptiles)+"\n"+"Peces: "+str(Pez.cantidadPeces)+"\n"+"Anfibios: "+str(Anfibio.cantidadAnfibios)
    def toString(self):
        if self._zona == None:
            return "Mi nombre es "+self._nombre+", tengo una edad de " +str(self._edad)+", habito en " +self._habitat+" y mi genero es "+self._genero
        else:
            return "Mi nombre es "+self._nombre+", tengo una edad de " +str(self._edad)+", habito en " +self._habitat+" y mi genero es "+self._genero+", la zona en la que me ubico es "+self._zona.getNombre()+", en el "+self._zona.getZoo()

    def getNombre(self):
        return self._nombre
    def setNombre(self,nombre):
        self._nombre = nombre
    def getEdad(self):
        return self._edad
    def setEdad(self,edad):
         self._edad = edad
    def getHabitat(self):
        return self._habitat
    def setHabitat(self,habitat):
        self._habitat =habitat
    def getGenero(self):
        return self._genero
    def setGenero(self,genero):
        self._genero = genero
    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales
    @classmethod
    def setTotalAnimales(cls,totalAnimales):
        cls._totalAnimales=totalAnimales
    def setZona(self,zona):
        self._zona = zona