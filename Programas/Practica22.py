# Importamos librerias
import cv2
import numpy as np


#Cargar imagen
ruta_imagen = "Imagenes/colibri.jpg"
imagen = cv2.imread(ruta_imagen)
cv2.waitKey(0)


# Recortar la imagen para solo mostrar al colibri
imagen_recortada = imagen[40:170, 25:300]
cv2.imshow("Imagen recortada", imagen_recortada)
cv2.waitKey(0)
