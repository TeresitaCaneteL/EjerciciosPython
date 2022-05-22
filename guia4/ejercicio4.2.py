#crear codigo que permita el ingreso de 5 notas
#funcion que permita ver notas insuficientes, notas suficientes. Promedio, aprobado y reprobado.

def notasbym():
    sufc = 0
    insuf = 0
    for x in range(len(notas)):
        if (notas[x] >= 4):
            sufc += 1
        else:
             insuf += 1
    print ("suficientes:",sufc)
    print ("insuficientes:",insuf)
def Notamayor(notas):
  nalta = 0.0
  for x in range(len(notas)):
    if (notas[x] > nalta):
      nalta = notas[x]
  return nalta
def promedio ():
  prom = 0.0
  for x in range(len(notas)):
    prom = prom + notas[x]
  pr = prom / len(notas)
  return pr
  if pr >= 3.95:
     print ("aprobado")
  else:
     print ("reprobado")
notas = []
for x in range(5):
    notas.insert(x,float(input("ingrese nota: ")))
print ("notas:",notas)
print ("nota mas alta:",Notamayor(notas) )
print ("su promedio es:",promedio())
notasbym()