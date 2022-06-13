# Importamos las librerias
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Seleccionamos las rutas de las imagenes
rut_img = "Imagenes/cebra.jpg"
imagen = cv2.imread(rut_img)

# Convertimos la imagen en blanco y negro
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
plt.imshow(imagen)
plt.show()
plt.imshow(imagen, cmap='gray')
plt.show()


# Establecer el umbral y el valor maximo
umbral = 150
val_max = 255


# Umbral binario
th, dst = cv2.threshold(imagen, umbral, val_max, cv2.THRESH_BINARY)
plt.imshow(dst, cmap="gray")
plt.show()


print(dst)





