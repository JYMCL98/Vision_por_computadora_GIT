# Jym Emmanuel Cocotle Lara
# OpenCV generación de imágenes
import cv2  # Agregamos la librería de OpenCV
import numpy # Agregamos la librería de numpy
import os  # Agregamos la librería de os


# Generamos un array con 120,000 bytes random
random_byte_array = bytearray(os.urandom(120000))


# Asignamos los valores aleatorios a un array
flat_numpy_array = numpy.array(random_byte_array)


# Convertir los bytes a imagen 400X300, 300X400 etc...
imagen_escala_grises = flat_numpy_array.reshape(300, 400)  # Reasignamos los bytes para crear una imagen en escala de grises
cv2.imwrite("Imagen_random_escala_grises.jpg", imagen_escala_grises)  # Guardamos la imagen en escala de grises


#Escribimos la imagen con color
imagen_rgb = flat_numpy_array.reshape(100, 400, 3)  # Reasignamos los bytes para crear una imagen con escala rgb
cv2.imwrite("Imagen_random_rgb.jpg", imagen_rgb)  # Guardamos la imagen con escala rgb


cv2.imshow("Imagen random en escala de grises", imagen_escala_grises)  # Mostramos la imagen en escala de grises
cv2.waitKey(0)  # Esperamos hasta que una tecla sea oprimida


cv2.imshow("Imagen random en escala RGB", imagen_rgb)  # Mostramos la imagen en escala rgb
cv2.waitKey(0)  # Esperamos hasta que una tecla sea oprimida
