# Importamos la librería
import numpy as np

# Creamos una matriz de puntos
puntos = np.array([[2,0,1],
				  [3,0,2],
				  [1,1,1]])

print(puntos)

# Si deseamos hacer una traslacion

puntos_traslador = np.array([[2+2,0+2,1+2],
				  		    [3+3,0+3,2+3],
				  			[1,1,1]])


print(puntos_traslador)
# Se mueven2 unidades a lo largo de la dirección x
a=2
# Se mueve 3 unidades a lo largo de la dirección y
b=3

# Generamos una matriz de traslación
M = np.array([[1,0,a],
			  [0,1,b],
			  [0,0,1]])

matriz_trasladada = M@puntos

print(f'Los puntos trasladados utilizando la matriz de traslación son:\n {matriz_trasladada}')


