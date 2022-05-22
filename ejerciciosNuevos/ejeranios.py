"""1.- Crear un programa que pida el
año actual (2022) y un año cualquiera y que
escriba cuántos años han pasado desde ese año o
cuántos años faltan para llegar a ese año.
cuando la diferencia sea solo de 1 año escribir un mensaje en pantalla que informe que falta 1 año o que paso 1 año
"""

cant=0
anioA = int(input("ingrese año actual: "))
anio = int(input("ingrese año a eleccion: "))
if anio < anioA:
      cant = anioA-anio
      if cant==1:
        print("Ha pasado solo un año")
      else:
        print("Han pasado:",cant,"años")

elif anio > anioA:
        cant = anio-anioA
        if cant==1:
          print("falta solo un año")
        else:
           print("Faltan:",cant,"años")

