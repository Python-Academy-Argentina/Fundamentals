# fibonacci.py
# imprime la secuencia Fibonacci hasta el número ingresado

limite = int(input('Ingresá un número: '))
print()

a, b = 0, 1

while a < limite:    # el bucle termina cuando a == limite

    print(a, end=' ')    # usamos espacio en lugar de una nueva línea

    a, b = b, a+b

print()
