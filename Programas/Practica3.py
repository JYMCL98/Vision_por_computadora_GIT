# Agregamos la libreria numpy con el comando: "pip install numpy" con el simbolo de sistema

# Estructura Array
import numpy as np # Importamos la librería numpy

x = np.array([1,4,3]) #Construimos un vector
print(x) # Imprimimos el vector tipo fila

y = np.array([[1,4,3],[9,2,7]]) # Construimos una matriz de 2 filas 3 columnas
print(y) # Imprimimos la matriz

print(y.size) # Conocemos el numero de elementos de la matriz
print(y.shape) # Conocemos el numero de filas y columnas de la matriz

z = np.arange(0,11,1) # construir un arreglo de datos desde 0 hasta 10 de uno en uno
print(z) # Visualizamos el arreglo

w = np.arange(-5,2,0.5) # Construir un arreglo de datos desde -5 hasta 2 de 0.5 en 0.5
print(w) # Visualizamos el arreglo

print(y[0,1]) # Accedemos al valor de la matiz en la fila 0 y columna 1
print(y[0,:]) # Accedemos a todos los valores de la fila 0
print(y[:,-1]) # Accedemos a los valores de la ultima columna

matriz_ceros = np.zeros((2,2)) # Construimos una matriz de 2x2 de ceros
matriz_unos = np.ones((3,3)) # Construimos una matriz de 3x3 de unos

print(matriz_ceros) # Visualizamos a la matriz de 2x2
print(matriz_unos) # Visualizamos a la matriz de 3x3