# si_o_no.py
# pregunta por sí o por no hasta recibir una respuesta válida o agotar los intentos
# no devuelve 'sí' o 'no', sino un booleano (sí: True; no: False)

def si_o_no(mensaje, intentos=4, error='Intentá de nuevo.'):
    """
    Pregunta por sí o por no hasta recibir una respuesta válida
    o agotar el número de intentos.

    Devuelve True o False, dependiendo del valor de la respuesta.

    Si se pasa intentos=0, no hay límite de intentos.
    """
    while True:

        ok = input(mensaje)

        if ok.lower() in ('y', 'yes', 'n', 'no'):
            break

        intentos -= 1

        if intentos == 0:
            print('Respuesta inválida.')
            break

        print(error)

    return ok.lower() in ('y', 'yes')


si_o_no('¿Desea continuar? ', intentos=5)

si_o_no(
    mensaje='¿De verdad querés borrar el archivo? ',
    intentos=0,
    error='Dale, capo. Media pila.'
)
