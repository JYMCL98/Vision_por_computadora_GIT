# Importamos las librerias
import cv2
import matplotlib.pyplot as plt

# Seleccionamos la imagen a tratar y la ponemos en escala de grises
img = cv2.imread("Imagenes/otro.jpg", cv2.IMREAD_GRAYSCALE)

# Mostramos la imagen
cv2.imshow("Imagen en escala de grises", img)
cv2.waitKey(0)

# Cambiamos de una matriz bidimensional a una planar
ax = plt.hist(img.ravel(), bins=256)
plt.show()


