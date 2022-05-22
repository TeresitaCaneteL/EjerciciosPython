data = []
i = 0
while i < 3:

        name = input('Nombre: ')
        age = int(input('Edad: '))
        data.append({"name": name, "age": age})
    #except ValueError as e:
        #print('La edad no es valida')
        i+=1
maximum_age = int(input('Maxima edad: '))
names = sorted([person['name'] for person in data if person['age'] >= maximum_age])
for name in names:
    print(name)