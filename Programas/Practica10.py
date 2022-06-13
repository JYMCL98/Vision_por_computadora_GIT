# Jym Emmanuel Cocotle Lara
# OpenCV modificación de pixeles
import cv2  # Agregamos la librería de OpenCV


# Escribimos la ruta de la imagen
ruta_imagen = "Imagenes/paisaje.jpg"


# Cargamos la imagen
image = cv2.imread(ruta_imagen)


# Accesamos al pixel localicado en la ubicacion (0,0)
(b, g, r) = image[0, 0]
print("Valores azul, verde, rojo del pixel en (0,0)", format((b, g, r)))  # Visualizamos los valores del pixel 0,0


# Manipulamos el pixel de color salmon
image[0:100, 0:100] = (114, 128, 250)  # Se asigna un nuevo valor a los pixeles en x de 0 hasta 100 al igual que en y


# Mostramos la imagen modificada
cv2.imshow("Imagen modificada", image)
cv2.waitKey(0)  # Esperamos hasta que una tecla sea oprimida
