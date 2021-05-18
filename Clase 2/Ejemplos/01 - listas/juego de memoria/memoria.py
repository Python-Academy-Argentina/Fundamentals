# memoria.py
# pide valores hasta que se ingrese 999, después pregunta por el orden original

# importamos shuffle para mezclar los valores ingresados
from random import shuffle


print('\nJuego de la memoria.')
print('\nConsigna: Ingresá tantos valores como quieras e ingresá 999')
print('          para empezar a jugar y poner a prueba tu memoria.')

valores = []

while True:
    valor = input('\nIngresá un valor: ')

    if not valor:
        print('El valor no puede ser nulo. Intentá de nuevo.')
        continue

    if valor in valores:
        print('No podés ingresar valores repetidos.')
        continue

    if valor == '999':
        break

    valores.append(valor)  # los valores aceptados se insertan en <valores>
    
# hacemos una copia de la lista original y mezclamos su contenidos
copia = valores[:]
shuffle(copia)

intentos = 3

for valor in copia:

    posicion = valores.index(valor) + 1

    while intentos > 0:
        respuesta = int(input(f'\n¿En qué posición ingresaste el valor [ {valor} ]? '))

        if respuesta != posicion:
            print('Respuesta incorrecta.')
            intentos -= 1
            continue

        print('¡Correcto!')
        break

    else:
        print('\nPerdiste. Más suerte la próxima.\n')
        exit()

print('\n¡Ganaste!\n')
