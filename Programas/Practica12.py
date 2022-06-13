# Jym Emmanuel Cocotle Lara

# Importamos la librería cv2
import cv2

# Establecemos la ruta de la imagen
ruta_imagen = "Imagenes/paisaje.jpg"
# Leemos la imagen en la ruta
img = cv2.imread(ruta_imagen)

#Seleccionamos las coordenadas de inicio y fin
inicio = (0, 0)
termina = (img.shape[1], img.shape[0])

#Establecemos el color de la línea
color = (192, 192, 192)

#Establecemos el grosor de la línea
grosor = 10

#Definimos la imagen con la línea
cv2.line(img, inicio, termina,color, grosor)

#Mostramos la imagen modificada
cv2.imshow("Imagen modificada", img)

# Esperamos cualquier tecla para cerrar el programa
cv2.waitKey(0)