# Importamos las librerias
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Mostramos la imagen
img = cv2.imread("Imagenes/otro.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_plot = plt.imshow(img_rgb)
plt.title("Imagen original")
plt.show()

# Cambio de tipo de matriz
ax = plt.hist(img_rgb.ravel())
plt.show()
