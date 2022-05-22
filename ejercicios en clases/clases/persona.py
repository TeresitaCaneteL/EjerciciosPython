class persona:
  def __init__(self, nombre,edad, rut):
    self.nombre = nombre
    self.edad= edad
    self.rut = rut
  def mostrar(self):
    mostracion = ("Hola soy {}, mi edad es {} y mi rut es {}")
    print(mostracion.format(self.nombre, self.edad, self.rut))
  def esMayorDeEdad(self):
    if self.edad > 18:
      mayor = ("{},es mayor de edad")
      print(mayor.format(self.nombre, self.edad, self.rut))
    else:
      menor=("{},es menor de edad")
      print(menor.format(self.nombre, self.edad, self.rut))

persona1=persona('Pablo',21,'11111111' )
persona2=persona('jose',15,'2222222' )
persona1.mostrar()
persona1.esMayorDeEdad()
persona2.mostrar()
persona2.esMayorDeEdad()

