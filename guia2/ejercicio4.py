#calcular el volumen para 3 cilindros
import math
altura = []
radio = []
volumen = []
for x in range(3):
  altura.insert(x,float(input("ingrese altura")))
  radio.insert(x,float(input("ingrese radio")))
  volumen.insert(x,((math.pi * pow(radio[x],2)) * altura[x]))
  print ("la altura es: ",altura)
  print ("el radio es:",radio)
  print ("el volumen es:",volumen)







