# Importamos las librerías
import cv2

# Seleccionamos la imagen a tratar
img = cv2.imread("Imagenes/lluvia2.jpg")
cv2.imshow("Imagen original", img)

# Filtro bilateral
img_filtro_5 = cv2.bilateralFilter(img,5,150,50)
cv2.imshow("Imagen con filtro bilateral 5",img_filtro_5)

img_filtro_7 = cv2.bilateralFilter(img,7,160,60)
cv2.imshow("Imagen con filtro bilateral 7",img_filtro_7)

cv2.waitKey(0)

