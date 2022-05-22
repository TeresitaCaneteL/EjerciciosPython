class Humano(): #Creamos la clase Humano

  def __init__(self, nombre,edad, ocupacion): #Definimos el atributo edad y nombre
    self.edad = edad # Definimos que el atributo edad, sera la edad asignada
    self.nombre = nombre # Definimos que el atributo nombre, sera el nombre asigs
    self.ocupacion = ocupacion
  def presentar(self):
    presentacion = ("Hola soy {}, mi edad es {} y mi ocupación es {}") #Mensaje
    print(presentacion.format(self.nombre, self.edad, self.ocupacion)) #Usamos FORMA
  def contratar(self, puesto): #añadimos un nuevo parámetro en el método
    self.puesto = puesto
    print ("{} ha sido contratado como {}".format(self.nombre, self.puesto))
    self.ocupacion = puesto #Ahora cambiamos el atributo ocupación
persona1=Humano('tere',21,'desocupado' )
persona1.presentar()
print(persona1.nombre)
