#permita el ingreso de un precio
#mayor a 9990 15%
#ingresar en la primera posicion
#en la sig desc aplicado

precio = []
total = 0.0
desc = 0.0
precio.append(int(input("valor del producto:")))
if (precio[0] >= 9990):
      desc = (precio[0] * 15)/ 100
      total = precio[0] - desc
else:
      print("no tiene descuento")

print ("precio",precio)
print("descuento",desc)
print("total",total)
