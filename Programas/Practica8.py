# Jym Emmanuel Cocotle Lara
# OpenCV escala de grises
import cv2  # Agregamos la librería de OpenCV


# Leemos la imagen desde el directorio
imagen_escala_grises = cv2.imread("Imagenes/paisaje.jpg", cv2.IMREAD_GRAYSCALE)


# Creamos la imagen en escala de grises en el directorio
cv2.imwrite("Imagenes/paisaje_gray.jpg", imagen_escala_grises)


# Mostramos la imagen en escala de grises
cv2.imshow("imagen en escala de grises", imagen_escala_grises)
cv2.waitKey(0)  # Esperamos hasta que una tecla sea oprimida
