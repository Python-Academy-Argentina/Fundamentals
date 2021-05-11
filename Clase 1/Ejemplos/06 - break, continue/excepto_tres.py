# excepto_tres.py
# imprime <num> salteándose el 3

num = 0

while num < 6:    # mientras <num> sea menor que 6

    num += 1

    if num == 3:

        continue    # sigue con la próxima iteración

    print(num)
