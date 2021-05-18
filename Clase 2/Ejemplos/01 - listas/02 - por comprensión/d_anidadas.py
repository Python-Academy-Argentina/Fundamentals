# anidadas.py
# muestra ejemplos de listas por comprensión anidadas

# tenemos una lista con tres listas anidadas y queremos generar una nueva
# lista con los primeros, segundos y terceros valores de cada una respectivamente

lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print('\nReordenando listas anidadas:')
print(f'lista_de_listas: {lista_de_listas}')

nueva = [[lista[i] for lista in lista_de_listas] for i in range(3)]

print('\nNueva lista usando comprensiones anidadas:')
print(f'nueva: {nueva}')


# podemos obtener lo mismo, aunque con más líneas de código, usando
# dos bucles 'for' anidados

nueva = []

for i in range(3):

    temp = []

    for lista in lista_de_listas:

        temp.append(lista[i])

    nueva.append(temp)

print('\nNueva lista usando bucles "for" anidados:')
print(f'nueva: {nueva}')

print()


# tenemos una lista con tres listas anidadas con tickets de distintos tipos
# y queremos crear una nueva que sólo contenga incidentes

tickets = [['INC001', 'RITM0012', 'INC002'],
           ['INC0013', 'INC004', 'CHG0003'],
           ['INC005', 'INC006', 'CTASK004']]

print('\nFiltrando listas anidadas:')
print(f'tickets: {tickets}')

incidentes = [ticket for lista in tickets for ticket in lista if 'INC' in ticket]

print('\nUsando comprensiones anidadas y un "if":')
print(f'incidentes: {incidentes}')


# obtenemos lo mismo, con más líneas de código, usando dos bucles 'for'
# anidados y un 'if'

incidentes = []

for lista in tickets:

    for ticket in lista:

        if 'INC' in ticket:

            incidentes.append(ticket)

print('\nUsando bucles "for" anidados y un "if":')
print(f'incidentes: {incidentes}')

print()
