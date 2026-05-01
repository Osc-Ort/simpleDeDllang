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
# Codigo que calcula a = b ** c
a = + 1
b = + 9
c = + 2

ETI:

a = * a b
c = - c 1

IF c ETI:
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

```python
# Código calculo secuencia de fibonacchi
n = + 10
a = + 0
b = + 1

TRUE = + 1

# Caso de n == 0
IF n CONT
a
IF TRUE EXIT
CONT:
n = - n 1
# Caso de n == 1
IF n CONT2
b
IF TRUE EXIT
CONT2:

BUCLE:
# Comentar siguiente linea si no se quieren todos los números solo el resultado 
a
a = + a b
a = ^ a b
b = ^ a b
a = ^ a b

n = - n 1

IF n BUCLE
a

```

```python
# b = a!
a = + 10
b = + 1

# Caso a <= 0
IF NOT a EXIT
FACT:
b = * b a
a = - a 1

IF a FACT
EXIT:
b

```
