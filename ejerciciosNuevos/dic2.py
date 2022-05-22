"""2.- Crear un programa que pregunte al usuario su nombre,
 edad, dirección y teléfono y lo guarde en un diccionario.
  Después debe mostrar por pantalla el mensaje <nombre>
  tiene <edad> años, vive en <dirección> y su número de teléfono
  es <teléfono>."""
usuario={}
nom=input("ingrese nombre: ")
edad=input("ingrese edad: ")
dire=input("ingrese direccion: ")
telefono=input("ingrese telefono: ")
usuario["nombre"]=nom
usuario["edad"]=edad
usuario["direccion"]=dire
usuario["telefono"]=telefono
print("Nombre:",usuario['nombre'], "tiene ", usuario['edad']," años, ","vive en ",usuario['direccion'],"su numero es ",usuario['telefono'])
"""
nombre = input('¿Cómo te llamas? ')
edad = input('¿Cuántos años tienes? ')
direccion = input('¿Cuál es tu dirección? ')
telefono = input('¿Cuál es tu número de teléfono? ')
persona = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}
print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['direccion'], 'y su número de teléfono es', persona['telefono'])
"""