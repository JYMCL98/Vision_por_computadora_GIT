# Importamos las librerías
import cv2
import numpy as np

# Cargamos la imagen
img = cv2.imread("Imagenes/letras2.jpg")

# Convertimos la imagen a escala de grises
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Imagen original",img)

# Binarizamos por umbral adaptativo
img_binarizada = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,7,3)
cv2.imshow("Imagen binarizada con una media simple",img_binarizada)

# Binarizamos la imagen utilizando una media Gaussiana
img_binarizada_2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,13)
cv2.imshow("Imagen binarizada con una media Gaussiana", img_binarizada_2)

cv2.waitKey(0)
