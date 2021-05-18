# operaciones.py
# demuestra la sintaxis básica de las funciones

print('\nEsta es una función muy simple:')

# las funciones se definen con la sentencia 'def', seguida por un nombre
# (sujeto a las mismas reglas y restricciones que las variables convencionales),
# un par de () y :

def saludo():
    """
    Esto es un doc string.
    Sirve para describir la función y es el texto
    que se muestra cuando se ejecuta help(función).
    """
    print('¡Hola!')


# para ejecutar la función, sólo tengo que llamarla por su nombre y sumar ()

saludo()

# entre los () definimos las variables con las que la función va a ejecutar
# alguna operación

print('\nEsta otra incluye un argumento:')

# para extender la funcinalidad de <saludo>, vamos a sumarle la capacidad de
# recibir un nombre y sumarlo al saludo:

def saludo_con_nombre(nombre):
    """
    Imprime un saludo para el nombre provisto.
    """
    print(f'¡Hola, {nombre}!')


# para pasarle <nombre> a nuestra función, lo pasamos entre ():

saludo_con_nombre('Python Academy')


# las funciones también pueden devolver uno o más valores de cualquier tipo,
# utilizando la sentencia 'return' seguida de lo que se quiere devolver:

print('\nY esta otra devuelve un valor que puedo guardar en una variable:')

def suma(a, b):
    """
    Devuelve la suma de <a> y <b>.
    """
    return a + b

a, b = 3, 4
resultado = suma(a, b)
print(f'Resultado de sumar {a} y {b}: {resultado}')

print()
