# par_o_impar.py
# imprime si los números del 0 al 9 son pares o impares

enteros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for n in enteros:    # por cada <n> en <enteros>

    if n % 2:    # si el resto != 0

        print(f'{n} es impar.')

    else:    # si el resto == 0

        print(f'{n} es par')
