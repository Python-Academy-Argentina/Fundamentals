# b_agenda_telefonica.py
# programa que permite guardar y leer números a y desde un archivo de texto

import os

def guardar_numero(nombre, numero, archivo):
    '''
    Abre agenda.txt y guarda <registro> al final.

    Devuelve True si el archivo se escribió correctamente,
    y False en caso contrario.
    '''
    with open(archivo, 'a') as f:
        f.write(f'{nombre}:{numero}\n')


def buscar_numero(nombre, archivo):
    '''
    Devuelve un número si <nombre> está en la agenda
    y None en caso contrario.
    '''
    numero = None
    for registro in open(archivo, 'r'):
        v = registro.strip().split(':')
        if v[0].lower() == nombre.lower():
            numero = v[1]
    
    return numero


def main(archivo):
    '''
    Provee un menú con opciones para operar
    sobre la agenda.
    '''
    print('\nIngrese el número de la opción deseada:\n')
    print('1. Leer agenda entera')
    print('2. Buscar número')
    print('3. Guardar número')
    print('4. Salir')

    while True:
        try:
            opcion = int(input('\nOpción: '))
            
            # leer agenda
            if opcion == 1:
                for registro in open(archivo, 'r'):
                    v = registro.strip().split(':')
                    print(f'\n{v[0]}: {v[1]}')

            # buscar contacto
            if opcion == 2:
                nombre = input('\nIngresá el nombre del contacto: ')
                numero = buscar_numero(nombre, archivo)

                if numero:
                    print(f'El número es: {numero}')
                else:
                    print('No se encontró un contacto con ese nombre.')
            
            # guardar contacto
            if opcion == 3:
                nombre = input('\nIngresá el nombre del contacto: ')
                numero = input('Ingresá el número: ')
                
                guardar_numero(nombre, numero, archivo)

                print('\nEl nuevo contacto se guardó correctamente.')
            
            if opcion == 4:
                print()
                exit()
                
        # OSError es padre de todas las excepciones que podría arrojar mi archivo
        except OSError:
            print(f'\nNo se pudo abrir el archivo: {archivo}\n')
            exit()


archivo = 'agenda.txt'

try:
    # creo el archivo si no existe
    if not os.path.exists(archivo):
        with open(archivo, 'w') as f:
            pass
except OSError:
    print(f'\nNo se pudo crear el archivo: {archivo}\n')

main(archivo)
