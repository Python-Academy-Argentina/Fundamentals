# palabras.py
# imprime palabras que no empiezan con "f"
# ni tienen menos que 4 caracteres

palabras = ['python', 'academy', 'fundamentals', 'ibm', 'kyndryl']

for p in palabras:

    if len(p) < 4:    # si <p> tiene menos que 4 caracteres

        continue

    if p.startswith('f'):    # si <p> empieza con "f"

        continue

    print(p)    # si no entra en ningún if, imprime <p>
