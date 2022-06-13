# Jym Emmanuel Cocotle Lara
# OpenCV propiedades de imágenes
import cv2  # Agregamos la librería de OpenCV


image_path = "Imagenes/paisaje.jpg"  # Agregamos la ruta de la imagen


# Leemos y cargamos la imagen de la ruta indicada
image = cv2.imread(image_path)  # Leemos la imagen 


# Imprimimos las propiedades de la imagen
print("Las dimensiones de la imagen son: ", image.ndim)  # Visualizamos el numero de dimensiones de la imagen
print("El largo de la imagen: ", image.shape[0])  # Visualizamos el valor de pixeles del largo de la imagen
print("El ancho de la imagen: ", image.shape[1])  # Visualizamos el valor de pixeles del ancho de la imagen
print("Los canales de la imagen son: ", image.shape[2])  # Visualizamos el numero de canales de la imagen
print("El tamaño de la imagen: ", image.size)  # Visualizamos el tamaño de la imagen

# Mostramos la imagen
cv2.imshow("Paisaje", image)  # Le damos nombre a la ventana de la imagen
cv2.waitKey(0)  # Esperamos hasta que una tecla sea oprimida
