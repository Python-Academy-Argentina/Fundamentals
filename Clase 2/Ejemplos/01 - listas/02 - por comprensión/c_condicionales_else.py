# condicionales_else.py
# muestra ejemplos de listas por comprensión con condicionales "if" y "else"

# generamos una lista de números aleatorios entre 0 y 50 y otra lista
# <par_o_impar> indicando con True o False si son pares o impares
# par: True; impar: False

from random import randint    # randint(a, b) devuelve un número entre <a> y <b>

rand_nums = [randint(0, 50) for n in range(10)]

print('\nEvaluamos una lista de números aleatorios de 0 a 50:')
print(f'rand_nums: {rand_nums}')

par_o_impar = []

for n in rand_nums:

    if n % 2:

        par_o_impar.append(False)

    else:

        par_o_impar.append(True)

print('\nUsando "if" y "else" en un bucle "for" convencional (par: True; impar: False):')
print(f'par_o_impar: {par_o_impar}')


# usamos 'if' y 'else' al comienzo de la comprensión

par_o_impar = [False if n % 2 else True for n in rand_nums]

print('\nUsando "if" y "else" al comienzo de la comprensión (par: True; impar: False):')
print(f'par_o_impar: {par_o_impar}')

print()
