def numeros(vector):
  p = 0
  i = 0
  c = 0
  r = []
  for x in range(len(vector)):
    if(vector[x] % 2 == 0 and vector[x] != 0):
      p = p + 1
    if(vector[x] % 2 != 0):
      i = i + 1
    if(vector[x] == 0):
      c = c + 1
  r.append(p)
  r.append(i)
  r.append(c)
  return r
nums = []
for x in range(5):
  nums.insert(x,float(input("ingrese numero")))
print ("pares",numeros(nums).pop(0))
print ("impares",numeros(nums).pop(1))
print ("ceros",numeros(nums).pop(2))