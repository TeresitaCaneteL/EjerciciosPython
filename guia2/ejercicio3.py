#crear rutina que permita ingresar 5 notas
#sacar promedio, aprobado, reprobado, nota alta.
promedio = 0.0
notas = []
nfinal = []
nalta = 0.0
suma = 0.0

for x in range(5):
  notas.insert(x,float(input("ingrese notas:")))
  suma = suma + notas[x]
  if (notas[x] > nalta):
    nalta = notas[x]
promedio = round(float(suma / 5))
#notas.append (promedio)
if(promedio >= 3.9):
  print("aprobado")
else:

  print("Reprobado con:",promedio)
  print("Su nota mas alta es:",nalta)

