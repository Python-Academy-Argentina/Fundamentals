# algunos_metodos.py
# ejemplos de métodos propios de todas los objetos de clase list

lista = ['python', 'academy', 'python', 'fundamentals']

print(f'\nLista original: {lista}')


# list.count() cuenta los ítems en una lista

n_python = lista.count('python')
n_academy = lista.count('academy')

print('\nUsando list.count():')
print(f'"python" se encuentra {n_python} veces.')
print(f'"academy", sólo {n_academy} vez.')


# list.copy() genera una copia de la original

copia = lista.copy()

print('\nUsando list.copy():')
print(f'Esta es la lista original: {lista}')
print(f'Y esta es una copia exacta: {copia}')


# list.clear() borra los contenidos de una lista

copia.clear()

print('\nUsando list.clear():')
print(f'Borramos los contenidos de la copia: {copia}')


# list.remove() borra la PRIMERA instancia del valor encontrado

lista.remove('python')

print('\nUsando list.remove():')
print(f'Borrando la primera instancia de "python": {lista}')


# list.reverse() revierte los ítems de la lista

lista.reverse()

print('\nUsando list.reverse():')
print(f'La lista original quedó así: {lista}')


# list.sort() ordena los ítems de la lista

lista.sort()

print('\nUsando list.sort():')
print(f'Después de ordenarla: {lista}')


# list.append() agrega ítems al final de la lista

lista.append('python')

print('\nUsando list.append():')
print(f'Después de ingresar "python" de nuevo: {lista}')


# list.extend() extiende una lista con los contenidos de una colección

lista.extend(('esto', 'es', 'una', 'tupla'))

print('\nUsando list.extend():')
print(f'Después de extender la lista con una tupla: {lista}')

print()
