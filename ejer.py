""" Realizar un programa que conste de una clase llamada Estudiante,
que tenga como atributos el nombre y la nota del alumno. Definir los métodos
para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado
de la nota y si ha aprobado o no """


class Estudiante:

    def __init__(self,nombre_es, nota_es):
        self.nombre = nombre_es
        self.nota = nota_es

    def aprobo(self):
        if self.nota <= 2.99:
            print(f"{self.nombre} no se aprobó la nota")
        elif 3.0 <= self.nota <= 5.00:
            print(f"hola {self.nombre} su nota final es {self.nota} y aprobo")
        else:
            print(f"{self.nombre} ingrese la nota en los parametros")

obj = Estudiante("Emersson", 3.9)

obj.aprobo()