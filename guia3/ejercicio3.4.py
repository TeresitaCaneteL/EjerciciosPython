def iva(vector):
  i = []
  for x in range(len(vector)):
    i.insert(x,vector[x] * 0.19)
  return i
def descuentos(vector):
  d = []
  for x in range(len(vector)):
    if(vector[x] >= 19990):
      d.insert(x,vector[x] * 0.15)
    else:
      d.insert(x,vector[x] * 0.1)
  return d
def total(v1,v2,v3):
  t = []
  for x in range(len(v1)):
    t.insert(x,v1[x] + v2[x] - v3[x])
  return t

vneto = []
for x in range(3):
  vneto.insert(x,float(input("ingrese valor neto: ")))
imps = iva(vneto)
desc = descuentos(vneto)
tots = total(vneto,imps,desc)

print("valor neto: ",vneto)
print("iva 19%: ",imps)
print("descuentos: ",desc)
print("totales",tots)