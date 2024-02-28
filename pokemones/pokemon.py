class Pokemon:
    def __init__(self, nombre,  salud ,nivel):
        self.__color = None
        self.nombre = nombre
        self.__salud = None
        self.__nivel = None


        self.salud = salud
        self.nivel = nivel

    @property
    def salud(self):
        return self.__salud

    @salud.setter
    def salud(self,salud):
        if 0 <= salud <= 100:
            self.__salud = salud
        else:
            print('la salud debe ser de 0 hasta 100')

    @property
    def nivel(self):
        return self.__nivel

    @nivel.setter
    def nivel(self, nivel):
        if 0 < nivel < 1000:
            self.__nivel = nivel
        else:
            print ("su nivel debe ser mayor a 0 y menor a 1000")

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color):
         self.__color = color


    def atacar(self):
        if self.nivel:
            print(f"{self.nombre} hace un daño de {self.nivel / 2}")