# Importamos las librerías
import cv2

# Seleccionamos la imagen a tratar
img = cv2.imread("Imagenes/lluvia2.jpg")
cv2.imshow("Imagen con ruido de sal y pimienta",img)

# Utilizando filtro de media para la reducción de ruido
img_filtrada_3 = cv2.medianBlur(img,3)
cv2.imshow("Imagen con filtro de ruido 3",img_filtrada_3)

img_filtrada_5 = cv2.medianBlur(img,5)
cv2.imshow("Imagen con filtro de ruido 5",img_filtrada_5)

cv2.waitKey(0)
