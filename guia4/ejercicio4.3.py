#crear codigo que permita ingrsar 10 numeros:
#funcion que permita contar pares negativos y pares positivos
#funcion que permita contar impares pos impares neg
#funcion que permita contar cantidad de ceros
num = []
def numparespos(num):
  ppos = 0
  for x in range(len(num)):
   if(num[x] % 2 == 0 and num[x] >0):
      ppos = ppos + 1
  return ppos
def numparesneg(num):
   pneg = 0
   for x in range(len(num)):
     if(num[x] % 2 == 0 and num[x] <0):
       ppneg = ppneg + 1
       return ppneg
def numimparespos(num):
  ipos = 0
  for x in range(len(num)):
    if(num[x] % 2 != 0 and num[x] >0):
      ipos = ipos + 1
  return ipos
def numimparesneg(num):
  ineg = 0
  for x in range(len(num)):
    if(num[x] % 2 != 0 and num[x] <0):
      ineg = ineg + 1
  return ineg
def ceros(num):
  c = 0
  for x in range(len(num)):
    if(num[x] == 0):
      c = c + 1
  return c
for x in range(10):
  num.insert(x,float(input("ingrese numero: ")))
  ppositivos = numparespos(num)
  pnegativos = numimparesneg(num)
  imppositivos = numimparespos(num)
  impnegativos = numimparesneg(num)
  crs = ceros(num)

print("los pares positivos son: ",ppositivos)
print("los pares negativos son: ",pnegativos)
print("los impares positivos son: ",imppositivos)
print("los impares negativos son: ",impnegativos)
print("los ceros son: ",crs)

