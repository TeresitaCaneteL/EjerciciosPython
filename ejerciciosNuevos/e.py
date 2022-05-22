"""3.- Crea un programa con una tupla con los meses del año,
 pide números al usuario, si el numero esta entre 1 y la longitud
  máxima de la tupla, muestra el contenido de esa posición sino
  muestra un mensaje de error. El programa termina cuando el
  usuario introduce un cero."""
meses = ("enero", "febrero", "marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")
num = int(input('ingrese numero: '))
if num < len(meses):
  print(meses[num])
  else:
    print("nummero invalido:")
