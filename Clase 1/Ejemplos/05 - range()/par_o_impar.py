# par_o_impar.py
# imprime si los números del 0 al ingresado son pares o impares

num = int(input('Ingresá un número: '))
print()

for n in range(num + 1):    # sumo 1 para incluir al número ingresado

    if n % 2:    # si el resto != 0

        print(f'{n} es impar.')

    else:    # si el resto == 0

        print(f'{n} es par')
