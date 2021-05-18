# filter_y_map.py
# demuestra los usos de las funciones built-in filter() y map()

# filter() sirve para filtrar (duh!) una colección
# acepta primero una función que provee la lógica del filtro, y luego la colección

lista = list(range(10))

print('\nTenemos una lista de enteros y queremos filtrar los impares.')

print(f'\nLa lista: {lista}')

# filter() devuelve un iterador, no una lista
# podemos convertir un iterador en una lista con el método list(iterador)

pares = filter(lambda x: x % 2 == 0, lista)

print(f'\nUsando filter() y lambda: {list(pares)}')

# podemos lograr el mismo resultado generando una lista por comprensión y un 'if'

pares_comp = [n for n in lista if n % 2 == 0]

print(f'\nGenerando una lista por comprensión: {pares_comp}')

print()


# map() resuelve una operación con los valores en una colección y devuelve
# un iterador que produce los resultados

print('\nAhora queremos una nueva lista con los cuadrados de la lista original.')

cuadrados = map(lambda x: x**2, lista)

print(f'\nUsando map() y lambda: {list(cuadrados)}')

# logramos el mismo resultado con una lista por comprensión

cuadrados_comp = [n**2 for n in lista]

print(f'\nGenerando una lista por comprensión: {cuadrados_comp}')

print()
