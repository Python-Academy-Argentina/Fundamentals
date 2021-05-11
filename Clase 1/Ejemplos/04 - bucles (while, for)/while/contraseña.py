# contraseña.py
# pide una contraseña hasta que cumpla con las condiciones

comunes = {
    'Pass1234',
    'mipass123',
    'passw0rd',
    'contras3ña',
}

pwd = input('\nIngresá una contraseña: ')

ok = False

while not ok:    # mientras <ok> no devuelva True

    if len(pwd) < 8:    # si la longitud de la contraseña es menor que 8

        print('La contraseña debe contener al menos 8 caracteres.')

        pwd = input('\nIntentá de nuevo: ')

    elif pwd in comunes:    # si la contraseña está en el conjunto <comunes>

        print('La contraseña es demasiado común.')

        pwd = input('\nIntentá de nuevo: ')

    elif pwd.isnumeric():    # si la contraseña solo tiene números

        print('La contraseña no puede contener sólo números.')

        pwd = input('\nIntentá de nuevo: ')

    elif pwd.islower():    # si la contraseña sólo tiene letras minúsculas

        print('La contraseña debe contener al menos una letra mayúscula.')

        pwd = input('\nIntentá de nuevo: ')

    else:

        print(f'Contraseña aceptada: {pwd}')
        
        ok = True

print()
