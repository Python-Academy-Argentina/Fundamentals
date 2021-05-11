# mi_edad.py
# calcula tu edad en días, horas, minutos y segundos

# convertimos a <edad> (string) en un integer
# para poder operar aritméticamente
edad = int(input('Ingresá tu edad: '))

dias = edad * 365

horas = dias * 24

minutos = horas * 60

segundos = minutos * 60

print('\nTu edad es ' + str(edad) + ' años.')

# usamos 'end' para quedarnos en el mismo renglón
print('Viviste, por lo menos, ', end='')

print(str(dias) + ' días, ', end='')

print(str(horas) + ' horas, ', end='')

print(str(minutos) + ' minutos, ', end='')

print('y ' + str(segundos) + ' segundos.')
