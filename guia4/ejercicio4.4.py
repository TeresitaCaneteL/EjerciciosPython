#crear una funcion que permita el ingreso de 5 palabras,
#funcion que permita contar cuantas letras tiene cada palabra
palabra = []
def contarcaracteres(palabra):
    for x in range(len(palabra)):
       print(palabra[x],"\n",len(palabra[x]))
for  x in range(5):
  palabra.append(input("ingrese palabra:"))
contarcaracteres(palabra)
