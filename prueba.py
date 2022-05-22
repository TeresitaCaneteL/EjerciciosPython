volts=[]
ohms=[]
ampers=[]
for x in range(2):
  volts.insert(x,float(input("ingrese voltage")))
  ohms.insert(x,float(input("ingrse valor de omh")))
  ampers.insert(x,volts[x]/ohms[x])

  print(volts)
  print(ohms)
  print(ampers)