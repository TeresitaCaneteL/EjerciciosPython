
lista = []
alumnos=[]
class Colegio:
  def  __init__(self,nombre,direccion, telefono,numProfesores,numAlumnos):
    self.nombre=nombre
    self.direccion=direccion
    self.telefono=telefono
    self.numProfesores = numProfesores
    self.numAlumnos = numAlumnos
  def __str__(self):
        return  """ Es un Colegio:
        Nombre:\t\t{}
        Direccion:\t{}
        Telefono:\t{}
        Numero docentes:{}
        Numero Alumnos:\t{}""".format(self.nombre, self.direccion,self.telefono, self.numProfesores, self.numAlumnos)

  def ver(self):
   print(l.nombre)

class Persona():
  def __init__(self, nombre, rut,edad):
    self.nombre = nombre
    self.rut = rut
    self.edad = edad
  def agregar_p(self):
    tipo=input("Agregar \n(1)Alumno,\n(2)Profesor,\n(3)Personal Aseo,\n(4)Vigilancia,\n(5)Administrativos\n(6)Volver al menu,\nIngrese opción:")
    if tipo == '1':
      print("\nAgregando alumno\n")
      curso= input("indique curso: ")
      idcurso=input("indique id del curso: ")
      al=Alumnos(self.nombre, self.rut,self.edad,curso,idcurso)
      alumnos.append(al)
      print("\nAlumno agregado correctament!!\n")
      agregar(c)


    elif tipo == '2':
      print("\nAgregando profesor\n")
      asig=input("ingrese asignatura: ")
      prof=Profesores(self.nombre,self.rut,self.edad,asig)
      print()
      print("Profesor agregado correctament!!")
    elif tipo == '3':
      cargo=input("ingrese cargo: ")
      p_aseo=Personal_Aseo(self.nombre,self.rut,self.edad,cargo)
      print()
      print("Personal agregado correctament!!")
    elif tipo == '4':
      cargo=input("ingrese cargo: ")
      id_vigi=input("ingrese id de vigilante: ")
      vigi=Vigilancia(self.nombre,self.rut,self.edad,cargo, id_vigi)
      print(vigi)
      print("Personal agregado correctament!!")
    elif tipo == '5':
      cargo=input("ingrese cargo: ")
      id_cargo=input("ingrese id de cargo: ")
      ad=Administrativos(self.nombre,self.rut,self.edad,cargo, id_cargo)
      print()
      print("Personal agregado correctament!!")
    elif tipo == '6':
      agregar(c)

  def buscar(self,rut):
    for i in alumnos:
      if rut == i:
        print('encontrado')
      else:
        print('no encontrado')

class Alumnos(Persona):
  def __init__(self, nombre, rut,edad,curso,id_curso):
    Persona.__init__(self,nombre, rut, edad)
    self.curso = curso
    self.id_curso = id_curso
  def __str__(self):
        return  """ Es alumno:
        Nombre:\t{}
        Rut:\t{}
        Edad:\t{}
        id curso:{}
        Curso:\t{}""".format(self.nombre, self.rut,self.edad,self.curso,self.id_curso)
class Personal_Aseo(Persona):
  def __init__(self, nombre, rut,edad,cargo):
    Persona.__init__(self, nombre,rut,edad)
    self.cargo = cargo
  def __str__(self):
        return  """
        Nombre:\t{}
        Rut:\t{}
        Edad:\t{}
        Cargo:\t{}""".format(self.nombre, self.rut,self.edad,self.cargo)
class Vigilancia(Persona):
  def __init__(self, nombre, rut,edad,idVigilante,cargo):
    Persona.__init__(self, nombre, rut,edad)
    self.idVigilante = idVigilante
    self.cargo = cargo
  def __str__(self):
        return  """
        Nombre:\t{}
        Rut:\t{}
        Edad:\t{}
        Id:\t{}
        Cargo:\t{}""".format(self.nombre, self.rut,self.edad,self.idVigilante,self.cargo)
class Administrativos(Persona):
  def __init__(self, nombre, rut,edad,cargo,idAdmin):
    Persona.__init__(self, nombre, rut,edad)
    self.cargo= cargo
    self.idAdmin = idAdmin
  def __str__(self):
        return  """
        Nombre:\t{}
        Rut:\t{}
        Edad:\t{}
        Cargo:\t{}
        Id:\t{}""".format(self.nombre, self.rut,self.edad,self.cargo,self.idAdmin)

class Profesores(Persona):
  def __init__(self, nombre, rut,edad,asignatura):
    Persona.__init__(self, nombre, rut,edad)
    self.asignatura = asignatura
  def __str__(self):
        return  """
        Nombre:\t{}
        Rut:\t{}
        Edad:\t{}
        Asignatura:\t{}""".format(self.nombre, self.rut,self.edad,self.asignatura)
class Departamento:
  def __init__(self, nombre,profesores):
    self.nombre = nombre
    self.idDepartamento= idDepartamento2
    # self.personaAseo = personaAseo
    # self.vigilancia = vigilancia
    # self.administrativos = administrativos
    self.profesores = profesores

# profesor1=Profesores("lol",1111,23,0,"asignatura")
# personaAseo1=PersonalAseo("lol",1111,23,0,"asignatura")
# dpto1=Departamento("Carlos",profesor1)
# profesor1=Profesores("uwu",1111,23,0,"b")
# print(profesor1.nombre)
# print(agregarColegio(colegios))

#p=int(input("Menu de opciones:\n(1)Añadir Colegio\n(2)Añadir Departameno\n(3)Añadir persona\nElige una opción:"))
#num=int(input('Cuantas Peliculas quiere agregar: '))
c=int(input("Cuantos desea agregar: "))
def agregar(c=1):

  i=1
  while c >= i:
    v=int(input('Menú de opciones\n(1)Agregar datos\n(2)Eliminar\n(3)Buscar\n(4)Listar\n(5)Terminar\nElige una opción:'))
    if v==1:
            nombre=input("indique nombre: ")
            rut=input("rut: ")
            edad=input("edad: ")
            col=Persona(nombre, rut, edad)
            col.agregar_p()
            lista.append(col)
    elif v==2:

      print('eliminar')

    elif v==3:
         print('buscar')
         rut=input('ingrese rut: ')
         col.buscar(rut)

    elif  v==5:
      exit()

    else:
            print("Opcion incorrecta, intentelo de nuevo")
            break
    i= i+1
  return lista
a=[]
a=agregar(c)
# for i in a:
#     print(i,"\n")
#     #i= i+1