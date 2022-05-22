"""Escriba un programa para ingresar las notas de los alumnos
de un curso, pregunte al usuario cuántos datos
ingresará, a continuación le pida que ingrese las notas uno
por uno, y finalmente entregue como salida
cuántas notas ingresadas son mayores que el promedio."""
def notas():
  numNotas=[]
  mayor=[]
  num=int(input("ingrese cantidad de notas: "))
  for x in range(0, num):
    numNotas.insert(x,float(input("ingrese notas: ")))
    prom=round(sum(numNotas)/num,1)
  for i in numNotas:
    if i >= prom:
       mayor.append(i)
  print("Promedio: ",prom)
  print("Notas mayor al promedio: ",len(mayor)," : ",*mayor)
notas()