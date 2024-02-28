from pokemon import Pokemon

class TipoElectrico(Pokemon):

    __tipo = "electrico"

    def __init__(self,nombre,nivel,salud,voltaje):
        Pokemon.__init__(self,nombre,nivel,salud)
        self.__voltaje = None
        self.voltaje = voltaje

    @property
    def voltaje(self):
        return self.__voltaje

    @voltaje.setter
    def voltaje(self, aumento_voltaje):
        if aumento_voltaje >= 0:
            self.__voltaje = aumento_voltaje
        else:
            print("el voltaje debe ser mayor a 0")

    def atacar(self):
        if self.nivel and self.voltaje:
            print(f"{self.nombre} hace mas daño {(self.voltaje * self.nivel) / 3}")