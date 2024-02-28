""" Realizar un programa en el cual se declaren dos valores enteros por teclado
utilizando el método _init_. Calcular después la suma, resta, multiplicación y división.
 Utilizar un método para cada una e imprimir los resultados obtenidos.
  Llamar a la clase Calculadora. """



class Calculadora:

    def __init__(self, numero_1, numero_dos):
        self.num = numero_1
        self.num2 = numero_dos

    def sumar(self):
        print(self.num + self.num2)

    def res(self):
        print(self.num - self.num2)

    def multi(self):
        print(self.num * self.num2)

    def div(self):
        print(self.num / self.num2)


num = int(input("ingrese un numero "))

num2 = int(input("ingrese un numero "))

calcular = Calculadora(num,num2)

calcular.sumar()
calcular.res()
calcular.multi()
calcular.div()




