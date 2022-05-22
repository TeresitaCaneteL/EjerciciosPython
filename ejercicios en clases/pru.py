lista = []

datos =int(input("Cuantas notas desea ingresar : "))
for x in range(datos):
    nota = float(input("Ingrese las notas a revisar : "))
    lista.append(nota)
    prom = sum(lista)/datos


print("Promedio",prom, "Cantidad de notas:",datos)