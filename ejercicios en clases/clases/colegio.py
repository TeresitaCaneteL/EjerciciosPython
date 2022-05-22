colegios=[]
class Minueduc:
  def __init__(self,nombre, direccion):
    self.direccion=direccion
    self.telefono=telefono
    self.correo=correo

def agregarColegio(cantidadColegio):
  cantidadColegio=int(input("ingrese cantidad: "))
  for x in range(cantidadColegio):
    colegios.append(input("ingrese nombre: "))
  return colegios

class Colegio:
  def  __init__(self,nombre,direccion, telefono,ganaciaAnual,numProfesores,numAlumnos,administrativos):
    self.nombre=nombre
    self.direccion=direccion
    self.telefono=telefono
    self.ganaciaAnual=ganaciaAnual
    self.numProfesores = numProfesores
    self.numAlumnos = numAlumnos
    self.administrativos = administrativos
class Persona():
  def __init__(self, nombre, rut,edad):
    self.nombre = nombre
    self.rut = rut
    self.edad = edad

class Alumnos(Persona):
  def __init__(self, nombre, rut,edad,idCurso,curso):
    Persona.__init__(self,nombre, rut, edad)
    self.idCurso = idCurso
    self.curso = curso
class PersonalAseo(Persona):
  def __init__(self, nombre, rut,edad,idAseo,cargo):
    Persona.__init__(self, nombre,rut,edad)
    self.idAseo = idAseo
    self.cargo = cargo
class Vigilancia(Persona):
  def __init__(self, nombre, rut,edad,idVigilante,cargo):
    Persona.__init__(self, nombre, rut,edad)
    self.idVigilante = idVigilante
    self.cargo = cargo
class Administrativos(Persona):
   def __init__(self, nombre, rut,edad,idAdmin,cargo):
    Persona.__init__(self, nombre, rut,edad)
    self.idAdmin = idAdmin
    self.cargo= cargo
class Profesores(Persona):
   def __init__(self, nombre, rut,edad,idProfesor,asignatura):
    Persona.__init__(self, nombre, rut,edad)
    self.idProfesor = idProfesor
    self.asignatura = asignatura
class Departamento:
  def __init__(self, nombre,profesores):
    self.nombre = nombre
    # self.idDepartamento= idDepartamento2
    # self.personaAseo = personaAseo
    # self.vigilancia = vigilancia
    # self.administrativos = administrativos
    self.profesores = profesores

# profesor1=Profesores("lol",1111,23,0,"asignatura")
# personaAseo1=PersonalAseo("lol",1111,23,0,"asignatura")
# dpto1=Departamento("Carlos",profesor1)
# profesor1=Profesores("uwu",1111,23,0,"b")
print(agregarColegio(1))






