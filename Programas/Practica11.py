# Jym Emmanuel Cocotle Lara

# Importamos las librerías necesarias
import cv2
import matplotlib.pyplot as plt
import numpy as np


# Cargamos la imagen
img = cv2.imread("Imagenes/paisaje.jpg")


# Mostramos la escala de la imagen
plt.imshow(img[:, :, ::-1])
plt.show()


print(img.shape)


# Creamos un array con el doble de minesiones de la imagen
imgNew = np.zeros((900, 300, 3), dtype=np.uint8)


# Mostramos la imagen que se acaba de crear
plt.imshow(imgNew[:, :, ::-1])
plt.show()


# Copiamos la imagen original
imgNew[:450][:] = img

# Mostramos la imagen que acabmos de crear
plt.imshow(imgNew[:, :, ::-1])
plt.show()


# Invertimos la imagen original
img_inverted = img[::-1, :, :]


# Mostramos la imagen invertida
plt.imshow(img_inverted[:, :, ::-1])
plt.show()


# Agregamos la imagen invertida
imgNew[450:][:] = img_inverted


# Mostramos la imagen final
plt.imshow(imgNew[:, :, ::-1])
plt.show()

# Guardamos la imagen
cv2.imwrite("Imagenes/Efecto_agua.jpg", imgNew)
