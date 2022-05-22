"""
class Automovil():
  def __init__(self,matricula,marca,kilometros,gasolina):
    self.matricula = matricula
    self.marca = marca
    self.kilometros = kilometros
    self.gasolina = gasolina
  def __str__(self):
    return
MATRICULA\t{}
MARCA\t\t{}
KILOMETROS\t\t{}
GASOLINA\t{}.format(self.matricula, self.marca, self.kilometros,self.gasolina)
  def avanzar(self,num_kilometros):
    self.kilometros += num_kilometros
class Auto(Automovil)
auto1=Automovil('qw-2333','remault',21.90,30.20)
auto1.avanzar(90)
auto2=Automovil('qw-4555','citroen',19.90,20.20)
auto1.avanzar(50)
"""
# Crea la clase Automovil que contenga las siguientes propiedades o atributos:
# matrícula (string)
# marca (string)
# kilometros_recorridos (float)
# gasolina (float)
# La clase tendrá un método llamado avanzar() que recibirá como argumento el número de kilómetros
# a conducir y sumará los kilómetros recorridos al valor del atributo
#El usuario debe tener la posibilidad de crear 2 instancias de esa clase, ingresando el los datos de ambos vehiculos

class Automovil():

  def __init__(self,matricula,marca,kilometros_recorridos,gasolina):
    self.matricula = matricula
    self.marca = marca
    self.kilometros_recorridos = kilometros_recorridos
    self.gasolina = gasolina

  def avanzar(self,numero_kilometros):
    self.kilometros_recorridos += numero_kilometros
    kilometros_avanzados = ("\nSu Automóvil marca {} con matrícula [{}] ha recorrido {} km y tiene {} L de gasolina.\n")
    print(kilometros_avanzados.format(self.marca, self.matricula.upper(),self.kilometros_recorridos,self.gasolina))


print("Ingrese datos para Automóvil N° 1")
matricula = input("Ingrese Matricula: ")
marca = input("Ingrese Marca: ")
kilometros = float(input("Ingrese Kilometros recorridos: "))
gasolina = float(input("Ingrese cantidad de gasolina: "))
cuanto_avanzara = float(input("Ingrese kilometros ha recorrer: "))

auto1 = Automovil(matricula,marca,kilometros,gasolina)
auto1.avanzar(cuanto_avanzara)



print("Ingrese datos para Automóvil N° 2")
matricula = input("Ingrese Matricula: ")
marca = input("Ingrese Marca: ")
kilometros = float(input("Ingrese Kilometros recorridos: "))
gasolina = float(input("Ingrese cantidad de gasolina: "))
cuanto_avanzara = float(input("Ingrese kilometros ha recorrer: "))

auto2 = Automovil(matricula,marca,kilometros,gasolina)
auto2.avanzar(cuanto_avanzara)





"""

auto1 = Automovil("hj-yu-21","Mercedes",21.90,30.23)
auto1.avanzar(90)

auto2 = Automovil("ry-ei-10","Citroen",10.10,12.0)
auto2.avanzar(190)


"""