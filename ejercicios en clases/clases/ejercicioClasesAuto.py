class Automovil():
  def __init__(self,color,marca,modelo,numPuerta,placa):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.numPuerta = numPuerta
        self.placa = placa
class Auto(Automovil):
  def __init__(self,color,marca,modelo,numPuerta,placa):
        Automovil.__init__(self,color,marca,modelo,numPuerta,placa)

  def __str__(self):
        return  """Es un auto
        Color\t{}
        Marca\t{}
        Modelo\t{}
        Puertas\t{}
        Placa\t{}""".format(self.color, self.marca,self.modelo, self.numPuerta, self.placa)
class Camion(Automovil):
  def __init__(self,color,marca,modelo,numPuerta,placa):
       Automovil.__init__(self,color,marca,modelo,numPuerta,placa)
  def __str__(self):
        return  """Es un camion
        Color\t{}
        Marca\t{}
        Modelo\t{}
        Puertas\t{}
        Placa\t {}""".format(self.color, self.marca,self.modelo, self.numPuerta, self.placa)
c=int(input("cuantos desea agregar: "))
def crear_automovil(c):
  lista=[]
  for x in range(c):
    p=input("que desea agregar: ")
    c=input("Cual es el color: ")
    m=input("Cual es la marca: ")
    mo=input("Que modelo: ")
    np=input("Numero de puertas: ")
    placa=input("Cual es la placa: ")

    if p=='auto':
      auto=Auto(c,m,mo,np,placa)
      lista.append(auto)
    elif p=='camion':
      camion=Camion(c,m,mo,np,placa)
      lista.append(camion)
  return lista
l=[]
l=crear_automovil(c)
for i in l:
    print("\n",i,"\n")

