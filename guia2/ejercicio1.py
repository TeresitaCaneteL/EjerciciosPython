#crear una rutina que permita ingresar 10 grados celsious
#debe obtener grados fahrenheit para cada grado celsious
#grados kelvin desde los fahrenheit obtenidos
#coversion celsious a faharenheit y de fahrenheit a kelvin
#libreria math

celsious = []
fahrenheit = []
kelvin = []
for x in range(10):
  celsious.insert(x,float(input("ingrese grados celcious")))
  fahrenheit.insert(x,celsious[x] * 1.8 + 32)
  kelvin.insert(x,(((fahrenheit[x]-32)*5)/9)+ 273.15)
print ("grados celcious: ", celsious)
print ("en grados fahrenheit son: ", fahrenheit)
print ("en grados kelvin son: ", kelvin)