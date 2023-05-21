## Problema 311: Chivas locas

En un corral dónde hay varias chivas peleoneras, un granjero ciego compró rejas para poder separar a cada una y evitar peleas, pero no está seguro
sobre la ubicación de las rejas que tiene que armar en el corral para separarlas. Las rejas sólo se pueden colocar en sentido diagonal en el corral.
Antes de poner las rejas, el granjero amarra a las chivas al suelo con cordel y estacas para que no se muevan, pero esto sólo es temporal y
obviamente no puede colocar las rejas en el lugar que ocupan las chivas. Una vez colocadas las rejas el granjero debe asegurarse que cada sección
del corral contiene sólo una chiva antes de soltarlas.

### Entrada
El archivo de entrada contiene en el primer renglón el tamaño de la matriz de M renglones y N columnas (dónde 1<=M<=10 y 1<=N<=10), en el
segundo renglón está el número X de chivas en el corral (donde 1<=X<=5) seguido de las coordenadas por renglón y columna de cada chiva
separados por un espacio. En el tercer renglón se específica el número de casos de rejas para comprobar si aíslan o no a las chivas. Cada renglón
siguiente contiene un caso que comienza con el número de rejas a colocar seguido de los pares ordenados (renglón, columna) inicial y final de cada
reja, que también están separados por un espacio.

### Salida
La salida a consola debe imprimir un SI por cada configuración exitosa y un NO por cada caso erróneo.

Ejemplo de entrada:
```
45
402132033
4
201340330
10022
3013230030033
3103230033214
```

Ejemplo de salida:
```
SI
NO
NO
SI
```
