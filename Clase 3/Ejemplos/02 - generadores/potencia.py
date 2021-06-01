# potencia.py
# generador que devuelve una secuencia de potencias

def potencia(n, exp):
    '''
    Devuelve enteros elevados a la <exp> potencia
    hasta llegar a <n>.
    '''
    cont = 1
    while cont <= n:
        yield cont ** exp
        cont += 1


# creamos un generador de N números al cuadrado

cuadrados = potencia(10, 2)

print('\nImprimimos cuadrados hasta 10:\n')

for n in cuadrados:
    print(n)

print()


# creamos otro generador de N números al cubo

cubos = potencia(10, 3)

print('\nImprimimos cubos hasta 10:\n')

for n in cubos:
    print(n)

print()


# también podemos emplear alguna de las técnicas de bucles en
# la sección anterior

cuartas = potencia(5, 4)
quintas = potencia(5, 5)

print('\nUsamos zip() para iterar sobre dos generadores:\n')

cont = 0
for c, q in zip(cuartas, quintas):
    cont += 1
    print(f'{cont} a la cuarta es {c}, y a la quinta es {q}.')

print()
