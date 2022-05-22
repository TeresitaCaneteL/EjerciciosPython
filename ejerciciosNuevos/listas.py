"""2.- Crear Programa que declare tres listas ‘lista1’, ‘lista2’
 y ‘lista3’ de cinco enteros cada uno, pida valores para ‘lista1’
  y ‘lista2’ y calcule lista3=lista1+lista2."""
lista1=[]
lista2=[]
lista3=[]
for i in range(5):
  lista1.insert(i,int(input("ingrese numero1:")))
  lista2.insert(i,int(input("ingrese numero2:")))
  lista=sum(lista1+lista2)
  lista3.append(lista)
  print(lista3)