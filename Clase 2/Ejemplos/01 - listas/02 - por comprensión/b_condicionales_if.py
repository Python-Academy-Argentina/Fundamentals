# condicionales_if.py
# muestra ejemplos de listas de comprensión con condiciones "if"

# tenemos una lista de tickets de distintos tipos y queremos
# una nueva lista filtrada con sólo incidentes

tickets = ['INC001', 'INC002', 'CTASK001', 'RITM001', 'CHG001', 'INC003']

print('\nFiltramos una lista de tickets:')
print(f'tickets: {tickets}')

incidentes = []

for ticket in tickets:

    if ticket[0:3] == 'INC':    # equivalente a ticket.startswith('INC')

        incidentes.append(ticket)

print('\nUsando "if" en un bucle "for" convencional:')
print(f'incidentes: {incidentes}')


# podemos sumar un 'if' al final de nuestra lista por comprensión
# para filtrar la lista original

incidentes = [ticket for ticket in tickets if ticket[0:3] == 'INC']

print('\nUsando "if" al final de la comprensión:')
print(f'incidentes: {incidentes}')

print()


# generamos una lista con múltiplos de 6 entre el 1 y el 100

print('\nGeneramos una lista con múltiplos de 6:')

mult_de_seis = []

for n in range(1, 100):

    if n % 2 == 0:

        if n % 3 == 0:

            mult_de_seis.append(n)

print('\nUsando dos "if" en un bucle "for" convencional:')
print(f'mult_de_seis: {mult_de_seis}')


# podemos sumar tantos condiciones al final de la comprensión
# como sean necesarios

# usamos 'not' para negar el resultado de la operación
# cuando <n> es múltiplo, la operación da 0, y 'not 0' resulta en True

mult_de_seis = [n for n in range(1, 100) if not n % 2 if not n % 3]

print('\nUsando dos "if" al final de la comprensión:')
print(f'mult_de_seis: {mult_de_seis}')

print()
