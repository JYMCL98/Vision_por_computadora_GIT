# Importamos la librería
import cv2

# Seleccionamos la imagen
ruta_imagen = "Imagenes/paisaje.jpg"
imagen = cv2.imread(ruta_imagen)

# Establecemos los parámetros
inicia = (50,70)
termina = (200,300)
color = (59,255,250)
grosor = 5

# Dibujamos el rectángulo
cv2.rectangle(imagen,inicia,termina,color,grosor)
cv2.imwrite("Imagenes/paisaje_rectangle.jpg",imagen)
cv2.imshow("Imagen con rectangulo",imagen)
cv2.waitKey(0)

