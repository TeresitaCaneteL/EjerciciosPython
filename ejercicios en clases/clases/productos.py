class Producto:
  def __init__(self,referencia,nombre,precio,descripcion):
    self.referencia = referencia
    #self.tipo = tipo
    self.nombre = nombre
    self.precio = precio
    self.descripcion = descripcion
    #self.productor = productor
    #self.autor = autor
  def __str__(self):
    return """
REFERENCIA\t{}
NOMBRE\t\t{}
PRECIO\t\t{}
DESCRIPCION\t{}""".format(self.referencia, self.nombre, self.precio,self.descripcion)

class Adorno(Producto):
  pass
a = Adorno('001','vaso',1500,'vaso con diseño')
class Alimento(Producto):
  productor=""
  distribuidor=""
  def __str__(self):
    return """
REFERENCIA\t{}
NOMBRE\t\t{}
PRECIO\t\t{}
DESCRIPCION\t{}
DISTRIBUIDOR\t{}
PRODUCTOR\t{}""".format(self.referencia, self.nombre, self.precio,self.descripcion,self.productor,self.distribuidor)

al=Alimento('0020','papas',1500,'papa chilota')
al.productor='Chiloe.sa'
al.distribuidor='Chiloe.sa'
class Libro(Producto):
 autor=""
 def __str__(self):
    return """
REFERENCIA\t{}
NOMBRE\t\t{}
PRECIO\t\t{}
DESCRIPCION\t{}
AUTOR\t\t{}""".format(self.referencia, self.nombre, self.precio,self.descripcion,self.autor)

li=Libro('0030','Dune',15000,'Ciencia Ficcion')
li.autor='Frank'
productos=[a,al,li]
#for x in productos:
  #print(x,'\n')
 # print(x.nombre,x.referencia)
for i in productos:
  if(isinstance(i,Adorno)):
    print(i.nombre,i.referencia)
  elif(isinstance(i,Alimento)):
    print(i.nombre,i.referencia,i.productor)
  elif(isinstance(i,Libro)):
    print(i.nombre,i.referencia,i.autor)
  def rebajado(p, rebaja):
    p.precio = p.precio - (p.precio/100 * rebaja)
    return p
rebajar= rebajado(al, 30)
print(rebajar)






