peso = []
est = []
imc = []
def calcularImc():
   for x in range(10):
    peso.insert(x,float(input("Ingrese peso: ")))
    est.insert(x,float(input("Ingrese estatura: ")))
    imc.insert(x,(peso[x] / est[x] ** 2))
    if (imc[x] >= 18.5 and imc[x] <= 24.9):
        print("El peso es: ",peso)
        print("La estatura es: ", est)
        print("El imc es: ",imc)
        print("Situación: Normal, promedio")
    elif (imc[x] >= 25 and imc[x] <= 29.9):
            print("El peso es: ",peso)
            print("La estatura es: ",est)
            print("El imc es: ",imc)
            print("Situación:Sobrepeso, aumentado")
    elif(imc[x] >= 30 and imc[x] <= 34.9):
      print("El peso es: ",peso)
                print("La estatura es: ",est)
                print("El imc es: ",imc)
                print("Situación:Obesidad grado I, moderado")
    elif (imc[x] >= 35 and imc[x] <= 39.9):
                    print("El peso es: ",peso)
                    print("La estatura es: ",est)
                    print("El imc es: ",imc)
                    print("Situación: Obesidad grado II, severo")
    elif (imc[x] >= 40):
                        print("El peso es: ",peso)
                        print("La estatura es: ",est)
                        print("El imc es: ",imc)
                        print("Situación: Obesidad grado III, muy severo")
