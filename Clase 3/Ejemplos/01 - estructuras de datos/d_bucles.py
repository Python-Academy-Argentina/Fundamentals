# d_bucles.py
# muestra ejemplos de técnicas de bucle con estructuras de datos

def unir_claves_y_valores(diccionario):
    '''
    Imprime las claves y valores en <diccionario>
    separados por un espacio.

    dict.items() devuelve pares de claves/valores
    en un diccionario.
    '''
    cont = 0
    for clave, valor in diccionario.items():
        cont += 1
        print(f'{cont}. {clave} {valor}')


def unir_dos_listas(objs, props):
    '''
    Imprime oraciones con dos listas representando
    objetos y propósitos.

    zip() devuelve los valores en las colecciones
    pasadas como argumentos, para poder acceder a
    cada uno de ellos en el mismo orden.
    '''
    cont = 0
    for obj, prop in zip(objs, props):
        cont += 1
        print(f'{cont}. Se necesita(n) {obj} para {prop}.')


def ordenar_unicos(secuencia):
    '''
    Imprime los valores en <secuencia> de manera
    ordenada y sólo una vez por valor.

    sorted() devuelve una lista ordenada de la
    colección pasada como argumento.
    '''
    unicos = set(secuencia)
    for indice, valor in enumerate(sorted(unicos)):
        print(f'{indice + 1}. {valor}')


def invertir(secuencia):
    '''
    Imprime los valores invertidos en <secuencia>.

    reversed() devuelve una lista invertida de los
    valores en la secuencia pasada como argumento.
    '''
    invertidos = reversed(secuencia)
    for indice, valor in enumerate(invertidos):
        print(f'{indice + 1}. {valor}')


# generamos un diccionario con nombres y apellidos de personajes
# desempeñados por Keanu Reeves y los unimos

personajes = {'John': 'Wick', 'Thomas': 'Anderson', 'Kevin': 'Lomax'}

print('\nUnimos claves y valores con dict.items():\n')

unir_claves_y_valores(personajes)

print()


# iteramos sobre dos listas de objetos y sus propósitos y los
# imprimimos en la misma oración

objetos = ['un anillo', 'siete esferas', 'una masterball']

propositos = ['gobernarlos a todos', 'revivir a Goku', 'atrapar a Mewtwo']

print('\nImprimimos los valores en dos listas separadas en la misma oración:\n')

unir_dos_listas(objetos, propositos)

print()


# ordenamos una colección, removiendo valores duplicados

canasta = ['uva', 'banana', 'kiwi', 'naranja',
           'uva', 'banana', 'kiwi', 'naranja']


print('\nImprimimos valores únicos y ordenados:\n')

ordenar_unicos(canasta)

print()


# ordenamos una colección, removiendo valores duplicados

impares = range(1, 10, 2)

print('\nImprimimos valores invertidos:\n')

invertir(impares)

print()
