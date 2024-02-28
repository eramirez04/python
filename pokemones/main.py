from pokemon import Pokemon
from electrico import TipoElectrico

class Pikachu(TipoElectrico):

    def __init__(self,nombre,salud,nivel,voltaje,longitud):
        TipoElectrico.__init__(self,nombre,salud,nivel,voltaje)
        self.__longitud = None
        self.longitud = longitud

    @property
    def longitud(self):
        return self.__longitud

    @longitud.setter
    def longitud(self, longitud):
        if longitud >= 0:
            self.__longitud = longitud
        else:
            print("no parametros de cola")


    def longitud_cola(self):
        pass


