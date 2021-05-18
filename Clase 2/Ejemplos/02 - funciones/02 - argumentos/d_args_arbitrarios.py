# d_args_arbitrarios.py
# muestra ejemplos de funciones que aceptan cantidades arbitrarias de argumentos

# usamos '*args' (tupla) para agrupar todos los argumentos que no fueron
# explícitamente definidos en nuestra función

print('\nconcatenador():')

def concatenador(*args, sep='/'):
    """
    Devuelve una cadena con los valores en <args>
    separados por <sep>.
    """
    return sep.join(args)


py_bin = concatenador('', 'usr', 'bin', 'python')

print(f'\nUsamos la función sin cambiar <sep> para generar un string concatenado: {py_bin}')


opciones = concatenador('opc1', 'opc2', 'opc3', 'opc4', sep=' | ')

print(f'\nY pasamos sep=\' | \' para cambiar el separador: {opciones}')

print()


# usamos '**kwargs' (diccionario) para agrupar todos los argumentos con clave
# que no fueron explícitamente definidos en la función

def args_y_kwargs(*args, **kwargs):
    """
    Imprime los tipos y contenidos de <args> y <kwargs>.
    """
    args_type = type(args).__name__
    kwargs_type = type(kwargs).__name__
    print(f'<args> es un objeto de clase {args_type} y contiene: {args}')
    print(f'<kwargs> es un objeto de tipo {kwargs_type} y contiene: {kwargs}')


print('\nargs_y_kwargs():\n')

args_y_kwargs(1, 2, 3, nombre='Python Academy', curso='Fundamentals')

print()
