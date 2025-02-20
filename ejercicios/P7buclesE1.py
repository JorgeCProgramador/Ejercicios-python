nuemro_nota = int(input("Cuantas notas desea ingresar: "))
suma = 0
for i in range(nuemro_nota):
    nota = float(input(f'Cual es la nota {i+1} ' ))
    suma = nota + suma
media = suma/nuemro_nota
print(f'La nota media del alumno es {media}')