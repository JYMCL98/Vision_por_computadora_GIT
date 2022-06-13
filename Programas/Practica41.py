# Importamos las librerías
import cv2
import numpy as np

# Cargamos la imagen a utilizar
img = cv2.imread("Imagenes/paisaje.jpg")

# Convertimos la imagen a escala de grises
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Imagen original",img)

# Binarización de la imagen
(T, img_binarizada) = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("Imagen utilizando binarización OTSU", img_binarizada)

# Binarización inversa de la imagen
(Ti, img_binarizada_inversa) = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
cv2.imshow("Imagen inversa utilizando binarización OTSU",img_binarizada_inversa)

cv2.waitKey(0)
