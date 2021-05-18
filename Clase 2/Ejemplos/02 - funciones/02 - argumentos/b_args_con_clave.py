# b_args_con_clave.py
# muestra ejemplos de funciones con argumentos con clave (keyword arguments)

# en la función <operaciones> de a_args_posicionales.py vemos que se aceptan
# dos argumentos: <a> y <b>
# estos argumentos tienen nombre (clave), aunque aceptan ser tratados posicionales
# en la medida en la que no se los referencie por su nombre:

def operaciones(a, b):
    """
    Devuelve el resultado de resolver distintas operaciones
    aritméticas entre <a> y <b>.
    """
    print(f'\nEl orden no importa para las sumas:')
    print(f'{a} + {b} es {a + b} y {b} + {a} también es {b + a}')
    print(f'\nNi tampoco para las multiplicaciones:')
    print(f'{a} * {b} es {a * b} y {b} * {a} también es {b * a}')

    print('\nSin embargo, restas y divisiones ya no son tan simples...')
    print(f'{a} - {b} es {a - b}, pero {b} - {a} es {b - a}')
    print(f'{a} / {b} es {a / b}, pero {b} / {a} es {b / a}')


print('\nPasando a = 5 y b = 2 con sus respectivos nombres:')

operaciones(b=2, a=5)  # doy vuelta los valores, pero el resultado es el mismo


print('\nPasando a=7 y b=1 con sus respectivos nombres:')

operaciones(b=1, a=7)


# si quisiera prohibir el uso de claves para ciertos argumentos, Python nos permite
# delimitarlos pasando / como si fuera una variable:

print('\n\nAhora probamos pasar argumentos posicionales con clave:')

def suma_posicionales(a, b, /):  # después de / puedo seguir agregando argumentos con clave
    """
    Esta no admite hacer algo como 'suma_posicionales(a=1, b=0)'.
    """
    print(f'\n{a} + {b} es {a + b}')


print('\nPasando <a> y <b> sin clave:')

suma_posicionales(5, 2)  # esto no falla


print('\nPasando a=5 y b=2 con clave:')

suma_posicionales(a=5, b=2)  # esto resulta en TypeError

print()
