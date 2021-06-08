# app.py
# programa para interactuar con la PAF CRUD API

import config as c
from tools import borrar_pantalla, convertir_fecha
from client import Client
from time import sleep


def pedir_input(mensaje, max_char=None, opciones=None, tipo=str):
    '''
    Pide un valor y se asegura de que cumpla con las condiciones
    antes de devolverlo.
    '''
    while True:
        try:
            valor = input(f'\n{mensaje}')

            if not valor:
                raise Exception('No se aceptan valores nulos.')

            elif opciones and valor not in set(o.lower() for o in opciones):
                raise Exception('El valor ingresado es inválido.')

            elif max_char and len(valor) > max_char:
                raise Exception(f'No podés superar los {max_char} caracteres.')

            elif tipo == int:
                try:
                    valor = int(valor)
                except ValueError:
                    raise Exception('El valor debe ser un entero.')

            return valor

        except Exception as e:
            print(f'\n{e}')


def intentar_de_nuevo(si_func, no_func):
    '''
    Pregunta si querés intentar de nuevo y devuelve
    la función correspndiente a la respuesta.

    Se puede invocar a la función y agregar un par de (),
    con o sin parámetros, inmediatamente después para
    ejecutar la función resultante.
    '''
    mensaje = '¿Querés intentar de nuevo? (y/n) '
    decision = pedir_input(mensaje, opciones = ('y', 'n'))

    if decision == 'y':
        return si_func

    return no_func


def publicar_tuit(client):
    borrar_pantalla()

    mensaje = '¿Qué vas a tuitear?\n\n'
    contenido = pedir_input(mensaje, max_char=280)
    respuesta = client.post_tuit(content=contenido)

    if respuesta.status_code != 201:
        print('\nNo se pudo publicar el tuit.')
        intentar_de_nuevo(publicar_tuit, menu_principal)(client)
    
    print('\n¡El tuit se publicó exitosamente!')
    sleep(2)
    tuits_personales(client)


def tuits_personales(client):
    borrar_pantalla()

    print(f'\nTuits de [{client.username}]')

    respuesta = client.get_user(client.id)

    if respuesta.status_code != 200:
        print('\nNo se pudieron leer los tuits.')
        intentar_de_nuevo(tuits_personales, menu_principal)(client)

    tuits = respuesta.json().get('tuits')

    if not tuits:
        print('\nNo hay tuits para mostrar.')
        sleep(2)
        menu_principal(client)

    for indice, tuit in enumerate(tuits):
        fecha = convertir_fecha(tuit.get('created_on'))
        contenido = tuit.get('content')
        print(f'\n{indice + 1}. {fecha}: {contenido}')
    
    print('\n'*2)
    print('1. Publicar otro tuit')
    print('2. Borrar tuit')
    print('3. Volver al menú principal')

    opciones = {str(n) for n in range(1, 4)}
    opcion = pedir_input('Opción: ', opciones=opciones, tipo=int)

    if opcion == 1:
        publicar_tuit(client)

    elif opcion == 2:
        mensaje = 'Ingresá el Nº del tuit: '
        opciones = {str(n) for n in range(1, len(tuits) + 1)}
        opcion = pedir_input(mensaje, opciones=opciones, tipo=int)
        
        client.delete_tuit(tuits[opcion - 1].get('id'))

        tuits_personales(client)
    
    else:
        menu_principal(client)


def tuits_de_otros(client):
    borrar_pantalla()

    respuesta = client.get_all_users()

    if respuesta.status_code != 200:
        print('No se pudo leer la lista de usuarios.')
        intentar_de_nuevo(tuits_de_otros, menu_principal)(client)

    usuarios = respuesta.json()

    # buscamos el diccionario correspondiente al usuario logueado
    yo_mismo = next((u for u in usuarios if u.get('id') == client.id))

    # y lo borramos de la lista
    del usuarios[usuarios.index(yo_mismo)]

    if not usuarios:
        print('\n¡Parece que sos el único usuario!')
        sleep(2)
        menu_principal(client)
    
    print('\nLista de usuarios')

    for indice, usuario in enumerate(usuarios):
        username = usuario.get('username')
        total = len(usuario.get('tuits'))

        # <s> = 's' si no hay tuits o si son más de uno, si no <s> = ''
        s = 's' if total > 1 or total == 0 else ''
        print(f'\n{indice + 1}. {username} ({total} tuit{s})')

    print('\n'*2)
    print('1. Seleccionar usuario')
    print('2. Volver al menú principal')

    opciones = {str(n) for n in range(1, 3)}
    opcion = pedir_input('Opción: ', opciones=opciones, tipo=int)

    if opcion == 2:
        menu_principal(client)

    mensaje = 'Ingresá el Nº del usuario: '
    opciones = {str(n) for n in range(1, len(usuarios) + 1)}
    opcion = pedir_input(mensaje, opciones=opciones, tipo=int)

    usuario = usuarios[opcion - 1]
    tuits = usuario.get('tuits')

    borrar_pantalla()

    print(f'\nTuits de [{usuario.get("username")}]')

    if not tuits:
        print('\nNo hay tuits para mostrar.')
        sleep(2)
        menu_principal(client)

    for indice, tuit in enumerate(tuits):
        fecha = convertir_fecha(tuit.get('created_on'))
        contenido = tuit.get('content')
        print(f'\n{indice + 1}. {fecha}: {contenido}')

    print('\n'*2)
    print('1. Buscar otro usuario')
    print('2. Volver al menú principal')

    opciones = {str(n) for n in range(1, 3)}
    opcion = pedir_input('Opción: ', opciones=opciones, tipo=int)

    if opcion == 1:
        tuits_de_otros(client)
    elif opcion == 2:
        menu_principal(client)


def administrar_cuenta(client):
    borrar_pantalla()

    print(f'\nCuenta de {client.username}:\n')
    print('1. Cambiar usuario')
    print('2. Cambiar contraseña')
    print('3. Guardar cambios')
    print('4. Volver al menú principal')

    cambios = dict()

    while True:
        opciones = {str(n) for n in range(1, 5)}
        opcion = pedir_input('Opción: ', opciones=opciones, tipo=int)

        if opcion == 1:
            cambios['username'] = pedir_input('Ingresá el nuevo usuario: ')
        
        elif opcion == 2:
            cambios['password'] = pedir_input('Ingresá la nueva contraseña: ')

        elif opcion == 3:
            respuesta = client.update_user(client.id, cambios)
            break

        elif opcion == 4:
            menu_principal(client)

    if respuesta.status_code != 200:
        errores = respuesta.json()

        for clave, valor in errores.items():
            print(f'\n{clave.capitalize()}: {valor[0]}')

        print('\n'*2)
        print('1. Intentar de nuevo')
        print('2. Volver al inicio')

        opciones = {str(n) for n in range(1, 3)}
        opcion = pedir_input('Opción: ', opciones=opciones, tipo=int)
        
        if opcion == 1:
            administrar_cuenta(client)
        else:
            main(client)
    
    print('\n¡Los cambios se efectuaron exitosamente!')

    if 'username' in cambios:
        client.username = cambios.get('username')

    if 'password' in cambios:
        client.password = cambios.get('password')

    sleep(2)
    menu_principal(client)


def menu_principal(client):
    borrar_pantalla()

    print('\nMenú Principal\n')
    print('1. Publicar nuevo tuit')
    print('2. Ver tuits personales')
    print('3. Ver tuits de otros usuarios')
    print('4. Administrar cuenta')
    print('5. Cerrar sesión')

    opciones = {str(n) for n in range(1, 6)}
    opcion = pedir_input('Opción: ', opciones=opciones, tipo=int)

    if opcion == 1:
        publicar_tuit(client)

    elif opcion == 2:
        tuits_personales(client)

    elif opcion == 3:
        tuits_de_otros(client)

    elif opcion == 4:
        administrar_cuenta(client)

    elif opcion == 5:
        main(client)


def iniciar_sesion(client):
    borrar_pantalla()
    username = pedir_input('Ingresá el usuario: ')
    password = pedir_input('Ingresá la contraseña: ')

    # intentamos loguearnos con las credenciales provistas
    # y guardamos el token en el cliente con 'save=True'
    client.get_token(username, password, save=True)

    if not client.token:
        print('\nNo se pudo iniciar sesión.')
        intentar_de_nuevo(iniciar_sesion, main)(client)

    # search devuelve una lista, así que tenemos que nos quedamos
    # con el primer resultado (que debería ser el único)
    respuesta = client.search_users(username).json()[0]

    client.id = respuesta.get('id')
    client.username = username

    menu_principal(client)


def crear_nuevo_usuario(client):
    borrar_pantalla()

    username = pedir_input('Ingresá un nombre de usuario: ', max_char=80)
    password = pedir_input('Ingresá una contraseña: ', max_char=80)

    respuesta = client.create_user(username, password)

    if respuesta.status_code != 201:
        errores = respuesta.json()

        if 'username' in errores:
            print(f'\nUsuario: {errores.get("username")[0]}')

        if 'password' in errores:
            print(f'\nContraseña: {errores.get("password")[0]}')

        print('\n'*2)
        print('1. Intentar de nuevo')
        print('2. Volver al inicio')

        opciones={str(n) for n in range(1, 3)}
        opcion = pedir_input('Opción: ', opciones=opciones, tipo=int)
        
        if opcion == 1:
            crear_nuevo_usuario(client)
        else:
            main(client)

    print('\n¡El usuario se creó exitosamente!')
    print('Redirigiendo al inicio de sesión.')
    sleep(2)
    iniciar_sesion(client)


def main(client):
    borrar_pantalla()
    
    print('\n¡Bienvenido a Tuits!\n')
    print('1. Iniciar sesión')
    print('2. Crear nuevo usuario')
    print('3. Salir')

    opciones = {str(n) for n in range(1, 4)}
    opcion = pedir_input('Opción: ', opciones=opciones, tipo=int)

    if opcion == 1:
        iniciar_sesion(client)

    elif opcion == 2:
        crear_nuevo_usuario(client)

    else:
        print()
        exit()


if __name__ == '__main__':

    client = Client(c.address, c.port)

    try:
        main(client)

    except KeyboardInterrupt:
        print('\n')
        exit()
        
    except Exception as e:
        print(f'\nOcurrió un error: {e}\n')
