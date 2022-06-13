# Importamos las librerias
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Seleccionamos la imagen a tratar
img = cv2.imread("Imagenes/colibri.jpg",0)

# Mostramos la imagen
cv2.imshow("Imagen original",img)
cv2.waitKey(0)

# Obtenemos el histograma
ax = plt.hist(img.ravel(), bins=256)
plt.title("Histograma de la imagen original")
plt.show()

# Ecualizamos a la imagen
hist_equ = cv2.equalizeHist(img)
cv2.imshow("Imagen equializada", hist_equ)
cv2.waitKey(0)

# Ecualizamos al histograma
ax = plt.hist(hist_equ.ravel(), bins=256)
plt.title("Histograma ecualizado")
plt.show()

# Comparamos las imagenes obtenidas
img_con_equ = np.hstack((img, hist_equ))
cv2.imshow("Comparación de imagenes", img_con_equ)
cv2.waitKey(0)