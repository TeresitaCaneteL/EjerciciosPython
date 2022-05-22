class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas) #sin necesidad de hacer self a todas las sub clases
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return  """Es un coche
        Color\t\t {}
        Ruedas\t\t {}
        Velocidad\t {}
        Cilindrada\t {}""".format(self.color, self.ruedas, self.velocidad, self.cilindrada)

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        Coche.__init__(self, color, ruedas, velocidad, cilindrada)
        self.carga = carga
    def __str__(self):
        return  """Es una Camioneta
        Color\t\t {}
        Ruedas\t\t {}
        Velocidad\t {}
        Cilindrada\t {}
        Carga\t\t {}""".format(self.color, self.ruedas, self.velocidad, self.cilindrada, self.carga)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, urbana=False, deportiva=False):
        Vehiculo.__init__(self, color, ruedas)
        self.urbana = urbana
        self.deportiva = deportiva

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, urbana=False, deportiva=False, velocidad=None, cilindrada=None):
        Bicicleta.__init__(self, color, ruedas, urbana, deportiva)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

c=int(input("Cuantos Vehiculos desea crear?: "))
def crear_Vehiculos(c=1):
  lista = []
  i=1
  while c>=i:
    v=int(input("Que Vehiculo desea crear, responda 1 para Coche, 2 para Camioneta, 3 para Bicicleta, 4 para Motocicleta: "))
    if v==1:
            co=input("De que color es?: ")
            ru=input("Cuantas ruedas tiene?: ")
            ve=input("Que velocidad maxima alcanza?: ")
            ci=input("Cual es su cilindrada?: ")
            vh=Coche(co, ru, ve, ci)
            lista.append(vh)
    elif v==2:
            co=input("De que color es?: ")
            ru=input("Cuantas ruedas tiene?: ")
            ve=input("Que velocidad maxima alcanza?: ")
            ci=input("Cual es su cilindrada?: ")
            car=input("Cual es su carga maxima?: ")
            cam=Camioneta(co, ru, ve, ci, car)
            lista.append(cam)
    elif v==3:
            co=input("De que color es?: ")
            ru=input("Cuantas ruedas tiene?: ")
            bici = Bicicleta(co, ru)
            ve=input("Es urbana? (responda (y) para si y (n) para no):  ")
            if ve == "y" or ve=="Y":
                bici.urbana=True
            elif ve=="n" or ve=="N":
                bici.deportiva= True
                lista.append(bici)
    elif v==4:
            co=input("De que color es?: ")
            ru=input("Cuantas ruedas tiene?: ")
            motoci = Motocicleta(co,ru)
            ve=input("Es urbana? (responda (y) para si y (n) para no):  ")
            if ve == "y" or ve=="Y":
                motoci.urbana=True
            elif ve=="n" or ve=="N":
                motoci.deportiva= True
            motoci.velocidad=input("Que velocidad maxima alzanza?: ")
            motoci.cilindrada=input("Cual es su cilindraje?: ")
            lista.append(motoci)
    else:
            print("Opcion incorrecta, intentelo de nuevo")
            break
    i= i+1
  return lista
a=[]
a=crear_Vehiculos(c)
for i in a:
    print(i,"\n")
    #i= i+1