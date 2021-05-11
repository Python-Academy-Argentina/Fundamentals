# mi_edad.py
# mismo ejemplo que '01 - números/mi_edad.py', esta vez
# formando cadenas más fáciles de leer

# convertimos al número (string) en un integer
# para poder operar aritméticamente
edad = int(input('Ingresá tu edad: '))

dias = edad * 365

horas = dias * 24

minutos = horas * 60

segundos = minutos * 60

print('Tu edad es ' + str(edad) + ' años.')

print('\nUsando "f":')
print(f'Viviste, por lo menos, {dias} días, {horas} horas, {minutos} minutos, y {segundos} segundos.')

# también podría haberlo escrito así:
print('\nUsando "format()":')
print('Viviste, por lo menos, {} días, {} horas, {} minutos, y {} segundos.'.format(dias, horas, minutos, segundos))
