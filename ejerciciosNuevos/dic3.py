"""3.- Crear un programa en python que pida un número por teclado
 y que cree un diccionario cuyas claves sean desde el número 1
 hasta el número indicado, y los valores sean los cuadrados de
  las claves.
"""
dic={}
num = int(input('ingrese numero: '))
for x in range(1,num):
  clave = x
  val = x**2
  dic={'clave': clave, 'val': val}
  print(dic)
