from pokemon import Pokemon


class TipoFuego(Pokemon):
    def __init__(self,nombre,nivel,salud, temperatura_max):
        Pokemon.__init__(self,nombre,nivel,salud)
        self.__temperatura = None
        self.temperatura = temperatura_max

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, temperatura):
        if 0 < temperatura < 2000:
            self.__temperatura = temperatura
        else:
            print("excede los limites de temperatura")

    def fuego(self):
        if self.temperatura:
            print(f"{self.nombre} hace un daño con fuego de {(self.nivel * self.temperatura) - 40}")


class Charmander(TipoFuego):

    def __init__(self, nombre, nivel,salud,temperatura_max):
        super().__init__(nombre, nivel,salud,temperatura_max)


charmander = Charmander("charmander",90,20, 900000)
charmander.fuego()

