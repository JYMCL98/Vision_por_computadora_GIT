# Importamos las librerías
import cv2
import numpy as np

# Seleccionamos la ruta de la imagen
ruta_imagen = 'Imagenes/colibri.jpg'
imagen = cv2.imread(ruta_imagen)

# Alto y ancho
(h,w) = imagen.shape[:2]

# Definimos la rotacion
centro = (h//2,w//2)
angulo = -20
scala = 1.0

matriz_rotacion = cv2.getRotationMatrix2D(centro,angulo,scala)
print(matriz_rotacion)

# Rotamos la imagen y la mostramos
imagen_rotada = cv2.warpAffine(imagen,matriz_rotacion,(w,h))
cv2.imshow("Imagen rotada", imagen_rotada)
cv2.waitKey(0)
