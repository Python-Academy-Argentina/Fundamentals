# basics.py
# muestra la sintaxis básica y algunos ejemplos de expresiones lambda

# las expresiones lambda son pequeñas funciones anónimas (no tienen nombre) que pueden
# ser empleadas donde sea que se necesite de una función, aunque están restringidas
# semánticamente a una única expresión

saludo = lambda nombre: f'¡Hola, {nombre}!'

# en el ejemplo de arriba, guardamos la función en una variable, que NO es lo mismo
# que asignarle un nombre

hola_python = saludo('Python Academy')

print(f'\nEjecutamos la función guardada en <saludo>: {hola_python}')

print()


# la sintaxis es simple: lambda [variables]: [expresión sin 'return']

suma = lambda a, b: a + b

a, b = 5, 2

res = suma(a, b)

print(f'\nSumamos {a} y {b} con una expresión lambda: {res}')

print()

# el siguiente ejemplo devuelve una expresión lambda que sirve de incrementador
# (incrementa el argumento provisto por <n>)

def incrementador(n):
    """
    Devuelve una función que incrementa <x> según lo que valga <n>.
    """
    return lambda x: x + n


print('\nincrementador():')

i = incrementador(100)

a, b = 100, 200

print(f'\nIncrementamos {a}: {i(a)}')
print(f'\nIncrementamos {b}: {i(b)}')

print()
