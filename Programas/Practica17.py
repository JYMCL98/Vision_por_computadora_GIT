# Importamos la librería
import cv2

# Seleccionamos la ruta de la imagen
ruta_imagen = "Imagenes/paisaje.jpg"
imagen = cv2.imread(ruta_imagen)

# Parámetros de tamaño
(alto,largo) = imagen.shape[:2]
aspecto = largo/alto

# Se modifican dichos parámetros
new_alto = int(0.5*alto)
new_largo = int(alto*aspecto)

# Se modifica la imagen
dimensiones = (new_alto, new_largo)
new_tamaño = cv2.resize(imagen,dimensiones,interpolation=cv2.INTER_AREA)

# Se muestra la imagen
cv2.imshow("Imagen con tamaño modificado",new_tamaño)
new_image_factores = cv2.resize(imagen,None,fx=1.2,fy=1.2,interpolation=cv2.INTER_LANCZOS4)
cv2.imshow("Imagen con tamaño modificado con factores",new_image_factores)

cv2.waitKey()


