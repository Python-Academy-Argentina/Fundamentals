# c_args_predeterminandos.py
# muestra ejemplos de funciones con argumentos predeterminados

# podemos definir valores predeterminados para nuestros argumentos con el fin de
# extender la funcionalidad de nuestras funciones sin necesidad de pasar todas las
# variables necesarias para su ejecución

print('\ngenerar_saludo():')

def generar_saludo(nombre, imprimir=False):
    """
    Devuelve un saludo personalizado.
    Si <imprimir> == True, lo imprime en pantalla.
    """
    saludo = f'¡Hola, {nombre}!'

    if imprimir:  # como <imprimir> es False
        print(saludo)  # esto no se ejecuta, a menos que pase True

    return saludo


print('\nNo paso <imprimir>, entonces no imprime nada.')
generar_saludo('Python Academy')

print('\nAhora paso imprimir=True, y el saludo se imprime:')
generar_saludo('Python Academy', imprimir=True)

print()


# la siguiente función imprime una cadena n=3 veces, pero me da la posibilidad
# de cambiar n por otro número

print('\nrepetir():')

def repetir(msj, n=3):
    """
    Imprime <msj> <n> veces.
    """
    for _ in range(n):
        print(msj)


print('\nNo paso <n>, entonces <msj> se imprime 3 veces (default):')
repetir('Esto se imprime 3 veces.')

n = 5  # pueden cambiar esto al entero que quieran

print(f'\nPaso n={n}, por lo que <msj> se imprime {n} veces:')
repetir(f'Esto se imprime {n} veces.', n=n)

print()
