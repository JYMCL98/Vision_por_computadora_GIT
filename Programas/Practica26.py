# Importamos las librerias
import cv2
import numpy as np

# Seleccionamos las rutas de las imagenes
ruta_imagen1 = "Imagenes/paisaje.jpg"
ruta_imagen2 = "Imagenes/etc.jpg"
imagen1 = cv2.imread(ruta_imagen1)
imagen2 = cv2.imread(ruta_imagen2)

# Redimensionamiento de la imagen
imagen1_red = cv2.resize(imagen1, (300,300),interpolation = cv2.INTER_AREA)
imagen2_red = cv2.resize(imagen2, (300,300),interpolation = cv2.INTER_AREA)

# Mostramos las imagenes redimensionadas
cv2.imshow("Imagen 1 redimensionada", imagen1_red)
cv2.imshow("Imagen 2 redimensionada", imagen2_red)

# Se muestra el resultado de la multiplicación de las dos imagenes
multi_img = cv2.multiply(imagen1_red, imagen2_red)
cv2.imshow("Multiplicación de dos imagenes", multi_img)
cv2.waitKey(0)

# Se multiplica una imagen por un escalar
mul_im_esc = cv2.multiply(imagen1_red, 3)
cv2.imshow("Multiplicación de una imagen por un escalar", mul_im_esc)
cv2.waitKey(0)
