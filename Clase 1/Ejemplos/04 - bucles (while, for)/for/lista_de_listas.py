# lista_de_listas.py
# imprime los ítems en cada lista dentro de <lista_de_listas>

lista_de_listas = [
    [1, 2, 3],
    ['cuatro', 'cinco', 'seis'],
    [7, 8, 9],
]

# usamos enumerate() para generar índices
# de cada ítem en la lista (desde 0)

for index, lista in enumerate(lista_de_listas):

    print(f'\nLista {index + 1}:')
    
    for item in lista:

        print(f' - {item}')

print()
