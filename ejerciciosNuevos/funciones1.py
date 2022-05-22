"""1.- Crear un programa en python (o modificar el que ya hicieron)
pero que esta vez sea con 2 funciones, que calcule el area de un circulo
y el area de un triangulo con datos ingresados por el usuario"""
import math
def area(r):
    print (round(math.pi*r**2))
radio=int(input("ingrese radio: "))
area(radio)

