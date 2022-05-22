#crear rutina que permita el ingreso de 4 valores en watts y 4 valores en ohms
#devolver en ampers

watts = []
ohms = []
ampers = []

for x in range(5):
  watts.insert(x,float(input("ingrese watts:")))
  ohms.insert(x,float(input("ingrese ohms:")))
  ampers.insert(x,watts[x]/ohms[x])
  print (watts)
  print (ohms)
  print (ampers)