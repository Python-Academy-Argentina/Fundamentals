# numeros_primos.py
# imprime si un número es primo o los factores que lo conforman

# sacado de la documentación oficial de Python

num = int(input('Ingresá un número mayor que 2 y menor que 50: '))

if num > 50:
    print('Cambiado a 50.')
    num = 50

elif num < 2:
    print('Cambiado a 2.')
    num = 2

else:
    pass    # pass no hace nada (equivalente a no usar el else)

for n in range(2, num + 1):

    for x in range(2, n):

        if n % x == 0:

            print(f'{n} es igual a {x} * {n//x}')

            break

    else:    # si no se llama a break, se entra al else
        
        print(f'{n} es un número primo')
