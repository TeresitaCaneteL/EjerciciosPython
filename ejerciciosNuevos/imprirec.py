"""Crear un programa que pida al usuario
un número entero y muestre por pantalla un
triángulo rectángulo como el que sale en el ejemplo
 que enviare a continuacion"""
num=int(input("ingrese numero "))
for i in range(0,num+1):
  #if num % i != 0:
  for x in range((i*2)-1, 0,-2):
    #x+=(str(i)+(' '))
    print('*',end=' ')
  print('\n')


"""n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")"""

"""Escribir un programa que pida al usuario un número entero
positivo y muestre por pantalla todos los números impares desde
 1 hasta ese número separados por comas.

n = int(input("Introduce un número entero positivo: "))
for i in range(1, n+1, 2):
    print(i, end=", ")

Escribir un programa que pida al usuario un número entero
positivo y muestre por pantalla la cuenta atrás desde ese número
hasta cero separados por comas.
n = int(input("Introduce un número entero positivo: "))
for i in range(n, -1, -1):
    print(i, end=", ")

    """
