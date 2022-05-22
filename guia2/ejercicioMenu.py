def invalido():
     print("opcion invalida")

def suma(n1,n2):
    r = n1 + n2
    return r

def resta(n1,n2):
    r = n1 - n2
    return r

def multiplica(n1,n2):
    r = n1 * n2
    return r

def divide(n1,n2):
    if(n2 != 0):
      r = n1 / n2
    else:
      r = 0
def rsuma():
  os.system("clear")
  n1 = float(input("ingrese numero: "))
  n2 = float(input("ingrese numero: "))
  print("el resultado es: ",suma(n1,n2))
def rresta():
  os.system("clear")
  n1 = float(input("ingrese numero: "))
  n2 = float(input("ingrese numero: "))
  print("el resultado es: ",resta(n1,n2))
def rmultiplica():
  os.system("clear")
  n1 = float(input("ingrese numero: "))
  n2 = float(input("ingrese numero: "))
  print("el resultado es: ",multiplica(n1,n2))
def rdivide():
  os.system("clear")
  n1 = float(input("ingrese numero: "))
  n2 = float(input("ingrese numero: "))
  print("el resultado es: ",divide(n1,n2))
op = 1
while op != 0:
     print("calculadora básica")
     print("\n1 -suma-")
     print("\n2 -resta-")
     print("\n3 -multiplicación-")
     print("\n4 -división-")
     print("\n5 -salir-")
     if(op == 1):
       rsuma()
     if(op == 2):
       rresta
     if(op == 3):
       rmultiplicación
     if(op == 4):
       rdivisión
     if(op == 5):
       rsalir


