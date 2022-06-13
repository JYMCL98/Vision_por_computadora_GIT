# Jym Emmanuel Cocotle Lara

# Importamos la librería cv2
import cv2
# Importamos la librería numpy como np
import numpy as np

# Creamos una matriz de ceros
matriz_zeros = np.zeros((200, 200, 3),dtype="uint8")

# Establecemos los parámetros del círculo
centro = (100,100)
radio = 50
color = (250,20,250)
grosor = 5

# Creamos la imagen con un círculo
cv2.circle(matriz_zeros,centro,radio,color,grosor)
cv2.imwrite("Imagenes/imagen_circulo.jpg",matriz_zeros)
cv2.imshow("imagen_circulo",matriz_zeros)
cv2.waitKey(0)

