# Jym Emmanuel Cocotle Lara

# Importamos la librería cv2
import cv2
# Importamos la librería numpy como np
import numpy as np


#Creamos una nueva imagen
imagen = np.zeros((200, 200, 3), dtype="uint8")

# Establecemos los valores para el rectángulo
inicia = (10, 10)
termina = (100, 100)
color = (15,30,155)
grosor = 5

# Creamos la imagen con el rectángulo
cv2.rectangle(imagen,inicia, termina, color, grosor)
# Creamos una nueva imagen que muestre la imagen original con el rectángulo
cv2.imwrite("Imagenes/Imagen_con_rectangulo.jpg", imagen)
# Mostramos la imagen con el rectángulo
cv2.imshow("Imagen con rectangulo", imagen)
# Esperamos cualquier tecla para cerrar el programa
cv2.waitKey()

