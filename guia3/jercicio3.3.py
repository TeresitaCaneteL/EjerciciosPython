def promedio (vector):
  s = 0.0
  for x in range(len(vector)):
    s = s + vector[x]
  pr = s / len(vector)
  return pr
def mayor(vector):
  max = 0.0
  for x in range(len(vector)):
    if (vector[x] > max):
      max = vector[x]
  return max
notas = []
for x in range(7):
    notas.insert(x,float(input("ingrese nota: ")))

print("\n las notas ingresadas son: ",notas)
print("la nota mas alta obtenida es:",mayor(notas))
print("el promedio es:",promedio(notas))