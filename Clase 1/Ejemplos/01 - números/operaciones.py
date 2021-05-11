# operaciones.py
# pide dos números e imprime el resultado de diferentes
# operaciones entre ellos

num_1 = input('Primer número: ')

num_2 = input('Segundo número: ')

# convertimos los números (string) en integers
# para poder operar aritméticamente
a = int(num_1)
b = int(num_2)

suma = a + b
resta = a - b
multi = a * b
div = a / b

print(num_1 + ' + ' + num_2 + ' es igual a ' + str(suma))

print(num_1 + ' - ' + num_2 + ' es igual a ' + str(resta))

print(num_1 + ' * ' + num_2 + ' es igual a ' + str(multi))

print(num_1 + ' / ' + num_2 + ' es igual a ' + str(div))
