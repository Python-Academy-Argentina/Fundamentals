# sintaxis.py
# muestra la sintaxis básica de las listas por comprensión

bases = list(range(10))    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print('\nCalculando cuadrados:')
print(f'bases: {bases}')

# usamos un bucle 'for' para calcular los cuadrados de los números en <bases>

cuadrados = []

for b in bases:
    
    cuadrados.append(b**2)    # calcula el cuadrado de <b> y lo mete en <cuadrados>

print('\nUsando un bucle "for" convencional:')
print(f'cuadrados: {cuadrados}')


# podemos obtener el mismo resultado calculando los valores
# de <cuadrados> por comprensión

cuadrados = [b**2 for b in bases]

print('\nGenerando una lista por comprensión:')
print(f'cuadrados: {cuadrados}')

print()

# si quisiera una matriz que se viera así: [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# podría usar bucles 'for' anidados

print('\nGenerando matrices con "for" anidados:')
matriz = []

for n in range(3):

    temp = []

    for x in range(4):

        temp.append(0)

    matriz.append(temp)

print('\nUsando bucles "for" anidados:')
print(f'matriz: {matriz}')


# puedo lograr lo mismo en una sóla línea sumando otro par de []
# a mi lista por comprensión

matriz = [[0 for n in range(4)] for x in range(3)]

print('\nGenerando listas por comprensión anidadas:')
print(f'matriz: {matriz}')

print()
