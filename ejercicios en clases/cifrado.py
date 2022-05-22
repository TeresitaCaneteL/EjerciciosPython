
while True:
    texto=input("Tu texto: ")

    abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuwxyz"

    k=(input("Valor de desplazamiento: "))
    cifrad=""

    for c in texto:
        if c in abc:
            cifrad += abc[(abc.index(c)+3)%(len(abc))]
        else:
            cifrad+=c

    print("Texto cifrado: ",cifrad)
    break
