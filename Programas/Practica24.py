# importamos las librerias
import cv2
import numpy as np

# Ruta de imagen
ruta_imagen1 = "Imagenes/paisaje.jpg"
ruta_imagen2 = "Imagenes/colibri.jpg"

# Cargamos las imagenes
imagen1 = cv2.imread(ruta_imagen1)
imagen2 = cv2.imread(ruta_imagen2)

# Redimensionamiento de imagenes
imagen1_redimensionada = cv2.resize(imagen1, (300,300),interpolation = cv2.INTER_AREA)
imagen2_redimensionada = cv2.resize(imagen2, (300,300),interpolation = cv2.INTER_AREA)

# Suma de las dos imagenes
operacion_suma = cv2.add(imagen1_redimensionada, imagen2_redimensionada)

# Mostramos las imagenes
cv2.imshow("Imagen 1 redimensionada", imagen1_redimensionada)
cv2.waitKey()

cv2.imshow("Imagen 2 redimensionada", imagen2_redimensionada)
cv2.waitKey()

cv2.imshow("Resultado de la operación", operacion_suma)
cv2.waitKey(0)

imagen_con_pesos = cv2.addWeighted(imagen1_redimensionada, 0.4, imagen2_redimensionada, 0.6, 0)
cv2.imshow("Imagen sumada con pesos", imagen_con_pesos)
cv2.waitKey(0)

imagen_mejorada = 255*imagen2_redimensionada
cv2.imshow("Imagen mejorada", imagen_mejorada)
cv2.waitKey(0)


imagen_array = imagen1_redimensionada + imagen2_redimensionada
cv2.imshow("Array de la suma de dos imagenes", imagen_array)
cv2.waitKey(0)

