precio = []
def precioAlto(precio):
  precioA = 0
  for x in range(len(precio)):
    if (precio[x] > precioA):
      precioA = precio[x]
  return precioA
def productosnueve(precio):
  p = 0
  for x in range(len(precio)):
    if(precio[x] == 990):
      p = p + 1
  return p

def descuentos(precio):
  d = []
  for x in range(len(precio)):
    if(precio[x] >= 9990):
      d.insert(x,precio[x] * 0.07)
  return d

def total(precio,descuentos):
  t = []
  for x in range(len(precio)):
    t.append(precio[0] - descuentos[x])
  return t
for x in range(5):
  precio.insert(x,float(input("ingrese valor: ")))
alto = precioAlto(precio)
prod = productosnueve(precio)
desc = descuentos(precio)
tot = total(precio,desc)

print("los precios son:",precio)
print("el precio mas alto es: ",alto)
print("Producos 990: ", prod)
print("descuentos: ",desc)
print("el total del producto:",tot)