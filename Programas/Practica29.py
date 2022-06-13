# Importamos las librerias
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Seleccionamos la ruta de la imagen
img = cv2.imread("Imagenes/CD1.png")

# Pasamos a escala de grises la imagen
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Mostramos la imagen
plt.imshow(img, cmap = "gray")
plt.show()

# Establecemos los valores de umbral y valor máximo
umbral = 150
val_max = 255

# Binarización
th, dst = cv2.threshold(img, umbral, val_max, cv2.THRESH_BINARY)
plt.imshow(dst, cmap="gray")
plt.show()

# Definimos la imagen de fondo
img_bg = cv2.imread("Imagenes/colibri.jpg")
img_bg = cv2.cvtColor(img_bg, cv2.COLOR_BGR2GRAY)
print(img_bg.shape)
print(dst.shape)

# Redimensionamos las imagenes
img = cv2.resize(img,(450,300), interpolation = cv2.INTER_LINEAR)
img_bg = cv2.resize(img_bg, (450,300), interpolation = cv2.INTER_LINEAR)
print(img_bg.shape)
print(img.shape)

# Motramos el resultado
resul = np.where(img, img_bg, 0)
plt.imshow (resul, cmap = 'gray')
plt.show()

# Juntamos las imagenes
final_img = cv2.hconcat((img, img_bg, resul))
cv2.imshow("Imagenes usadas", final_img)
cv2.waitKey(0)
