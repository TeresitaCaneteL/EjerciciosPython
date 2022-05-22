"""crear un programa que solicite al usuario ingresar un password que
sea guardado en una variable, pregunte confirmacion, si son iguales
debe imprimir menjase en pantalla,si son distintas debe decir en pantalla y dar
opcion de poner la correcta"""

nom=input("ingrese nombre: ")
contraseña=input("ingrese contraseña: ")
ccontraseña=input("confirme contraseña: ")
if contraseña.upper()  == ccontraseña.upper() :
  print(" contraseña correcta, bienvenid@ ", nom)
else:
  print(" contraseña incorrecta")
  ccontraseña=input("ingrese contraseña correcta: ")
  if contraseña.upper()  == ccontraseña.upper():
    print(" contraseña correcta, bienvenid@ ", nom)


