# c_diccionarios.py
# muestra ejemplos de operaciones con diccionarios

# los diccionarios son pares de claves y valores encerrados entre {},
# y, al igual que los conjuntos, no admiten duplicados, PERO ENTRE SUS CLAVES

agenda = {'Ana': 43782348, 'Beto': 45872394, 'Charly': 47893489}

print(f'\nTenemos una agenda: {agenda}')

# tienen la particularidad de poder devolver el valor asociado a una clave
# referenciando a ese valor por su clave como si fuera un índice

print(f'\nagenda["Ana"] devuelve el teléfono de Ana: {agenda["Ana"]}')


# podemos agregar claves que todavía no existen del mismo modo

agenda["Dani"] = 42875937

print(f'\nActualizamos el diccionario: {agenda}')


# se comportan como conjuntos en la medida en la que no se haga alusión a sus valores,
# es decir, por defecto devuelve sólo sus claves

claves = list(agenda)

print(f'\nNombres de la agenda: {claves}')


al_reves = sorted(agenda, reverse=True)

print(f'\nDados vuelta: {al_reves}')


print(f'\nPregunto si Ana está en la agenda: {"Ana" in agenda}')
print(f'\nPregunto si Juan está en la agenda: {"Juan" in agenda}')


# el método dict() acepta dos maneras de pasarle valores para crear diccionarios

numeros_por_clave = dict(uno=1, dos=2, tres=3, cuatro=4)

numeros_por_coleccion = dict([('uno', 1), ('dos', 2), ('tres', 3), ('cuatro', 4)])

print(f'\ndict() con claves: {numeros_por_clave}')
print(f'\ndict() con colecciones: {numeros_por_coleccion}')


# admiten ser creados por comprensión

cuadrados = {x: x**2 for x in range(1, 6)}

print(f'\nDiccionario de cuadrados: {cuadrados}')


# entre los métodos más comunmente utilizados encontramos:

ana = agenda.get('Ana')
dani = agenda.get('Dani')

print(f'\ndict.get() devuelve el valor asociado al argumento: Ana = {ana}, Dani = {dani}')


copia = agenda.copy()

print(f'\ndict.copy() devuelve una copia: {copia}')


dani_copia = copia.pop('Dani')

print(f'\ndict.pop() borra una clave devolviendo su valor: Dani = {dani_copia}')
print(f'\nCopia actualizada: {copia}')


claves = agenda.keys()

print(f'\ndict.keys() devuelve las claves: {claves}')


valores = agenda.values()

print(f'\ndict.values() devuelve los valores: {valores}')


items = agenda.items()

print(f'\ndict.items() devuelve pares de clave/valor: {items}')


# al igual que dict(), dict.update() admite dos maneras de pasar diccionarios

agenda.update(Ana=48973478)

print(f'\ndict.update() admite actualizar por clave: {agenda}')


agenda.update({'Eze': 46982190})

print(f'\nY también pasarle un diccionario: {agenda}')

print()
