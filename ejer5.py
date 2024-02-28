""" Crear un programa con
 tres clases Universidad, con atributos
  nombre (Donde se almacena el nombre de
  la Universidad). Otra llamada Carerra, con los atributos especialidad
  (En donde me guarda la especialidad de un estudiante).
   Una ultima llamada Estudiante, que tenga como atributos su nombre y edad.
    El programa debe
imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona. """



class Universidad:
    def __init__(self,nombre_u):
        self.__nombreU = nombre_u


class Carrera(Universidad):
    def __init__(self, carrera, uni, especialidad):
        Universidad.__init__(self,uni)
        self.__carrera = carrera
        self.__especialidad = especialidad


class Estudiante(Carrera):

    def __init__(self,nombre_es, edad, carrera, uni,especialidad):
        Carrera.__init__(self,carrera,uni,especialidad)
        self.nombre = nombre_es
        self.edad = edad

    def informacion(self):
        print(f"hola soy {self.nombre} estudio en la univerdidad del {self._Universidad__nombreU}",
              f"tengo {self.edad} años y estoy en la especialidad de {self._Carrera__especialidad}")


estudiante = Estudiante("Emersson",23 ,"ingenieria","Sena","ciberseguridad")


estudiante.informacion()