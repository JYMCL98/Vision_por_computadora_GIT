# Importamos las librerias
import cv2
import numpy as np

# Seleccionamos la ruta de la imagen
ruta_imagen = "Imagenes/paisaje.jpg"
image = cv2.imread(ruta_imagen)

# Cambiar su orientación horizontalmente
orientacion_horizontal = cv2.flip(image, 1)
cv2.imshow("Orientación horizontal", orientacion_horizontal)
cv2.waitKey(0)

# Cambiar su orientación vertical
orientacion_vertical = cv2.flip(image, 0)
cv2.imshow("Orientación vertical", orientacion_vertical)
cv2.waitKey(0)

# Cambiar la orientación horizontal y vertical
orientacion_hv = cv2.flip(image, -1)
cv2.imshow("Orientacion horizontal y vertical", orientacion_hv)
cv2.waitKey(0)


