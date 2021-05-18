# memoria.py
# pide valores tantas veces como se indique al comienzo, después pregunta por el orden original

# importamos shuffle para mezclar los valores ingresados y os para borrar la pantalla
from random import random
import os


def borrar_pantalla():
    """
    Borra los contenidos de la consola.
    """
    # para windows
    if os.name == 'nt':
        _ = os.system('cls')
    # para mac y linux (os.name es 'posix')
    else:
        _ = os.system('clear')


def pedir_valores(cantidad):
    """
    Devuelve una lista de n valores (n = <cantidad>).
    """
    valores = []

    while cantidad > 0:
        valor = input('\nIngresá un valor: ')

        if not valor:
            print('El valor no puede ser nulo. Intentá de nuevo.')
            continue

        if valor in valores:
            print('No podés ingresar valores repetidos.')
            continue

        valores.append(valor)
        cantidad -= 1

    return valores


def adivinar(valores, intentos):
    """
    Crea una copia de valores y mezcla sus contenidos.
    Pregunta por el orden original de la nueva lista y
    se pierde cuando <intentos> == 0.
    """
    copia = valores[:]
    copia.sort(key=lambda x: random())

    for valor in copia:
        posicion = valores.index(valor) + 1

        while intentos > 0:
            respuesta = pedir_entero(f'\n¿En qué posición ingresaste el valor [ {valor} ]? ')

            if respuesta != posicion:
                print('Respuesta incorrecta.')
                intentos -= 1
                continue

            print('¡Correcto!')
            break

        else:
            print('\nPerdiste. Más suerte la próxima.')
            return
    
    print('\n¡Ganaste!')


def pedir_entero(msj):
    """
    Ejecuta input(msj) hasta que se ingrese un entero.
    """
    while True:
        try:
            entero = int(input(msj))
        except ValueError:
            print('El valor ingresado no es válido.')
        else:
            return entero


def jugar_de_nuevo():
    """
    Pregunta si se quiere jugar de nuevo y ejecuta main()
    si la respuesta es 'y' o termina el programa si 'n'.
    """
    while True:
        try:
            respuesta = input('\n¿Querés jugar de nuevo? (y/n) ')
            assert respuesta.lower() in {'y', 'n'}
        except AssertionError:
            print('Respuesta inválida. Por favor ingresá "y" o "n".')
        else:
            if respuesta.lower() == 'y':
                borrar_pantalla()
                main()
            else:
                print()
                exit()


def main():
    try:
        # pedimos el total de valores a ingresar
        cantidad = pedir_entero('\n¿Cuántos valores querés ingresar? ')

        # pedimos el número de intentos para adivinar
        intentos = pedir_entero('\n¿Cuántos intentos querés? ')

        # ejecutamos pedir_valores() y guardamos la lista
        lista = pedir_valores(cantidad)

        # borramos la pantalla
        borrar_pantalla()

        # ejecutamos adivinar() y pasamos la lista y el nº de intentos
        adivinar(lista, intentos)

        # preguntamos si se quiere jugar de nuevo
        jugar_de_nuevo()

    # si el usuario ejecuta Ctrl + C
    except KeyboardInterrupt:
        print('\n\nGracias por jugar.\n')
        exit()


# bienvenida
print('\nJuego de la memoria.')
print('\nConsigna: Ingresá tantos valores como quieras y poné a prueba tu memoria.')

main()
