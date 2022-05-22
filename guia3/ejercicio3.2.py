#crear un codigo que permita ingresar 5 num
#contar los pares
#contar impares
#contar ingresados
def pares (vector):
  p = 0
  for x in range (len(vector)):
    if(vector[x] % 2 == 0 and vector[x] !=0):
      p = p + 1
  return p
def impares (vector):
  i = 0
  for x in range(len(vector)):
    if(vector[x] % 2 != 0):
      i = i + 1
  return i
def ceros(vector):
  c = 0
  for x in range(len(vector)):
    if(vector[x] == 0):
      c = c + 1
  return c
nums = []
for x in range(5):
  nums.insert(x,float(input("ingrese numero: ")))
  prs = pares(nums)
  imp = impares(nums)
  crs = ceros(nums)

print("los pares son: ",prs)
print("los impares son: ",imp)
print("los ceros son: ",crs)

