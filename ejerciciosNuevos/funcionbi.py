"""3.- Crear un programa en python con una función que
reciba un número decimal y lo convierta en binario y otra
funcion que reciba un número binario y lo convierta en decimal."""

"""numero_decimal = 50
numero_binario = 0
multiplicador = 1
while numero_decimal != 0: # paso 3
    # pasos 1, 4 y 5 se multiplica el módulo por su multiplicador
    numero_binario = numero_binario + numero_decimal % 2 * multiplicador
    numero_decimal //= 2 # paso 1
    multiplicador *= 10 # paso 5

print(numero_binario)"""

"""numero = int('11101', 2) #donde el 2 indica la base en la que se encuentra el número a convertir
print(numero)"""

def binario_a_decimal(numero_binario):
	numero_decimal = 0
	for posicion, digito_string in enumerate(numero_binario[::-1]):
		numero_decimal += int(digito_string) * 2 ** posicion

	return numero_decimal
num=input("ingrese numero: ")
print(binario_a_decimal(num))
