"""3.- Crear un programa que inicialice una lista
con 10 valores aleatorios (del 1 al 10) y posteriormente
 muestre en pantalla cada elemento de la lista junto con
 su cuadrado y su cubo."""
import random
import math
lista=[]
for i in range(10):
  lista.append(random.randint(1,10))
for i in lista:
  print(i,"Al cuadrado: ",pow(i,2),"al cubo: ",pow(i,3))






