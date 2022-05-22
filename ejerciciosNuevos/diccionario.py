"""1.- crear un programa que guarde en una variable el
diccionario {'Euro':'EUR', 'Dollar':'USD', 'Peso Chileno':'CLP'},
 pregunte al usuario por una moneda y muestre su símbolo o un
 mensaje de aviso si la moneda no está en el diccionario."""

dic={'Euro':'EUR', 'Dollar':'USD', 'Peso Chileno':'CLP'}
moneda = input('ingrese moneda: ')
for mone in dic:
  if mone == moneda:
    print("Su simbolo es: ",dic[mone])
    break
  else:
    print("no Existe")
    break
"""
monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")
if moneda.title() in monedas:
    print(monedas[moneda.title()])
else:
    print("La divisa no está.")
"""