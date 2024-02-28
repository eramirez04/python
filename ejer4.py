""" Crear una clase llamada Marino(), con un
método que sea hablar, en donde muestre un mensaje
que diga "Hola...". Luego, crear una clase Pulpo()
que herede Marino, pero modificar el mensaje de hablar
por "Soy un Pulpo". Por último, crear una clase Foca(), heredada de Marino,
pero que tenga un atributo nuevo llamado mensaje y que
muestre ese mensaje como parámetro """


class Marino:
    def hablar(self):
        print("hola")


class Pulpo(Marino):

    def hablar(self):
        print("hola soy el pulpo")

class Foca(Marino):
    def __init__(self,mensaje):
        self.mensaje = mensaje

    def hablar(self,):
        print(f"hola, este el mensaje de la clase foca = '{self.mensaje}'")



pulpo = Foca("creando una nueva foca")

pulpo.hablar()