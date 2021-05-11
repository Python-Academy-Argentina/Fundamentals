# solo_pares.py
# imprime sólo números pares en <enteros>

enteros = list(range(10))

for n in enteros:

    if n != 0:    # si <n> no es 0

        pass

    else:    # si <n> es 0, continúa con la siguiente iteración

        continue

    if n % 2 == 0:

        print(n)
