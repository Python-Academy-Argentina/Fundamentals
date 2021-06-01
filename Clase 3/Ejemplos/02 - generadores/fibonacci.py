# fibonacci.py
# generador que devuelve valores de la secuencia Fibonacci

def fibonacci(n):
    '''
    Devuelve números de la secuencia Fibonnaci
    menores que <n>.
    '''
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a+b


# creamos un generador

fib1 = fibonacci(50)


# imprimimos los valores en <fib> uno por uno

print('\nImprimimos la serie en <fib1> con un bucle convencional:\n')

for n in fib1:
    print(n, end=' ')

print('\n')


# los generadores son objetos que recuerdan su estado, de manera que
# podemos acceder al próximo valor en la serie con el método next()

# cuando el generador se queda sin valores, next() arroja una excepción
# de tipo StopIteration

fib2 = fibonacci(10)

print('\nImprimimos la serie usando next():\n')

while True:
    try:
        print(next(fib2))
    except StopIteration:
        print('\nYa no hay más valores para devolver.')
        break

print()


# también podemos crear colecciones por comprensión utilizando generadores

lista = [n for n in fibonacci(100)]

print('\nImprimimos una lista por comprensión:\n')

print(f'Fibonacci por comprensión: {lista}')

print()
