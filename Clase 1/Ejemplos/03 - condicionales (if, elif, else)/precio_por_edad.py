# precio_por_edad.py
# calcula el precio de una entrada según la edad ingresada

print('Bienvenid@ al cine de la Python Academy.')

edad = int(input('Ingresá tu edad: '))

if edad < 12:
    precio = 100

elif 12 <= edad < 18:
    precio = 120

else:
    precio = 150

print(f'\nEl valor de tu entrada es ${precio}.')
