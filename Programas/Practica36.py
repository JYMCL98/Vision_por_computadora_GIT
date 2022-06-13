# Importamos las librerías
import cv2
import numpy as np

# Seleccionamos la imagen a tratar
img = cv2.imread("Imagenes/otro.jpg")
cv2.imshow("Imagen original",img)

# Aplicamos el filtro de Gauss y mostramos el resultado
filtro_gaussiano = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow("Imagen con filtro gaussiano",filtro_gaussiano)

cv2.waitKey(0)
