# Ejercicios

De manera ideal, los ejercicios deberían ser resueltos en archivos separados, de manera que puedan ser ejecutados como:
```bash
> python3 archivo.py
```

### Temario de consignas
**[a. Imprimiendo en pantalla](#a-imprimiendo-en-pantalla)**<br>
**[b. Operaciones aritméticas](#b-operaciones-aritméticas)**<br>
**[c. Estructuras de control: Condicionales](#c-estructuras-de-control-condicionales)**<br>
**[d. Estructuras de control: Bucles](#d-estructuras-de-control-bucles)**<br>
**[e. Ejercicios integradores](#e-ejercicios-integradores)**<br>


## Consignas

### a. Imprimiendo en pantalla

1. Mostrar el mensaje "Hola, Mundo."

2. Ingresar el nombre de un usuario y saludarlo. Ejemplo: Si el usuario se llama Juan, debe mostrar el mensaje "Hola, Juan."


### b. Operaciones aritméticas

1. Ingresar dos números y mostrar la suma y la diferencia.

2. Ingresar tres números y mostrar la suma y el promedio.

3. Ingresar el monto de una factura y calcular el IVA (21%).

4. Calcular el promedio de las notas que obtiene un alumno al rendir dos parciales. Se debe imprimir el nombre del alumno y la nota final.

5. Tres personas invierten dinero para fundar una empresa (no necesariamente en partes iguales). Calcular qué porcentaje invirtió cada una. Se debe imprimir el monto total, además del nombre de cada inversor y el porcentaje contribuído.

6. Una persona quiere invertir su capital en un banco y quiere saber cuánto dinero gana en un mes si el banco paga 2% mensual. Se debe mostrar el monto a 3, 6 y 12 meses.

7. Una inmobiliaria paga a sus vendedores un salario base, más una comisión fija por cada venta realizada, más el 5% del valor de esas ventas. Realizar un programa que imprima el número del vendedor y el salario que le corresponde en un determinado mes. Se leen por teclado el número del vendedor, la cantidad de ventas que realizó y el valor total de las mismas.

8. Un banco necesita para sus cajeros de la sucursal un programa que lea una cantidad de dinero que desea retirar el cliente e imprima a cuántos billetes equivale, considerando que existen billetes de $1000, $500, $200, $100, $50, $20 y el resto en monedas de $10, $5, $2 y $1. Desarrollar dicho programa de tal forma que se minimice la cantidad de billetes entregados por el cajero.

9. Leer un período en segundos e imprimirlo expresado en días, horas, minutos y segundos. Por ejemplo, 200000 segundos equivalen a 2 días, 7 horas, 33 minutos y 20 segundos.


### c. Estructuras de control: Condicionales

1. Ingresar dos números enteros e indicar si son iguales o distintos.

2. Leer un número entero e imprimir un mensaje indicando si es par o impar.

3. Crear un programa que pida un número de mes (ejemplo 4) y escriba el nombre del mes en letras ("abril"). Verificar que el mes sea válido e informar en caso que no lo sea.

4. Ingresar las notas de los dos parciales de un alumno e indicar si promocionó, aprobó o debe recuperar. Si el valor de la nota no esta entre 0 y 10, debe informar un error.

   - Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
   - Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
   - Se debe recuperar cuando al menos una de las dos notas es menor a 4.

5. Una remisería requiere un sistema que calcule el precio de un viaje a partir de la cantidad de km que desea recorrer el usuario. Tiene la siguiente tarifa:

   - Viaje mínimo $50
   - Si recorre entre 0 y 10km: $20/km
   - Si recorre 10km o más: $15/km

6. Leer un número correspondiente a un año e imprimir un mensaje indicando si es bisiesto o no. Se recuerda que un año es bisiesto cuando es divisible por 4. Sin embargo, aquellos años que sean divisibles por 4 y también por 100 no son bisiestos, a menos que también sean divisibles por 400. Por ejemplo, 1900 no fue bisiesto, pero sí el 2000.


### d. Estructuras de control: Bucles

1. Escribir un algoritmo que muestre los primeros 25 números naturales.

2. Calcular e imprimir la suma de los números comprendidos entre 42 y 176.

3. Mostrar las tablas de multiplicar (entre 1 y 10) del número 4. ¿Cómo cambiarías el algoritmo para que el usuario pueda decidir la tabla de multiplicar a mostrar?

4. Escribir un algoritmo que lea números enteros hasta que se ingrese un 0, y muestre el máximo, el mínimo (sin considerar el 0) y la media (promedio) de todos ellos (pensá cómo tenés que inicializar las variables).

5. Ingresar números, hasta que la suma de los números pares supere 100. Mostrar cuántos números en total se ingresaron.

6. Un negocio desea saber el importe total recaudado al fin del día, desea contar con un programa que pueda ingresar el importe de cada venta realizada. Para indicar que finalizó el día se ingresa **-1**. ¿Cuál es el monto total vendido y cuántas ventas se realizaron? El importe de cada venta realizada debe ser un valor positivo.

7. Se desea analizar cuántos autos circulan con patente que tiene numeración par y cuántos con numeración impar en un día. Le solicitan escribir un algoritmo que permita ingresar la terminación de la patente (entre 0 y 9) hasta ingresar **-1** e informar cuántas se ingresaron con numeración par y cuántas con numeración impar.

8. Ingresar un número n, validar que sea positivo. Luego:

   Mostrar los primeros n números impares hasta el número ingresado. Ejemplo:

     - Si se ingresa 5, se debe mostrar: ```1 3 5```
     - Si se ingresa 8, se debe mostrar: ```1 3 5 7```
     - Si se ingresa -5, se debe pedir otro número.</ul><br>

   Informar la suma de esos números impares.


### e. Ejercicios integradores

1. Leer números que representan edades de un grupo de personas, finalizando la lectura cuando se ingrese el número 999. Imprimir cuántos son menores de 18 años, cuántos tienen 18 años o más y el promedio de edad de ambos grupos. Descartar valores que no representan una edad válida. (Se considera válido una edad entre 0 y 100).

2. Una empresa aplica el siguiente procedimiento en la comercialización de sus productos:

   - Aplica el precio base a la primera docena de unidades.
   - Aplica un 10% de descuento a todas las unidades entre 13 y 100.
   - Aplica un 25% de descuento a todas las unidades por encima de las 100.</ul><br>

   Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio base es 100. El cálculo resultante sería: ```100 * 12 + 90 * 88 + 75 * 130 = 18870```, y el precio promedio será ```18870 / 230 = 82,04```.
   
   Escribir un algoritmo que lea la cantidad solicitada de un producto y su precio base, y muestre el valor total de la venta y el precio promedio por unidad. El fin de carga se determina ingresando **-1** como cantidad solicitada. Al finalizar informar:

   * Cantidad total de ventas realizadas.
   * Cantidad de ventas a la que se le aplicó un 10% de descuento.
   * Cantidad de ventas a la que **sólo** se le aplicó el precio base, sin descuentos.

3. Una empresa factura a sus clientes el último día de cada mes. Si el cliente paga su factura dentro de los primeros 10 días del mes siguiente, tiene un descuento de $120 o del 2% de la factura (lo que resulte más conveniente para el cliente). Si paga en los siguientes 10 días del mes deberá pagar el importe original de la factura, mientras que si paga después del día 20 deberá abonar una multa de $150 o del 10% de su factura (lo que resulte mayor). Escriba un algoritmo que lea el número del cliente y el total de la factura, y emita un informe donde conste el número del cliente y los tres importes que podrá abonar según la fecha de pago.

4. Una empresa cuenta con N empleados, divididos en tres categorías A, B y C. Por cada empleado se lee su legajo, categoría y salario. Se solicita elaborar un informe que contenga:

   - Importe total de salarios pagados por la empresa.
   - Cantidad de empleados que ganan más de $20000.
   - Cantidad de empleados que ganan menos de $5000, cuya categoría sea "C".
   - Legajo del empleado que más gana.
   - Sueldo más bajo.
   - Importe total de sueldos por cada categoría.
   - Salario promedio.

5. Ingresar por teclado la cantidad de términos a generar de la siguiente serie: ```1 7 19 43 91 187 379 763 1531 3067 6139```\
   El primer término es el 1 y cada término se genera como el doble del término anterior más 5. Mostrar la serie por pantalla e informar la suma de los términos generados.
