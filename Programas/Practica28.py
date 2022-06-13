# Importamos las librerias
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Seleccionamos la ruta de las imaenes
imagen1 = cv2.imread("Imagenes/chess1.jpg")
imagen2 = cv2.imread("Imagenes/chess2.jpg")

# Pasamos a escala de grises las imagenes
imagen1 = cv2.cvtColor(imagen1, cv2.COLOR_BGR2GRAY)
imagen2 = cv2.cvtColor(imagen2, cv2.COLOR_BGR2GRAY)


plt.imshow(imagen1, cmap="gray")
plt.show()
plt.imshow(imagen2, cmap="gray")
plt.show()

# Establecemos el umbral y el valor máximo
umbral = 150
val_max = 255

# Binarización
th, dst1 = cv2.threshold(imagen1, umbral, val_max, cv2.THRESH_BINARY)
th, dst2 = cv2.threshold(imagen2, umbral, val_max, cv2.THRESH_BINARY)


plt.imshow(dst1, cmap = "gray",)
plt.show()
plt.imshow(dst2, cmap = "gray")
plt.show()

# Se calcula el XOR
dst_xor = cv2.bitwise_xor(dst1,dst2)
plt.imshow(dst_xor, cmap="gray")
plt.show()

# Se calcula el AND
dst_and = cv2.bitwise_and(dst1,dst2)
plt.imshow(dst_and, cmap = "gray")
plt.show()

# SE calcula el OR
dst_or = cv2.bitwise_or(dst1,dst2)
plt.imshow(dst_or, cmap = "gray")
plt.show()

# Se calcula el NOT
dst_not = cv2.bitwise_not(dst1,dst2)
plt.imshow(dst_not, cmap = "gray")
plt.show()
