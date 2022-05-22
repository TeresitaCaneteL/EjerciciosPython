"""el cifrado cesar consiste en sustituir una letra por la que
viene 3 posiciones mas adelante en el alfabeto"""

def cif_cesar(frase):
  letra='abcdefghijklmnñopqrstuvwxyxABCDEFGHIJKLMNÑOPQRESTUVWXYZ'
  cifrado=''
  i=input('cifrar(c), decifrar(d): ')
  if i == 'c':
    for x in frase:
      if x in letra:
        cifrado += letra[(letra.index(x)+3) % len(letra)]
      else:
        cifrado+=x
  elif i == 'd':
    for x in frase:
      if x in letra:
        cifrado += letra[(letra.index(x)-3) % len(letra)]
      else:
        cifrado+=x

  print(cifrado)
cifrar=input("ingrese texto: ")
cif_cesar(cifrar)