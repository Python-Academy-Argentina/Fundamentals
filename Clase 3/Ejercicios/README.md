# Ejercicios

De manera ideal, los ejercicios deberían ser resueltos en archivos separados, de manera que puedan ser ejecutados como:
```bash
> python3 archivo.py
```

### Temario de consignas
**[a. Estructuras de Datos](#a-estructuras-de-datos)**<br>
**[b. Archivos](#b-archivos)**<br>
**[c. Clases](#c-clases)**<br>


## Consignas

### a. Estructuras de Datos

1.	Desarrollar las siguientes funciones utilizando tuplas para representar fechas y horarios, y luego escribir un programa para verificar su comportamiento:

      - Ingresar una fecha desde el teclado, verificando que corresponda a una fecha válida.
      - Sumar N días a una fecha.
      - Ingresar un horari o desde teclado, verificando que sea correcto.
      - Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al segundo se considerará que el primero corresponde al día anterior. En ningún caso la diferencia en horas puede superar las  24 horas.

2.	Escribir una función que reciba como parámetro una tupla conteniendo una fecha ```(día, mes, año)``` y devuelva una cadena de caracteres con la misma fecha expresada en formato extendido. Por ejemplo, para ```(12, 10, 17)``` devuelve ```"12 de Octubre de 2017"```. Escribir también un programa para verificar su comportamiento.

3.	Desarrollar un programa que utilice una función que reciba como parámetro una cadena de caracteres conteniendo una dirección de correo electrónico y devuelva una tupla con las distintas partes que componen dicha dirección. Ejemplo: ```alguien@ar.ibm.com``` --> ```(alguien, uade, edu, ar)```.

4.	Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son recibidas en dos tuplas, por ejemplo: ```(3, 4)``` y ```(5, 4)```. La función devuelve True o False. Escribir también un programa para verificar su comportamiento.

5.	Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar las palabras ordenadas según su longitud.

6.	Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al usuario y eliminarlos del conjunto mediante el método ```remove()```, mostrando el contenido del conjunto luego de cada eliminación. Finalizar el proceso al ingresar -1. Utilizar manejo de excepciones para evitar errores al intentar quitar elementos inexistentes.

7.	Generar e imprimir un diccionario donde las claves sean números enteros entre 1 y 20 (ambos incluidos) y los valores asociados sean el cuadrado de las claves.

8.	Escribir una función que reciba un número entero N y devuelva un diccionario con la tabla de multiplicar de N del 1 al 12. Escribir también un programa para probar la función.

9.	Desarrollar una función ```eliminar_claves()``` que reciba como parámetros un diccionario y una lista de claves. La función debe eliminar del diccionario todas las claves contenidas en la lista, devolviendo el diccionario modificado y un valor de verdad que indique si la operación fue exitosa. Desarrollar también un programa para verificar su comportamiento.

10. Crear una función ```contar_vocales()```, que reciba una palabra y cuente cuántas letras "a" contiene, cuántas "e", cuántas "i", etc. Devolver un diccionario con los resultados. Desarrollar un programa para leer una frase e invocar a la función por cada palabra que contenga la misma. Imprimir cada palabra y la cantidad de vocales hallada.

11. Una librería almacena su lista de precios en un diccionario. Disenar un programa para crearlo, incrementar los precios de los cuadernos en un 15%, imprimir un listado con todos los elementos de la lista de precios e indicar cuál es el ítem más costoso que venden en el comercio.

12. Escribir una función ```buscar_clave()``` que reciba como parámetros un diccionario y un valor, y devuelva una lista de claves que apunten ("mapeen") a ese valor en el diccionario. Comprobar el comportamiento de la función mediante un programa apropiado.


### b. Archivos

1.	Desarrollar un programa para eliminar todos los comentarios de un programa escrito en lenguaje Python. Tener en cuenta  que los comentarios comienzan con el signo ```#``` (siempre que este no se encuentre encerrado entre comillas simples o dobles) y que también se considera comentario a las cadenas de documentación (doc strings).

2.	Escribir un programa que permita grabar un archivo los datos de lluvia caída durante un año. Cada línea del archivo se grabará con el siguiente formato: ```<dia>;<mes>;lluvia caída en mm```. Por ejemplo: ```25;5;319```

      Los datos se generarán mediante números al azar, asegurándose que las fechas sean válidas. La cantidad de registros también será un número al azar entre 50 y 200.

      Por último se solicita leer el archivo generado e imprimir un informe en formato matricial donde cada columna represente a un mes y cada fila corresponda a los días del mes. Imprimir además el total de lluvia caída en todo el año.

3.	Una institución deportiva necesita clasificar a sus atletas para inscribirlos en los próximos Juegos Panamericanos. Para eso encargó la realización de un programa que incluya las siguientes funciones:

      - ```grabar_rango_alturas()``` graba en un archivo las alturas de los atletas de distintas disciplinas, que se ingresan desde el teclado. Cada dato se debe grabar en una línea distinta. Ejemplo:

         <deporte 1><br>
         <altura del atleta 1><br>
         <altura del atleta 2><br>
         <deporte 2><br>
         <altura del atleta 1><br>
         <altura del atleta 2><br>
         <...><br>

      - ```grabar_promedio()``` graba en un archivo los promedios de las alturas de los atletas presentes en el archivo generado en el paso anterior. La disciplina y el promedio deben grabarse en líneas diferentes. Ejemplo:

         <deporte 1><br>
         <promedio de alturas deporte 1><br>
         <deporte 2><br>
         <promedio de alturas deporte 2><br>
         <...><br>

      - ```mostrar_mas_altos()``` muestra por pantalla las disciplinas deportivas cuyos atletas superan la estatura promedio general. Obtener los datos del segundo archivo.

4.	Escribir un programa que lea un archivo de texto conteniendo un conjunto de apellidos y nombres en formato ```Apellido, Nombre``` y guarde en el archivo ```Armenia.txt``` los nombres de aquellas personas cuyo apellido terminan con la cadena ```ian```, en el archivo ```Italia.txt``` los terminados en ```ini``` y en el archivo ```España.txt``` los terminados en ```ez```. Descartar el resto. Ejemplo:

      Arslanian, Gustavo --> Armenia.txt<br>
      Rossini, Giuseppe  --> Italia.txt<br>
      Pérez, Juan --> España.txt<br>
      Smith, John --> descartar<br>

      El archivo de entrada puede ser creado mediante el block de notas o el IDLE. No escribir un programa para generarlo.


### c. Clases

1. <b>Pilas</b>

   Una pila es una estructura de datos que permite almacenar y recuperar datos, siendo el modo de acceso a sus elementos de tipo LIFO (del inglés Last In, First Out: último en entrar, primero en salir). Es una estructura muy utilizada en informática debido a su simplicidad y capacidad de dar respuesta a numerosos procesos.

   Para el manejo de los datos cuenta con dos operaciones básicas: ```apilar``` (push), que coloca un objeto en la pila, y su operación inversa, ```retirar``` o ```desapilar``` (pop), que retira el último elemento apilado.

   Desarrollar una clase ```Pila``` que contenga métodos para resolver las siguientes operaciones:

   - Agregar un nuevo elemento a la pila (siempre al final).

   - Remover un elemento de la pila (siempre el último), devolviendo su valor.

   - Devolver la suma de los elementos de la pila, si y sólo si todos los elementos de la pila son números. Caso contrario, arrojar una excepción de tipo ```ValueError``` o ```TypeError``` con un mensaje claro indicando el inconveniente.

   - Devolver una copia de la pila en el orden inverso sin modificar la pila original.

   - Invertir los contenidos de la pila modificando la pila original.

   - Devolver una copia ordenada de la pila sin modificar la pila original.

   - Ordenar los contenidos de la pila modificando la pila original.

   - Reemplazar todas las apariciones de un valor viejo por uno nuevo. El método debe recibir dos argumentos: ```viejo``` y ```nuevo```

   Hacer uso de la clase para resolver el siguiente problema:

      - Un conductor viaja de un pueblo origen a un pueblo destino, pasando por varios pueblos intermedios. Una vez en el destino, el conductor debe regresar a casa por el mismo camino. Desarrollar un programa que permita al conductor registrar cada pueblo visitado y al finalizar el viaje le indique el camino de regreso.


2. <b>Colas</b>

   Una cola es una estructura de datos caracterizada por ser una secuencia de elementos en la que la operación de inserción (push) se realiza por un extremo y la operación de extracción (pull) por el otro. También se le llama estructura FIFO (del inglés First In, First Out), debido a que el primer elemento en entrar será también el primero en salir.

   Desarrollar una clase ```Cola``` que contenga métodos para resolver las siguientes operaciones:

   - Agregar un nuevo elemento a la cola (siempre al final).

   - Remover un elemento de la cola (siempre el primero), devolviendo su valor.

   Hacer uso de la clase para resolver los siguientes problemas:

      - Una universidad cuenta con una cola de estudiantes y graduados, donde cada persona se representa mediante una tupla (situación, DNI) (la situación se codifica como 0: estudiante, 1: graduado). Dividirla en dos nuevas colas según el nivel educativo de cada integrante.

      - Se tiene una cola en la que se han repartido números con el orden de atención. Cada integrante se representa mediante una tupla (número de orden, DNI). Sin embargo hay muchos "colados" en la misma,  los  que  carecen  de  número (```None```). Por eso se le ha ordenado al personal de seguridad que retire a todos aquellos que no tienen número. Mostrar la cola inicial, los DNI de quienes fueron retirados de la cola y la cola final.

      - Escribir un programa que devuelva la concatenación de dos colas de números enteros, respetando el orden original de cada una.

      - Escribir un programa que devuelva la concatenación de dos colas de números enteros, respetando valor de los elementos de cada una. La cola final debe quedar ordenada de menor a mayor.

      - Cargar desde el teclado una instancia de la clase Cola. Imprimir un mensaje indicando si el contenido del objeto es capicúa.
