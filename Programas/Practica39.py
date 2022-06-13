# Importamos las librerías
import cv2
import numpy as np

# Cargamos la imagen
img = cv2.imread("Imagenes/letras.jpg")

# Convertimos en escala de grises a la imagen
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Imagen original", img)

# Binarizamos la imagen usando un umbral
(T, img_binarizada) =  cv2.threshold(img,60,255,cv2.THRESH_BINARY)
cv2.imshow("Imagen binarizada", img_binarizada)

# Binarización utilizando colores inversos
(Ti, img_binarizada_inv) = cv2.threshold(img,130,255,cv2.THRESH_BINARY_INV)
cv2.imshow("Imagen binarizada inversa", img_binarizada_inv)

cv2.waitKey(0)
