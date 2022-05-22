"""2.- crear un programa que pida al usuario ingresar 5 notas
 de un alumno (notas del 1.0 al 7.0), obtener su promedio y
 mostrar como resultado final si paso o no paso la asignatura
 (minimo para aprobar es el 4.0)"""

promedio = 0.0
notas = []
suma = 0.0

for x in range(3):
  notas.insert(x,float(input("ingrese notas:")))
  suma = suma + notas[x]
promedio = round(float(suma / 3),1)
if(promedio >= 3.9):
  print("aprobado con:",promedio)
else:
    print("reprobado con:",promedio)



