class Automovil():

  def __init__(self,color,marca,modelo,num_puertas,placa):
    self.color = color
    self.marca = marca
    self.modelo = modelo
    self.num_puertas = num_puertas
    self.placa = placa


  def agrega(self):

    detalle_auto = ("\n Automovil color : {}\n marca : {}\n modelo : {}\n numero de puertas : {} \n placa N : {}.\n")
    print(detalle_auto.format(self.color, self.marca, self.modelo, num_puertas, self.placa))

print("Ingrese datos para automovil n° 1")
color = (input("Ingrese color : "))
marca = (input("Ingrese marca : "))
modelo = (input("Ingrese modelo : "))
num_puertas = (input("Ingrese numero de puertas : "))
placa = (input("Ingrese placa patente : "))
auto1 = Automovil(color, marca, modelo, num_puertas, placa)

print("Ingrese datos para automovil n° 2")
color = (input("Ingrese color : "))
marca = (input("Ingrese marca : "))
modelo = (input("Ingrese modelo : "))
num_puertas = (input("Ingrese numero de puertas : "))
placa = (input("Ingrese placa patente : "))
auto2 = Automovil(color, marca, modelo, num_puertas, placa)

print("Ingrese datos para automovil n° 3")
color = (input("Ingrese color : "))
marca = (input("Ingrese marca : "))
modelo = (input("Ingrese modelo : "))
num_puertas = (input("Ingrese numero de puertas : "))
placa = (input("Ingrese placa patente : "))
auto3 = Automovil(color, marca, modelo, num_puertas, placa)

print("Ingrese datos para automovil n° 4")
color = (input("Ingrese color : "))
marca = (input("Ingrese marca : "))
modelo = (input("Ingrese modelo : "))
num_puertas = (input("Ingrese numero de puertas : "))
placa = (input("Ingrese placa patente : "))
auto4 = Automovil(color, marca, modelo, num_puertas, placa)

print("Ingrese datos para automovil n° 5")
color = (input("Ingrese color : "))
marca = (input("Ingrese marca : "))
modelo = (input("Ingrese modelo : "))
num_puertas = (input("Ingrese numero de puertas : "))
placa = (input("Ingrese placa patente : "))
auto5 = Automovil(color, marca, modelo, num_puertas, placa)


auto1.agrega()
auto2.agrega()
auto3.agrega()
auto4.agrega()
auto5.agrega()
