# index.py
# muestra el índice de cada ítem en una lista junto a su respectivo ítem

palabras = ['python', 'academy', 'fundamentals']

# usamos range() y len() para conseguir un iterador
# de tantos índices como ítems haya en la lista

for i in range(len(palabras)):

    print(i, palabras[i])
