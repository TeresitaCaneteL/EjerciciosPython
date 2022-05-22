# crear codigo que permita ingresar 3 grados celsious
def fahrenheit(vector):
  f = []
  for x in range(len(vector)):
    f.insert(x, (vector[x] * 1.8) + 32)
  return f


def kelvin(vector):
    k = []
  for x in range (len(vector)):
      k.insert(x,((5 * (vector[x] - 32) / 9) + 273.15))
  return k
    cel = []
  for x in range (3):
    cel.insert(x,float(input("ingrese grados celcius")))
      fah = fahrenheit(cel)
      kel = kelvin(fah)
      print(cel)
      print(fah)
      print(kel)
