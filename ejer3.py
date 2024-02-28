""" Crear una clase Fabrica que tenga los atributos de
 Llantas, Color y Precio; luego crear dos clases
 mas que hereden de Fabrica, las cuales son Moto y Carro.
  Crear metodos que muestren la cantidad de llantas,
  color y precio de ambos
 transportes. Por ultimo, crear objetos para cada clase y
 mostrar por pantalla los atributos de cada uno """




class Fabrica:

    def __init__(self,llantas, color, precio):
        self.llanta = llantas
        self.color = color
        self.precio = precio


    @property
    def llantas(self):
        return f"la cantidad de llantas es {self.llanta}"

    @property
    def colors(self):
        return f"el color  es {self.color}"

    @property
    def precios(self):
        return f"el precio es: {self.precio}"


    @llantas.setter
    def llantas(self,llanta):
        if llanta > 1 :
            self.llantas = llanta



class Moto(Fabrica):

    def __init__(self, llantas, color, precio):
        Fabrica.__init__(self,llantas,color, precio)


class Carro(Fabrica):

    def __init__(self, llantas, color, precio):
        Fabrica.__init__(self,llantas,color, precio)

moto = Carro(3,"rojo",431)

hola = moto.precios

print(hola)