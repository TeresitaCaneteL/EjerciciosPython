"""
def factorial():
  num=int(input("ingrese numero: "))
  if num > 1:
    num *= num * num -1
    print(num)
factorial()

"""
def factorial(num):
    if num < 0:
        print("Factorial negativo no existe")

    elif num == 0:
        return 1

    else:
        fact = 1
        while(num > 1):
            fact *= num
            num -= 1
        return fact

num = int(input("ingrese numero: "))

print("Factorial de",num,"es", factorial(num))
