"""1.- Crear un programa en python que haga lo siguiente:
 una función que reciba una frase y devuelva un diccionario
 con las palabras que contiene y su longitud."""

def diccionario(frase):
  frase=frase.split(" ")
  dic={}
  for i in frase:
    if i != " ":
      dic[i]=len(i)
  print(dic)
frase=input("ingrese frase:")
diccionario(frase)