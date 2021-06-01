# alumnos.py
# programa que permite crear diccionarios representando alumnos, asignar notas,
# imprimir información de interés, y guardar en o leer desde un archivo de texto
# en formato json

import json


def crear_alumno():
    """
    Devuelve un diccionario con el nombre, apellido,
    nombre completo y notas (lista vacía).
    """
    nombre = input('Ingresá el primer nombre: ')
    apellido = input('Ingresá el apellido: ')
    alumno = {
        'nombre': nombre,
        'apellido': apellido,
        'notas': []
    }
    return alumno


def agregar_nota(alumno, nota):
    """
    Agrega <nota> a <alumno>.
    """
    alumno['notas'].append(nota)


def calcular_promedio(alumno):
    """
    Devuelve el promedio de un alumno.
    """
    notas = alumno['notas']
    cantidad = len(notas)

    try:
        promedio = sum(notas) / len(notas)
    except ZeroDivisionError:
        promedio = 0

    return promedio


def generar_detalles(alumno):
    """
    Imprime información de interés sobre un alumno.
    """
    id_ = alumno.get('id')
    nombre = alumno.get('nombre')
    apellido = alumno.get('apellido')
    nombre_completo = f'{apellido}, {nombre}'
    promedio = round(calcular_promedio(alumno), 1)

    return f'ID: {id_}; Alumno: {nombre_completo}; Promedio: {promedio}'


def guardar(alumnos, archivo):
    """
    Guarda la lista <alumnos> en <archivo> en formato json.
    """
    renglones = [json.dumps(alumno) + '\n' for alumno in alumnos]

    with open(archivo, 'w') as f:
        f.writelines(renglones)


def main(**kwargs):
    """
    Permite agregar alumnos, notas, e imprimir
    la lista de alumnos y sus promedios.
    """
    print('\nIngresá el número correspondiente a la opción deseada:\n')
    print('1. Ingresar nuevo alumno')
    print('2. Ingresar nota para un alumno')
    print('3. Imprimir la lista de alumnos')
    print('4. Guardar')
    print('0. Salir del programa')

    alumnos = kwargs.get('alumnos')
    archivo = kwargs.get('archivo')

    while True:
        opcion = int(input('\nOpción: '))

        if opcion == 1:
            alumno = crear_alumno()
            id_ = len(alumnos) + 1
            # agrego 'id' al diccionario
            alumno.update(id=id_)
            # agrego el diccionario a la lista
            alumnos.append(alumno)

        elif opcion == 2:
            id_ = int(input('Ingresá el ID del alumno: ')) - 1

            try:
                alumno = alumnos[id_]
            except IndexError:
                print('El ID ingresado no existe.')
            else:
                nota = int(input('Ingresá la nota: '))
                # agregamos la nota
                agregar_nota(alumno, nota)

        elif opcion == 3:
            for alumno in alumnos:
                detalles = generar_detalles(alumno)
                print(f'\n{detalles}')

        elif opcion == 4:
            try:
                guardar(alumnos, archivo)
            except OSError:
                print('No se pudo guardar la lista de alumnos.')

        elif opcion == 0:
            print()
            exit()

        else:
            print('Opción inválida.')


archivo = 'alumnos.txt'

try:
    alumnos = [json.loads(alumno) for alumno in open(archivo, 'r')]
except OSError:
    alumnos = []

try:
    main(alumnos=alumnos, archivo=archivo)
except KeyboardInterrupt:
    print('\n')
    exit()
