# a_sep_por_coma.py
# programa que crea, escribe un archivo CSV de números y sus potencias
# luego lo cierra, lo abre para lectura e imprime sus contenidos

def potencias(n):
    '''
    Devuelve una tupla con <n> a la segunda,
    tercera, cuarta y quinta potencias.
    '''
    return n**2, n**3, n**4, n**5


encabezados = ['numero', 'cuadrado', 'cubo', 'cuarta', 'quinta']


# creamos un archivo con 'w', y lo borramos si ya existe
print('\nEscribimos un archivo CSV con potencias.')

f = open('potencias.csv', 'w')

# encabezados
f.write(','.join(encabezados) + '\n')

# escribimos las potencias del 2 al 5
for n in range(2, 6):
    f.write(f'{n},')
    f.write(','.join([str(n) for n in potencias(n)]))
    f.write('\n')

# cerramos el archivo
f.close()

# ahora lo abrimos y lo imprimimos en pantalla
print('\nLo cerramos y volvemos a abrir para lectura:\n')

# genero una lista con los renglones (menos el primero)
renglones = [r for r in open('potencias.csv', 'r')][1::]

for renglon in renglones:
    v = renglon.strip().split(',')
    print(
        f'{v[0]} al cuadrado es {v[1]}, '
        f'al cubo es {v[2]}, '
        f'a la cuarta es {v[3]}, '
        f'y a la quinta es {v[4]}.'
    )

print()
