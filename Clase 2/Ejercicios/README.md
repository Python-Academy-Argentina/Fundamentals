# Ejercicios

De manera ideal, los ejercicios deberían ser resueltos en archivos separados, de manera que puedan ser ejecutados como:
```bash
> python3 archivo.py
```

### Temario de consignas
**[a. Funciones](#a-funciones)**<br>
**[b. Listas](#b-listas)**<br>
**[c. Cadenas](#c-cadenas)**<br>
**[d. Excepciones](#d-excepciones)**<br>


## Consignas

### a. Funciones

1. Desarrollar una función que reciba tres números positivos y devuelva el mayor de los tres, sólo si éste es único (mayor estricto). En caso de no existir el mayor estricto devolver -1. No utilizar operadores lógicos (```and, or, not```). Desarrollar también un programa para ingresar los tres valores, invocar a la función y mostrar el máximo hallado, o un mensaje informativo si este no existe.

2. Desarrollar una función que reciba tres números enteros positivos y verifique si corresponden a una fecha válida (día, mes, año). Devolver True o False según la fecha sea correcta o no. Realizar también un programa para verificar el comportamiento de la función.

3. Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo dentro de un mes. Sabiendo que dicho medio de transporte utiliza un esquema de tarifas decrecientes (detalladas en la tabla de abajo) se solicita desarrollar una función que reciba como parámetro la cantidad de viajes realizados en un determinado mes y devuelva el total gastado en viajes. Realizar también un programa para verificar el comportamiento de la función.

<div align="center">

| Cantidad de viajes | Valor del pasaje                     |
|------------------- | -------------------------------------|
| 1 a 20             | Averiguar valor actualizado          |
| 21 a 30            | 20% de descuento sobre tarifa máxima |
| 31 a 40            | 30% de descuento sobre tarifa máxima |
| Más de 40          | 40% de descuento sobre tarifa máxima |

</div>

4. Un comercio de electrodomésticos necesita para su línea de cajas un programa que le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan dos números enteros, correspondientes al total de la compra y al dinero recibido. Informar cuántos billetes de cada denominación deben ser entregados al cliente como vuelto, de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes de $500, $100, $50, $20, $10, $5 y $1. Emitir un mensaje de error si el dinero recibido fuera insuficiente. Ejemplo: Si la compra es de $317 y se abona con $500, el vuelto debe contener 1 billete de $100, 1 billete de $50, 1 billete de $20, 1 billete de $10 y 3 billetes de $1.

5. Desarrollar una función que reciba como parámetros dos números enteros positivos y devuelva el número que resulte de concatenar ambos valores. Por ejemplo, si recibe ```1234``` y ```567``` debe devolver ```1234567```. No se permite utilizar facilidades de Python no vistas en clase.

6. Escribir una función ```dia_siguiente()``` que reciba como parámetro una fecha cualquiera expresada por tres enteros (correspondientes al día, mes y año) y calcule y devuelva tres enteros correspondientes al día siguiente al dado. Utilizando esta función, desarrollar programas que permitan:

   - Sumar N días a la fecha.
   - Calcular la cantidad de días existentes entre dos fechas cualquiera.

7. Resolver el siguiente problema diseñando y utilizando funciones:

   Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso para poder cargar el camión de reparto. La empresa cuenta con N camiones, y cada uno puede transportar hasta media tonelada (500kg). En un cajón caben 100 naranjas con un peso entre 200 y 300 gramos cada una. Si el peso de alguna naranja se encuentra fuera del rango indicado, se clasifica para procesar como jugo. Se solicita desarrollar un programa para ingresar la cantidad de naranjas cosechadas e informar cuántos cajones se pueden llenar, cuántas naranjas son para jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente reparto. Simular el peso de cada unidad generando un número entero al azar (ya vimos ```random.randint(a, b)```) entre 150 y 350.

   Además, se desea saber cuántos camiones se necesitan para transportar la cosecha, considerando que la ocupación del camión no debe ser inferior al 80%; en caso contrario, el camión no será despachado por su alto costo.


### b. Listas

1. Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento imprimiendo la lista luego de invocar a cada función:

   - Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también será un número al azar de dos dígitos.
   - Calcular y devolver la sumatoria de todos los elementos de la lista anterior.
   - Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar se ingresa desde el teclado y la función lo recibe como parámetro.
   - Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas auxiliares. Un ejemplo de lista capicúa es ```[50, 17, 91, 17, 50]```.

2. Escribir funciones para:

   - Generar una lista de 50 números aleatorios del 1 al 100.
   - Recibir una lista como parámetro y devolver True si la misma contiene algún elemento repetido. La función no debe modificar la lista.
   - Recibir una lista como parámetro y devolver una nueva lista con los elementos únicos de la lista original, sin importar el orden.

   Combinar estas tres funciones en un mismo programa.

3. Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos), donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valores de la lista.

4. Eliminar de una lista de palabras las palabras que se encuentren en una segunda lista. Imprimir la lista original, la lista de palabras a eliminar y la lista resultante.

5. Escribir una función que reciba una lista como parámetro y devuelva ```True``` si la lista está ordenada en forma ascendente o ```False``` en caso contrario. Por ejemplo, ```ordenada([1, 2, 3])``` retorna ```True``` y ```ordenada(['b', 'a'])``` retorna ```False```. Desarrollar además un programa para verificar el comportamiento de la función.

6. Intercalar los elementos de una lista entre los elementos de otra. La intercalación deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará una lista nueva sino que se modificará la primera. Por ejemplo, si ```lista1 = [8, 1, 3]``` y ```lista2 = [5, 9, 7]```, lista1 deberá quedar como ```[8, 5, 1, 9, 3, 7]```.

7. Utilizar la técnica de listas por comprensión para construir una lista con todos los números impares comprendidos entre 100 y 200.

8. Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7 que no sean múltiplos de 5. A y B se ingresar desde el teclado.

9. Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con los elementos de la primera que sean impares. El proceso deberá realizarse utilizando listas por comprensión. Imprimir las dos listas por pantalla.

10. Resolver el siguiente problema, disenando las funciones a utilizar:

    Una clínica necesita un programa para atender a sus pacientes. Cada paciente que ingresa se anuncia en la recepción indicando su número de afiliado (número entero de 4 dígitos) y además indica si viene por una urgencia (ingresando un 0) o con turno (ingresando un 1). Para finalizar se ingresa -1 como número de socio. Luego se solicita:

    - Mostrar un listado de los pacientes atendidos por urgencia y un listado de los pacientes atendidos por turno en el orden que llegaron a la clínica.
    - Realizar la búsqueda de un número de afiliado e informar cuántas veces fue atendido por turno y cuántas por urgencia. Repetir esta búsqueda hasta que se ingrese -1 como número de afiliado.

11. Resolver el siguiente problema, utilizando funciones:

    Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se ingresa el número de socio de cinco dígitos hasta ingresar un cero como fin de carga. Se solicita:

    - Informar para cada socio, cuántas veces ingresó al club (cada socio debe aparecer una sola vez en el informe).
    - Solicitar un número de socio que se dio de baja del club y eliminar todos sus ingresos. Mostrar los registros de entrada al club antes y después de eliminarlo. Informar cuántos ingresos se eliminaron.


### c. Cadenas

1. Desarrollar una función que determine si una cadena de caracteres es capicúa, sin utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita verificar su funcionamiento.

2. Los números de claves de dos cajas fuertes están intercalados dentro de un número entero llamado "clave maestra", cuya longitud no se conoce. Realizar un programa para obtener ambas claves, donde la primera se construye con los dígitos ubicados en posiciones impares de la clave maestra y la segunda con los dígitos ubicados en posiciones pares. Los dígitos se numeran desde la izquierda. Ejemplo: Si clave maestra fuera ```18293```, la clave 1 sería ```123``` y la clave 2 sería ```89```.

3. Escribir una función que reciba como parámetro un número entero entre 0 y 3999 y lo convierta en un número romano, devolviéndolo en una cadena de caracteres. ¿En qué cambiaría la función si el rango de valores fuese diferente?

4. Escribir una función ```filtrar_palabras()``` que reciba una cadena de caracteres conteniendo una frase y un entero N, y devuelva otra cadena con las palabras que tengan N o más caracteres de la cadena original. Escribir también un programa para verificar el comportamiento de la misma. Hacer tres versiones de la función, para cada uno de los siguientes casos:

   - Utilizando sólo ciclos normales
   - Utilizando listas por comprensión
   - Utilizando la función filter

5. Desarrollar una función que extraiga una subcadena de una cadena de caracteres, indicando la posición y la cantidad de caracteres deseada. Devolver la subcadena como valor de retorno. Escribir también un programa para verificar el comportamiento de la misma. Ejemplo, dada la cadena ```"El número de teléfono es 4356- 7890"``` extraer la subcadena que comienza en la posición 25 y tiene 9 caracteres, resultando la subcadena ```"4356-7890"```. Escribir una función para cada uno de los siguientes casos:

   - Utilizando rebanadas
   - Sin utilizar rebanadas

6. Escribir una función que reciba como parámetro una cadena de caracteres en la que las palabras se encuentran separadas por uno o más espacios. Devolver otra cadena con las palabras ordenadas alfabéticamente, dejando un espacio entre cada una.

7. Desarrollar una función que devuelva una subcadena con los últimos N caracteres de una cadena dada. La cadena y el valor de N se pasan como parámetros.

8. Desarrollar una función para reemplazar todas las apariciones de una palabra por otra en una cadena de caracteres y devolver la cadena obtenida y un entero con la cantidad de reemplazos realizados. Tener en cuenta que sólo deben reemplazarse palabras completas, y no fragmentos de palabras. Escribir también un programa para verificar el comportamiento de la función.

9. Escribir un programa para crear una lista por comprensión con los naipes de la baraja española. La lista debe contener cadenas de caracteres. Ejemplo: ```["1 Oros", "2 Oros", ... ]```. Imprimir la lista por pantalla.

10. Muchas aplicaciones financieras requieren que los números sean expresados también en letras. Por ejemplo, el número 2153 puede escribirse como "dos mil ciento cincuenta y tres". Escribir un programa que utilice una función para convertir un número entero entre 0 y 1 billón (1.000.000.000.000) a letras. ¿En qué cambiaría la función si también aceptara números negativos? ¿Y números con decimales?


### d. Excepciones

1. Desarrollar una función para ingresar a través del teclado un número natural. La función rechazará cualquier ingreso inválido de datos utilizando excepciones y mostrar la razón exacta del error. Controlar que se ingrese un número, que ese número sea entero y que sea mayor que 0. Devolver el valor ingresado cuando este sea correcto. Escribir también un programa que permita probar el correcto funcionamiento de la misma.

2. Realizar una función que reciba como parámetros dos cadenas de caracteres conteniendo números reales, sume ambos valores y devuelva el resultado como un número real. Devolver -1 si alguna de las cadenas no contiene un número válido, utilizando manejo de excepciones para detectar el error.

3. Desarrollar una función que devuelva una cadena de caracteres con el nombre del mes cuyo número se recibe como parámetro. Los nombres de los meses deberán obtenerse de una lista de cadenas de caracteres inicializada dentro de la función. Devolver una cadena vacía si el número de mes es inválido. La detección de meses inválidos deberá realizarse a través de excepciones.

4. Todo programa Python es susceptible de ser interrumpido mediante la pulsación de las teclas ```Ctrl + C```, lo que genera una excepción del tipo KeyboardInterrupt. Realizar un programa para imprimir los números enteros entre 1 y 100000, y que solicite confirmación al usuario antes de detenerse cuando se presione ```Ctrl + C```.

5. La raíz cuadrada de un número puede obtenerse mediante la función sqrt del módulo math (```from math import sqrt```). Escribir un programa que utilice esta función para calcular la raíz cuadrada de un número cualquiera ingresado a través del teclado. El programa debe utilizar manejo de excepciones para evitar errores si se ingresa un número negativo.

6. El método index permite buscar un elemento dentro de una lista, devolviendo la posición que este ocupa. Sin embargo, si el elemento no pertenece a la lista se produce una excepción de tipo IndexError. Desarrollar un programa que cargue una lista con números enteros ingresados a través del teclado (terminando con -1) y permita que el usuario ingrese el valor de algunos elementos para visualizar la posición que ocupan, utilizando el método index. Si el número no pertenece a la lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el proceso al tercer error detectado. No utilizar el operador in durante la búsqueda.

7. Escribir un programa que juegue con el usuario a adivinar un número. El programa debe generar un número al azar entre 1 y 500 y el usuario debe adivinarlo. Para eso, cada vez que se introduce un valor se muestra un mensaje indicando si el número que tiene que adivinar es mayor o menor que el ingresado. Cuando consiga adivinarlo, se debe imprimir en pantalla la cantidad de intentos que le tomó hallar el número. Si el usuario introduce algo que no sea un número se mostrará un mensaje en pantalla y se lo contará como un intento más.
