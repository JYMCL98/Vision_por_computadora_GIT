# Jym Emmanuel Cocotle Lara
# OpenCV descomposición en canales de imágenes
import cv2  # Agregamos la librería de OpenCV
from matplotlib import pyplot as plt  # De la libreria matplotlib importamos el complemento de pyplot y lo igualamos con plt


img = cv2.imread("Imagenes/paisaje.jpg")  # Cargamos la imagen


if img is None:  # Si no se encuentra ninguna imagen con ese nombre entonces:
    print("La imagen no se encuentra en la ruta especificada")  # se muestra un mensaje de alerta


# Mostramos la imagen
cv2.imshow("Paisaje", img)  # # Le damos nombre a la ventana de la imagen
cv2.waitKey(0)  # Esperamos hasta que una tecla sea oprimida
cv2.destroyAllWindows()  # Se destruyen todas las ventanas


# Separando los canales
blue, green, red = cv2.split(img)  # Se divide los canales de colores de la imagen y se igualan a valores
cv2.imshow("Blue", blue)  # En una ventana nueva se muestra solo el canal azul
cv2.waitKey(0)  # Esperamos hasta que una tecla sea oprimida


cv2.imshow("Green", green)  # En una ventana nueva se muestra solo el canal verde
cv2.waitKey(0)  # Esperamos hasta que una tecla sea oprimida


cv2.imshow("Red", red)  # En una ventana nueva se muestra solo el canal rojo
cv2.waitKey(0)  # Esperamos hasta que una tecla sea oprimida


# Guardamos los canales de la imagen
cv2.imwrite("Imagenes/Blue.png", blue)  # Se guarda la imagen con que solo posee el canal azul
cv2.imwrite("Imagenes/Green.png", green)  # Se guarda la imagen con que solo posee el canal verde
cv2.imwrite("Imagenes/Red.png", red)  # Se guarda la imagen con que solo posee el canal rojo


image1 = cv2.imread("Imagenes/Blue.png")  # Se lee la imagen guardada anteriormente
image2 = cv2.imread("Imagenes/Green.png")  # Se lee la imagen guardada anteriormente
image3 = cv2.imread("Imagenes/Red.png")  # Se lee la imagen guardada anteriormente


final_frame = cv2.hconcat((img, image1, image2, image3))  # En una imagen nueva ponemos la imagen original y las imagenes creadas
cv2.imwrite("Imagenes/final_image.png", final_frame)  # Guardamos la imagen final
cv2.imshow("Image and chanels", final_frame)  # # En una ventana nueva se muestra la imagen final
cv2.waitKey(0)  # Esperamos hasta que una tecla sea oprimida
