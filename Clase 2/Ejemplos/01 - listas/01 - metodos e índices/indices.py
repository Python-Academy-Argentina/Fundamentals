# indices.py
# muesta métodos que hacen uso de índices

lista = ['python', 'academy', 'fundamentals', 'listas', 'índices', 'segmentos']

print(f'\nLista original: {lista}')


# podemos usar range(len(coleccion)) para obtener un iterador de tantos índices
# como ítems contenga nuestra colección

print('\nUsando range():')

for indice in range(len(lista)):
    # el índice va entre [] pegados al objeto
    valor = lista[indice]
    print(f'"{valor}" se encuentra en el índice número {indice}')


# Python nos provee una función que genera índices automáticamente y nos devuelve
# dos valores: el índice y su respectivo valor

print('\nUsando enumerate(lista):')

for indice, valor in enumerate(lista):
    print(f'"{valor}" se encuentra en el índice número {indice}')


# list.index(valor) devuelve el número de índice de <valor>

print('\nUsando list.index():')

for item in lista:
    indice = lista.index(item)
    print(f'"{item}" se encuentra en el índice número {indice}')


# list.insert(indice, valor) inserta <valor> en la posición <indice>

lista.insert(0, 'todo a la derecha')
lista.insert(len(lista), 'esto va al final')

print('\nUsando list.insert():')
print(f'Después de insertar en los índices 0 y len(lista): {lista}')


# list.pop(indice) borra la posición <indice> y su contenido, devolviendo el valor
# si no pasamos un índice, borra el último índice (-1)

ultimo = lista.pop()
primero = lista.pop(0)

print('\nUsando list.pop():')
print(f'Después de remover los índices -1 y 0: {lista}')
print(f'ultimo: {ultimo}')
print(f'primero: {primero}')

print()
