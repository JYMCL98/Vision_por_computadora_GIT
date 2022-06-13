# Importamos las librerias
import cv2
import numpy as np

# Seleccionamos la ruta de la imagen
ruta_imagen = "Imagenes/otro.jpg"
imagen = cv2.imread(ruta_imagen)

#Definimos la matriz de traslación
matriz_traslacion = np.float32([[1,0,5],
								[0,1,20]])

print(matriz_traslacion)

# Trasladamos a la imagen
imagen_trasladada = cv2.warpAffine(imagen,matriz_traslacion,(imagen.shape[1],imagen.shape[0]))

cv2.imshow("Imagen trasladada", imagen_trasladada)
cv2.waitKey(0)

