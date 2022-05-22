"""Crear un programa que permita a una empresa de cine almacenar en su base de datos información
sobre nuevas películas y estrenos. Suponga que cada nueva película se compone de: titulo, director,
género y duración. Al final se debe mostrar la información detallada de cada película, por lo que se
debe crear la clase Película y el usuario encargado agregar al menos 5 películas para después
mostrarlas por pantalla
"""
class Peliculas():
  def __init__(self,titulo,director,genero,duracion):
    self.titulo=titulo
    self.director=director
    self.genero=genero
    self.duracion=duracion

  def __str__(self):
      return  """Nombre de la Película {}:
      Director:\t{}
      Genero:\t{}
      Duración:\t{}""".format(self.titulo, self.director,self.genero,self.duracion)
def agregar():
  lista=[]
  num=int(input('Cuantas Peliculas quiere agregar: '))
  for x in range(num):
    nombre=input("Nombre de la pelicula: ")
    direct=input("Nombre del director: ")
    genero=input("Que genero: ")
    duracion=input("Duracion de la pelicula: ")
    if nombre == '' :
      print("Debe agregar una pelicula")

    else:
      p=Peliculas(nombre,direct,genero,duracion)
      lista.append(p)
  return lista

l=[]
l=agregar()
for i in l:
    print("\n",i,"\n")






