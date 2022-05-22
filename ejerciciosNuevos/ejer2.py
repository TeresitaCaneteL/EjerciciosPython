"""Crea un programa que pregunte al usuario
 cuántos números se van a introducir, pida esos
 números, y muestre un mensaje por pantalla cada
 vez que un número no sea mayor que el primero.
ese es el numero 1"""
num=int(input("cuantos numero quiere?: "))
for x in range(num):
  num2=int(input("indique un numero: "))
  if num2 < num:
    print(num2,"no es mayor que",num)




