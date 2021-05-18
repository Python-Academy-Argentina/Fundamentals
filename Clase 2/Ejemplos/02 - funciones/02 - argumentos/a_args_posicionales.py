# a_args_posicionales.py
# muestra ejemplos de funciones con argumentos posicionales

# se llaman argumentos posicionales porque se respeta el orden en el que
# los argumentos son pasados a la función

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


print('\nPasando a = 5 y b = 2:')

operaciones(5, 2)  # esto no falla


print('\nPasando a = 7 y b = 0:')

operaciones(7, 0)  # esto resulta en ZeroDivisionError
