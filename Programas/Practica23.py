# Importamos las librerias
import cv2
import numpy as np
import matplotlib.pyplot as plt


# Cagamos la imagen
imagen = cv2.imread("Imagenes/paisaje.jpg")


#Mostramos la imagen
plt.imshow(imagen[:,:,::-1])
plt.show()


# Sumando 100 a la imagen
suma_imagen = imagen+100


# Mostramos la imagen
plt.imshow(suma_imagen[:,:,::-1])
plt.show()


# Utilizando OpenCV
suma_opencv = cv2.add(imagen, 100)


# Mostramos la imagen
plt.imshow(suma_opencv[:,:,::-1])
plt.show()


print(imagen.shape)


matriz_arreglo = np.ones((450, 300, 3), dtype = np.uint8)*100


suma_opencv2 = cv2.add(imagen, matriz_arreglo)


# Mostramos la imagen
plt.imshow(suma_opencv2[:, :, ::-1])
plt.show()

