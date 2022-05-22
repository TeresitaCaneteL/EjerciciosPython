"""Se pide ingresar al usuario solo un numero entre el 1 y el 9,
si ingresa cualquier otro numero debe salir un mensaje que informe
de un numero errone y debe existir la posibilidad de ingresar nuevamente otro numero.
di una vez se ingrese un numero del 1 al 9....se
debe desplegar en pantalla la tabla de multiplicar
del 0 al 10 con el numero ingresado por el usuario"""

num1=int(input("ingrese numero: "))
if num1 >= 10:
  print("formato invalido")
  num1=int(input("ingrese un nuevo numero: "))
  for x in range(0,11):
      print(num1*x)
elif num1 <=10:
    for x in range(0,11):
      print(num1*x)