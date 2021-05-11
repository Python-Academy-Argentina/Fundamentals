# adivinanza.py
# pide un número hasta que se adivine

num = 43

opcion = int(input('\nIngresá un número: '))

while True:

    if opcion == num:

        print('\n¡Ganaste!\n')

        break    # el bucle se frena

    print('\nNúmero incorrecto.')

    opcion = int(input('\nIntentá de nuevo: '))
