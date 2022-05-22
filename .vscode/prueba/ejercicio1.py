#crear codigo que permita calculo de imc para 10 personas
#formula: imc=peso/altura al cuadrado
#obtener situacion
peso = []
altura = []
imc1 = []
def imc(imc):
  for x in range(10):
     imc1.append(peso / pow(altura,2)
      altura.insert(x,float(input("ingrese altura")))
     peso.append(x,float(input("ingrese radio")))
   if imc[x] >= 18 and imc <= 29.9:
    print ("usted tiene un imc normal")
   else:
        (imc[x] >= 25 and imc1 <= 29.9):
   print("usted tiene sobrepeso",imc1)

   if imc[x] >= 30 and imc1 <= 34.9:
    print("usted tiene obesidad grado1")
   else:
    imc[x] >= 35 and imc1 <= 39.9
    print("usted tiene obesidad grado2")
   if imc[x]>= 40:
    print("usted tiene obesidad grado3")

print("peso: ",peso)
print("altura: ",altura)
print("imc ",imc(peso,altura))





