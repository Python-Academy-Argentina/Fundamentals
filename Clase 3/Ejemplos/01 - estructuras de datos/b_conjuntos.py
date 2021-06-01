# b_conjuntos.py
# muestra ejemplos de operaciones con conjuntos (sets)

# los conjuntos son colecciones de objetos encerrados entre {},
# y tienen la particularidad de no aceptar valores duplicados

canasta = {'manzana', 'naranja', 'banana', 'uva', 'pera', 'manzana', 'uva', 'pera'}

print(f'\nAunque intente sumar duplicados, los conjuntos no los admiten: {canasta}')


# podemos crear conjuntos con el método set(), que acepta cualquier
# iterable y lo separa en cada una de sus partes

hechizo_1 = set('abracadabra')

hechizo_2 = set('alacazam')

print(f'\nLetras del primer hechizo: {hechizo_1}')
print(f'\nLetras del segundo hechizo: {hechizo_2}')


# los conjuntos son excelentes para realizar comparaciones

a, b = hechizo_1, hechizo_2

print(f'\n(a - b) devuelve los contenidos de <a> que no estan en <b>: {a - b}')
print(f'\n(a | b) devuelve los contenidos de <a> y de <b>: {a | b}')
print(f'\n(a & b) devuelve los contenidos en común entre <a> y <b>: {a & b}')
print(f'\n(a ^ b) devuelve los contenidos que no se repiten entre <a> y <b>: {a ^ b}')


# para crear un conjunto vacío, aunque sepamos que encierran a sus contenidos
# entre {}, debemos hacerlo a través set(), ya que Python entiende {} como
# un diccionario

print(f'\nset() crea un conjunto: {type(set())}')
print(f'\nPero {{}} crea un diccionario: {type({})}')


# admiten ser creados por comprensión

cuadrados = {x**2 for x in range(1, 6)}

print(f'\nConjunto de cuadrados: {cuadrados}')


# los conjuntos tienen varios métodos:

enteros = set(range(1, 8))    # {1, 2, 3, 4, 5, 6, 7}

pares = set(range(2, 6, 2))   # {2, 4}

print(f'\nEmpezamos con dos conjuntos: <enteros> = {enteros}, <pares> = {pares}')


pares.add(6)

print(f'\nset.add() agrega un valor: {pares}')


pares.remove(6)

print(f'\nset.remove() quita un valor: {pares}')


diff = enteros.difference(pares)

print(f'\nset.difference() devuelve diferencias (sin cambiarlos): {diff}')


enteros.difference_update(diff)

print(f'\nset.difference_update() actualiza el conjunto con la diferencia: {enteros}')


pares = set(range(2, 7, 2))

is_sub = pares.issubset(enteros)

print(f'\nset.issubset() devuelve si el argumento contiene al conjunto: {is_sub}')


is_super = pares.issuperset(enteros)

print(f'\nset.issuperset() devuelve si el conjunto contiene al argumento: {is_super}')


impares = set(range(1, 6, 2))    # {1, 3, 5}

union = impares.union(pares)

print(f'\nset.union() une dos conjuntos: {union}')


copia = union.copy()

print(f'\nset.copy() devuelve una copia: {copia}')


copia.update({7, 8, 9})

print(f'\nset.update() actualiza un conjunto: {copia}')


copia.clear()

print(f'\nset.clear() borra los contenidos: {copia}')

print()
