# SimpleDeDllang

Lenguaje "Turing completo" que cumple las funciones basicas del modelo L definido por Davis.

Dos modos de uso:

+ Interactivo:
  + Se accede ejecutando main.py sin ningún archivo.
  + No se permiten ni etiquetas ni condicionales, este modo no es Turing completo.
  + Si NO se pone ; al final de una linea se imprime el estado actual de variables
  + No es posible varias instrucciones por linea.
+ Archivo:
  + Se accede ejecutando con archivos como argumentos al main.py.
  + Turing completo y permite todas las funcionalidades de este programa.
  + Permite varios archivos, todos seran concatenados.

## Características

Todos los numeros son de tipo coma flotante.
Operaciones básicas de suma, resta, división y multiplicación.
Los operadores lógicos tienen una característica, se realizan las operaciones con las 
conversiones a entero y se vuelve a convertir a float, por lo que si solos sirven como operación floor.

Sintaxis:

```python
# Los comentarios solo son inline tipo python
# Solo se pueden tener comentarios en el principio de linea, no final
# Para asignar una expresion a una variable, 
# los datos pueden ser flotantes literales o 
# variables ya definidas.
var = ope datos...

# Imprimir un valor por pantalla
ope datos...

# Imprimir el valor de una variable por pantalla
var

# Se pueden escribir varias instrucciones en una línea separadas por ;
ope datos... ; var = ...

# Etiquetas deben de terminar en :
ETIQUETA_VALIDA:

# Salto si el valor de la variable es mayor a 0
IF var ETIQUETA_VALIDA:
IF NOT var ETIQUETA_VALIDA 
```

### Ejemplos de código

```python
# Codigo que convierte a = c ** b
a = + 1
b = + 2
c = + 9

ETI:

a = * a c
b = - b 1

IF b ETI:
a

```
```python
# Código de MCD 
a = + 15
b = + 10
true = + 1

MCD:
IF NOT b FIN

RESTO:
diff = - a b
diff = + diff 1
IF NOT diff FIN_RESTO
a = - diff 1

IF true RESTO
FIN_RESTO:

# Un swap
a = ^ a b
b = ^ a b
a = ^ a b
IF true MCD

FIN:
a

```
