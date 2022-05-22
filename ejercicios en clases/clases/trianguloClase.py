# Se quiere crear una clase Cuenta la cual se caracteriza por tener asociado un número de cuenta y un saldo
# disponible. Además, se puede consultar el saldo disponible en cualquier momento, recibir depósitos y pagar
# gastos.
# Crear además una clase Persona, que se caracteriza por un carnet y una o más cuentas bancarias. La Persona
# puede tener asociada hasta 3 cuentas bancarias, y debe tener un método que permite añadir cuentas (hasta 3
# que es el máximo).
lista= []
class Cuenta:
  def __init__(self, numeroDeCuenta, saldoDisponible):
    self.numeroDeCuenta = numeroDeCuenta
    self.saldoDisponible = saldoDisponible
    lista.append(self.numeroDeCuenta)
    print(len(lista))
  def consultarSaldo(self):
    saldo = self.saldoDisponible
    print(saldo)

  def recibirDeposito(self, deposito):
    self.deposito = deposito
    saldo_actual = self.saldoDisponible + self.deposito
    print(saldo_actual)

  def pagarGastos(self, pago):
    saldo= self.saldoDisponible - pago
    print(saldo)

class Persona(Cuenta):
  def __init__(self, numeroDeCuenta, saldoDisponible, carnet):
    Cuenta.__init__(self, numeroDeCuenta, saldoDisponible)
    self.carnet = carnet

  def crearCuentas(self, numeroDeCuenta):
    self.numeros_cuentas = numeroDeCuenta
    cuentas_disponible = 3 - len(lista)

    if self.numeros_cuentas <= cuentas_disponible:
      for i in range(self.numeros_cuentas):
        lista.append(int(input("ingrese cuenta:")))
    else:
      print("Error: ha alcanzado su maximo de cuntas.")
    return lista

print("Bienvenido a banco BBB:")
numero_cuenta = int(input("N° Cuenta: "))
saldo_disponible= int(input("Saldo disponible: "))
numero_carnet= int(input("N° Carnet: "))
persona = Persona(numero_cuenta,saldo_disponible,numero_carnet)
n_cuenta = int(input(f"Ingrese numero de cuenta a crear (Maximo:{3-len(lista)})?: \n"))
print(persona.crearCuentas(n_cuenta),persona.saldoDisponible)