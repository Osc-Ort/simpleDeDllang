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

## Características

Operaciones básicas de suma, resta, división y multiplicación.

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

# Salto si el valor de la variable es distinta de 0
IF var ETIQUETA_VALIDA:
# Solo se puede volver para atras en las etiquetas, no avanzar
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