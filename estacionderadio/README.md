## Problema 407: Estación de radio
Una estación de radio desea clasificar automáticamente las canciones que emite, las canciones
están en una lista de y hay que colocarlas en grupos de dos tratando de formar parejas de
canciones que queden lo más cerca posible de los 3 minutos de reproducción continua, siempre
se comlenza con la canción A para buscar pares de canciones a fin de obtener otra lista para 6
usarla en el programa de radio.

La entrada inicia con un valor n U que representa la cantidad de canciones a ordenar, en los n
renglones siguientes están las canciones empezando con una letra y el tiempo de reproducción en
el formato de minutos:segundos.

La salida debe mostrar en un solo renglón el orden de reproducción de las canciones formados
por parejas de letras separadas por una coma.

Ejemplo de entrada:
```
14
A1:38
B1:50
C1:52
D1:03
E1:09
F1:07
G 1:32
H1:29
11:50
J1:36
K1:42
L1:25
M144
N1:59
```

Ejemplo de salida:
```
AL,BE,CE,DI,GH,JK,MN
```