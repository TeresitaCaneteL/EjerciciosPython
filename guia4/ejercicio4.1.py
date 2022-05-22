#crear un codigo, que permita calcular el vulumen para 3 cilindros.
#debemos obtener: funcion que permita calcular el volumen de los cilindros ingresados.
import math
altura = []
radio = []
volumen = []
def calcularV(alt,ra):
   volumen.insert(x,((math.pi * pow(ra,2) * alt)))
for x in range(3):
   altura.insert(x,float(input("ingrese altura")))
   radio.insert(x,float(input("ingrese radio")))
   calcularV(radio[x],altura[x])
print ("la altura es: ",altura)
print ("el radio es:",radio)
print ("el volumen es:",volumen)

