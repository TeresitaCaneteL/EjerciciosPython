"""Crear una clase Automóvil, a través de la cual se pueda agregar
el color del Automóvil, la marca, el modelo, el número de puertas y
la placa. Crear el constructor del coche, así como los métodos que
considere necesarios. Se deben crear 5 instancias de esta clase,
en donde el usuario introduzca manualmente la información de estos
 vehículos para que sean agregados al inventario y luego imprimirlos
 en pantalla
"""
class Automovil:

  def __init__(self,tipo,color,marca,modelo,numPuerta,placa):
    self.tipo= tipo
    self.color = color
    self.marca = marca
    self.modelo = modelo
    self.numPuerta = numPuerta
    self.placa = placa
  def __str__(self):
        return  """Usted acaba de crear un {}:

        Color\t{}
        Marca\t{}
        Modelo\t{}
        Puertas\t{}
        Placa\t{}""".format(self.tipo, self.color,self.marca,self.modelo,self.numPuerta,self.placa)

def agregar():
  lista=[]
  num=int(input('cuantos quiere agregar: '))
  for x in range(num):
    tipo=input("que quiere agregar: Auto(1),Moto(2),Camion(3),Camioneta(4),Furgon(5): ")
    color=input("que color: ")
    marca=input("que marca: ")
    modelo=input("que modelo: ")
    puertas=input("Cuantas puertas: ")
    placa=input("numero de placa: ")
    if tipo.isnumeric() and int(tipo) == 1:
      a=Automovil("Auto",color,marca,modelo,puertas,placa)
      lista.append(a)
    elif tipo.isnumeric() and int(tipo) == 2:
      m=Automovil('Moto',color,marca,modelo,puertas,placa)
      lista.append(m)
    elif tipo.isnumeric() and int(tipo) == 3:
      c=Automovil('Camion',color,marca,modelo,puertas,placa)
      lista.append(c)
    elif tipo.isnumeric() and int(tipo) == 4:
      ca=Automovil('Camioneta',color,marca,modelo,puertas,placa)
      lista.append(ca)
    elif tipo.isnumeric() and int(tipo) == 5:
      f=Automovil('Furgon',color,marca,modelo,puertas,placa)
      lista.append(f)
  return lista

l=[]
l=agregar()
for i in l:
    print("\n",i,"\n")





