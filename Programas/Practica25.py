# Importamos las librerias
import cv2
import numpy as np

# Seleccionamos las rutas de las imagenes
ruta_imagen1 = "Imagenes/paisaje.jpg"
ruta_imagen2 = "Imagenes/etc.jpg"

imagen1 = cv2.imread(ruta_imagen1)
imagen2 = cv2.imread(ruta_imagen2)

# Redimensionamiento de la imagen
imagen_redimensionada1 = cv2.resize(imagen1, (int(500*imagen1.shape[1]/imagen1.shape[0]), 500))
imagen_redimensionada2 = cv2.resize(imagen2, (int(500*imagen2.shape[1]/imagen2.shape[0]), 500))
cv2.imshow("Imagen 1", imagen_redimensionada1)
cv2.imshow("Imagen 2", imagen_redimensionada2)

# Resta de dos imagenes
cv2.imshow("Resta de dos imagenes", cv2.subtract(imagen_redimensionada2, imagen_redimensionada1))
cv2.waitKey(0)
cv2.imshow("Resta de dos imagenes 2", cv2.subtract(imagen_redimensionada1, imagen_redimensionada2))
cv2.waitKey(0)

# Resta de dos imagenes con matrices
resta_imagen = imagen_redimensionada2 - imagen_redimensionada1
cv2.imshow("Resta matricial de dos imagenes", resta_imagen)
cv2.waitKey(0)

# Resta de una imagen y constante
resta_imagen2 = imagen_redimensionada1 - 50
cv2.imshow("Resta de una imagen con una constante", resta_imagen2)
cv2.waitKey(0)
