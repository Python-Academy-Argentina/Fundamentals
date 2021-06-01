# alumnos.py
# programa que permite crear diccionarios representando alumnos, asignar notas,
# imprimir información de interés, y guardar en o leer desde un archivo de texto
# en formato JSON

import json


class Alumno:
    '''
    Una simple clase que representa a un alumno.
    '''

    def __init__(self, nombre, apellido, notas=None, id_=None):

        self.id = id_
        self.nombre = nombre
        self.apellido = apellido
        self.__notas = notas or []

    def __repr__(self):
        return f'<ID: {self.id} - Apellido: {self.apellido}>'

    def __str__(self):
        promedio = round(self.promedio(), 1)

        return f'ID: {self.id}; Alumno: {self.nombre_completo}; Promedio: {promedio}'
    
    @property
    def nombre_completo(self):
        '''
        Devuelve el nombre completo en formato <apellido, nombre>.
        '''
        return f'{self.apellido}, {self.nombre}'

    @property
    def notas(self):
        '''
        Devuelve la lista de notas.
        '''
        return self.__notas

    def agregar_nota(self, nota):
        '''
        Agrega una nota a self.__notas.
        '''
        self.__notas.append(nota)

    def borrar_nota(self, indice):
        '''
        Borra una nota de self.__notas.
        '''
        del self.__notas[indice]

    def promedio(self):
        '''
        Devuelve el promedio de self.__notas.
        '''
        try:
            promedio = sum(self.__notas) / len(self.__notas)
        except ZeroDivisionError:
            promedio = 0

        return promedio

    def a_json(self):
        '''
        Devuelve un JSON-string con los datos del alumno.
        '''
        datos = {
            'id_': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'notas': self.__notas
        }
        return json.dumps(datos)

    @classmethod
    def desde_json(cls, json_str):
        '''
        Devuelve un objeto Alumno a partir de un JSON-string.
        '''
        return cls(**json.loads(json_str))


def crear_alumno():
    """
    Devuelve un objeto de tipo Alumno.
    """
    nombre = input('Ingresá el primer nombre: ')
    apellido = input('Ingresá el apellido: ')

    return Alumno(nombre, apellido)


def buscar_alumno(id_):
    """
    Devuelve un alumno de la lista.
    """
    return next((a for a in alumnos if a.id == id_), None)


def guardar(alumnos, archivo):
    """
    Guarda la lista <alumnos> en <archivo> en formato JSON.
    """
    renglones = [alumno.a_json() + '\n' for alumno in alumnos]

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
    print('3. Borrar una nota de un alumno')
    print('4. Imprimir la lista de alumnos')
    print('5. Guardar')
    print('0. Salir del programa')

    alumnos = kwargs.get('alumnos')
    archivo = kwargs.get('archivo')

    while True:
        opcion = int(input('\nOpción: '))

        # nuevo alumno
        if opcion == 1:
            alumno = crear_alumno()
            id_ = len(alumnos) + 1
            # agrego el ID del alumno
            alumno.id = id_
            # agrego el objeto a la lista
            alumnos.append(alumno)
        
        # ingresar nota
        elif opcion == 2:
            id_ = int(input('Ingresá el ID del alumno: '))

            alumno = buscar_alumno(id_)
            
            if not alumno:
                print('El ID ingresado no existe.')
            else:
                nota = int(input('Ingresá la nota: '))
                # agregamos la nota
                alumno.agregar_nota(nota)

        # borrar nota
        elif opcion == 3:
            id_ = int(input('Ingresá el ID del alumno: '))

            alumno = buscar_alumno(id_)
            
            if not alumno:
                print('El ID ingresado no existe.')
                continue

            if len(alumno.notas) == 0:
                print('\nNo hay notas para mostrar.')
                continue

            print()
            for indice, nota in enumerate(alumno.notas):
                print(f'{indice + 1}. {nota}')

            i = int(input('\n¿Qué nota querés borrar?: '))

            try:
                alumno.borrar_nota(i - 1)
            except IndexError:
                print('\nLa opción ingresada es inválida.')

        # imprimir alumnos
        elif opcion == 4:
            for alumno in alumnos:
                print(f'\n{alumno}')

        # guardar alumnos
        elif opcion == 5:
            try:
                guardar(alumnos, archivo)
            except OSError:
                print('No se pudo guardar la lista de alumnos.')

        # salir
        elif opcion == 0:
            print()
            exit()

        else:
            print('Opción inválida.')


archivo = 'alumnos.txt'

try:
    alumnos = [Alumno.desde_json(a) for a in open(archivo, 'r')]
except OSError:
    alumnos = []

try:
    main(alumnos=alumnos, archivo=archivo)
except KeyboardInterrupt:
    print('\n')
    exit()
