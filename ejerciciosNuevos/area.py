"""
 3.- Cree un programa que pregunte primero
al usuario si se quiere calcular el área de un
triángulo o la de un círculo. Si se indica que se
quiere calcular el área de un triángulo, el programa
tiene que pedir entonces la base y la altura y escribir
el área. Si se contesta que se quiere calcular el área
de un círculo, el programa tiene que pedir entonces el
 radio y escribir el área.
"""
import math
area=0.0
ingreso = input("que desea calcular?: ")
if ingreso == "triangulo":
  base=float(input("ingrese base "))
  alt=float(input("ingrese altura "))
  area=round(float(base*alt/2),2)
  print("El area es:",area)
elif ingreso == "circulo":
  radio=float(input("ingrese radio "))
  area=round(float(math.pi * pow(radio,2)),2)
  print("El area es:",area)

