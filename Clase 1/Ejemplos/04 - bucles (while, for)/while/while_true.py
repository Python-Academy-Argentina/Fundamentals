# while_true.py
# cuenta indefinidamente hasta que se frene ejecutando Ctrl + C

import time    # importamos el módulo time

n = 0

while True:    # True es verdadero, así que el bucle inicia

    print(n)

    n += 1

    time.sleep(0.5)    # usamos el método sleep() para esperar 1/2 segundo
                       # antes de seguir con la próxima iteración
