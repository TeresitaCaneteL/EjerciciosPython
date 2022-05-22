"""crear un programa que almacene las asignaturas de un curso
(minimo 5) en una lista, pregunte al usuario la nota que ha sacado
en cada asignatura y elimine de la lista las asignaturas aprobadas
(nota aprobacion 4). Al final el programa debe mostrar por pantalla
las asignaturas que el usuario tiene que repetir."""

data = []
i = 0
while i < 5:
    try:
        asig = input('Asignatura: ')
        nota = float(input('nota: '))
        data.append({"asig": asig, "nota": nota})
    except ValueError as e:
        print('ingrese nota')
    i+=1
maximum_nota = 4.0
notas =[asignatura['asig']
for asignatura in data
if asignatura['nota'] <= maximum_nota]
print("Debe repetir: ")
#print(notas)
for nota in notas:
  print(nota)
"""
subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
passed = []
for subject in subjects:
    score = float(input("¿Qué nota has sacado en " + subject + "?"))
    if score >= 5:
        passed.append(subject)
for subject in passed:
    subjects.remove(subject)
print("Tienes que repetir " + str(subjects))
"""
"""
sol2
subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for i in range(len(subjects)-1, -1, -1):
    score = float(input("¿Qué nota has sacado en " + subjects[i] + "?"))
    if score >= 5:
        subjects.pop(i)
print("Tienes que repetir " + str(subjects))
"""
