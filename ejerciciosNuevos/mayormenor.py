"""
 Crear un programa que solicite al usuario
 dos números enteros y que escriba en pantalla
  si el mayor es múltiplo del menor.
"""
num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese un numero: "))
div=0
if num1 > num2 and num1 % num2 == 0:
  print(num2,"Es multiplo",num1)
elif num2 > num1 and num2 % num1 == 0:
  print(num1,"es multiplo",num2)
else:
    print("no son multiplos")

