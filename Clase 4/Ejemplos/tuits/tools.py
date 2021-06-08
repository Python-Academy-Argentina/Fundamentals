import os
from datetime import datetime


def borrar_pantalla():
    '''
    Borra los contenidos de la consola.
    '''
    # para windows
    if os.name == 'nt':
        _ = os.system('cls')
    # para mac y linux (os.name es 'posix')
    else:
        _ = os.system('clear')


def convertir_fecha(fecha):
    '''
    Convierte la fecha de un tuit a un formato más legible.
    '''
    obj = datetime.strptime(fecha, '%Y-%m-%dT%H:%M:%S.%f%z')
    fmt = '%d/%b/%Y %H:%M'
    return obj.strftime(fmt)
