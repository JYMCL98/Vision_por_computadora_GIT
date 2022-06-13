# Importamos las librerías
import cv2
import numpy as np

# Seleccionamos la imagen a tratar
img = cv2.imread("Imagenes/paisaje.jpg")
cv2.imshow("Imagen original",img)
cv2.waitKey(0)

# Definimos el kernel y mostramos el resultado
kernel_3x3 = (3,3)
imagen_borrosa3x3 = cv2.blur(img,kernel_3x3)
cv2.imshow("Imagen borrossa 3x3", imagen_borrosa3x3)

kernel_5x5 = (5,5)
imagen_borrosa5x5 = cv2.blur(img,kernel_5x5)
cv2.imshow("Imagen borrossa 5x5", imagen_borrosa5x5)

kernel_7x7 = (7,7)
imagen_borrosa7x7 = cv2.blur(img,kernel_7x7)
cv2.imshow("Imagen borrossa 7x7", imagen_borrosa7x7)

cv2.waitKey(0)

