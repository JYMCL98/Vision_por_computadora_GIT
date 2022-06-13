# Importamos las librerias
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Seleccionamos la imagen a tratar
img = cv2.imread("Imagenes/luz.jpg",0)
cv2.imshow("Imagen original",img)

# Obtenemos el histograma
ax=plt.hist(img.ravel(), bins=256)
plt.title("Imagen original")
plt.show()

# Declaramos y hacemos uso del algoritmo CLAHE
alg_clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize = (8,8))
img_clahe = alg_clahe.apply(img)

# Mostramos las imagenes
cv2.imshow("Imagen CLAHE",img_clahe)
ax = plt.hist(img_clahe.ravel(), bins=256)
plt.title("Imagen despues del CLAHE")
plt.show()