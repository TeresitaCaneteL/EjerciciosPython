"""crear un programa que pida al usuario un numero par del 2 al 100.....
si este es impar debe volver a preguntar el numero,
cuando ingrese un numero par....debe
imprimir en pantalla todos los pares siguientes hasta el numero 100. """


num1 = int(input("ingrese numero par: "))
if num1 % 2 != 0:
  num1=int(input("ingrese un nuevo numero: "))
  for i in range(num1, 100):
    if i % 2 == 0:
        print(i, num1)
else:
  for i in range(num1, 100):
    if i % 2 == 0:
        print(i, num1)
