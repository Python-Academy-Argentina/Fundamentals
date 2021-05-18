# segmentos.py
# muesta ejemplos de uso de segmentos

lista = ['python', 'academy', 'fundamentals', 'listas', 'índices', 'segmentos']

print(f'\nLa lista original es: {lista}')

print('\nLos segmentos se definen como lista[inicio:final], con índices separados por : dentro de [].')


# al igual que con la función range(), el último índice no se cuenta

print('\nSin salto:')
print(f'lista[0:3] devuelve una lista con los índices 0, 1 y 2: {lista[0:3]}')
print(f'lista[4:6] devuelve una lista con los índices 4 y 5: {lista[4:6]}')


# el tercer argumento es el salto

print('\nCon salto:')
print(f'lista[::2] devuelve una lista arrancando en 0 y saltando de a dos: {lista[::2]}')
print(f'lista[1::2] hace lo mismo, pero arrancando desde el índice 1: {lista[1::2]}')


# el salto puede ser negativo, para ir de atrás para adelante, revirtiendo el orden original

print('\nCon salto negativo:')
print(f'lista[2::-1] empieza en el índice 2 y va hasta el principio: {lista[2::-1]}')
print(f'lista[::-2] empieza desde el final, saltando de a dos: {lista[::-2]}')

# podemos usar lista[::-1] para obtener una lista revertida, igual que con list.reverse()
print(f'lista[::-1] hace lo mismo que list.reverse(): {lista[::-1]}')


# los índices y los segmentos también pueden ser usados con cadenas y tuplas

cadena = 'Fundamentals'

print('\nEjemplos con cadenas:')
print(f'Cadena original: {cadena}')
print(f'cadena[:5] resulta en: {cadena[:5]}')
print(f'cadena[::-1] la revierte: {cadena[::-1]}')


# omitir todos los índices devuelve una copia exacta del objeto

print('\nOmitiendo índices para conseguir copias exactas:')
print(f'lista[:] o lista[::] resulta en: {lista[::]}')
print(f'cadena[:] o cadena[::] resulta en: {cadena[::]}')

print()
