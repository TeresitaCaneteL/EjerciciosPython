"""Al ingresar un numero par cualquiera que sea del 2 al 100,
este imprima en pantalla todos los
números pares siguientes, y si ingreso un numero impar cualquiera
sea del 1 al 99 se imprima en
pantalla todos los números impares siguientes hasta el 99."""

def par_impar(numero):
   #numero=int(input("numero: "))
  if numero % 2 == 0:
     print("par")
     for x in range(numero,100,2):
       print(x)
  elif numero % 2 != 0:
     print("impar")
     for i in range(numero,100,2):
       print(i)
num=int(input("ingrese num: "))
par_impar(numero)

"""
Realizar un programa que lea por teclado las 5 notas obtenidas
por un alumno (comprendidas entre
0 y 10). A continuación, debe mostrar todas las notas,
la nota media, la nota más alta que ha sacado
y la menor."""
"""
def notasbym():
  nmenor=0.0
  nalta=0.0
  prom=0.0
  notas = []
  for x in range(5):
    notas.insert(x,float(input("ingrese nota: ")))
  for x in range(len(notas)):
    if (notas[x] > nalta):
      nalta = notas[x]
    else:
      nmenor = min(notas)

  prom=round(sum(notas)/len(notas),1)
  print ("notas:",notas)
  print ("promedio:",prom)
  print ("nota mayor:",nalta)
  print ("nota menor:",nmenor)
notasbym()
"""
"""
Crea un programa que pida un número al usuario un número de mes
(por ejemplo, el 4) y diga
cuántos días tiene (por ejemplo, 30) y el nombre del mes.
Debes usar listas. Para simplificarlo vamos
a suponer que febrero tiene 28 días.
"""
"""
def meses():
  introMeses=[{'num':'1','mes':'enero', 'dias':'31'},{'num':'2','mes':'Febrero', 'dias':'28'},{'num':'3','mes':'marzo','dias':'31'},
  {'num':'4','mes':'abril','dias':'30'},{'num':'5','mes':'mayo','dias':'31'},{'num':'6','mes':'junio','dias':'30'},{'num':'7','mes':'julio','dias':'31'},
  {'num':'8','mes':'agosto','dias':'31'},{'num':'9','mes':'septiembre','dias':'30'},{'num':'10','mes':'octubre','dias':'31'},{'num':'11','mes':'noviembre','dias':'30'},
  {'num':'12','mes':'diciembre','dias':'31'}]
  numMes=input("ingrese numero: ")
  for x in introMeses:
    if x['num'] == numMes:
      print("El mes de ",x['mes'],"tiene ",x['dias']," días")
meses()
"""