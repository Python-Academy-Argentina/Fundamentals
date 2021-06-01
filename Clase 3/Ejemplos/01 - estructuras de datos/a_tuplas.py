# a_tuplas.py
# muestra ejemplos de operaciones con tuplas

# las tuplas son colecciones de objetos delimitados por ,
# y se muestran entre ()

tupla_1 = 'python', 3, '¡Clase 3!'

print(f'\nNo uso paréntesis para definirla pero python igual los suma: {tupla_1}')

tupla_2 = tupla_1, tuple(range(1, 6))

print(f'\nPuedo tener tuplas anidadas: {tupla_2}')


# son inmutables, es decir, no puedo cambiarlas de ninguna manera

try:
    tupla_1[0] = 'ruby'
except TypeError:
    print('\nPython arrojó un TypeError. ¡No se las puede cambiar!')


# pero sí pueden contener objetos mutables, y a estos SÍ puedo modificarlos

tupla_3 = ['python', 'academy'], 'fundamentals'

print(f'\n<tupla_3> original: {tupla_3}')

tupla_3[0][0] = 'python3'

print(f'\n<tupla_3> después de modificar su lista: {tupla_3}')


# vimos que las funciones suelen operar con tuplas

# *args es una tupla, y tiene mucho sentido, ya que es importante mantener
# la integridad de las variables pasadas a nuestras funciones

def func1(*args):
    return args


# cualquier cosa que le pase a <func> es convertida a una tupla

print(f'\nImprimimos <args> de <func1>: {func1("esta es la", 3, "clase")}')


# y si una función devuelve más de un objeto, también lo hace en forma de tupla

def func2():
    return list(), dict(), 1, 2, 3

print(f'\nImprimimos lo que devuelve <func2>: {func2()}')


# tienen dos métodos que ya conocemos por haber estudiado listas:

contador = tupla_1.count('python')

indice = tupla_1.index('¡Clase 3!')

print(f'\n"python" aparece {contador} vez en <tupla_1> y {indice} es el índice de su tercer objeto.')


# admiten ser generadas por comprensión, pero sólo utilizando tuple()

print(f'\nTupla de cuadrados: {tuple(x**2 for x in range(1, 6))}')

print()
