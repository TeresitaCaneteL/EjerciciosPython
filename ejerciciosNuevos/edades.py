"""1.- Crear un programa que guarde los nombres y la edades de
los alumnos de un curso. la idea es que se introduzca el
nombre y la edad de cada alumno. El proceso de lectura de datos
terminará cuando se introduzca como nombre un asterisco (*)
Al finalizar se mostrará los siguientes datos:
Todos lo alumnos mayores de edad.
Los alumnos mayores (los que tienen más edad)"""
data = []
i = 0
while i < 2:

        nombre = input('Nombre: ')
        edad = int(input('edad: '))
        data.append({"nombre": nombre, "edad": edad})
        i+=1
        if nombre == "*":
          break
        else:
          edad =[nombre['nombre']
          for nombre in data
          if nombre['edad'] >= 18]
          print("Alumnos mayores: ")
          for e in data:
            print(*e.values())
