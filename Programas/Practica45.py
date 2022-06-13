# Importamos las librerías
import cv2

# Cargamos la imagen a utilizar
img = cv2.imread("Imagenes/fruit2.jpg")
cv2.imshow("Imagen original",img)

# Pasamos la imagen a escala de grises
img_grises = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Imagen en escala de grises",img_grises)

# Binarizamos la imagen
ret,img_binarizada = cv2.threshold(img_grises,170,255,cv2.THRESH_BINARY)
cv2.imshow("Imagen binarizada",img_binarizada)

# Hacemnos la binarización inversa
img_binarizada_inv = ~img_binarizada
cv2.imshow("Imagen binarizada inversa",img_binarizada_inv)

# Identificamos y dibujamos los contornos
contornos,jeraquia = cv2.findContours(img_binarizada_inv,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
img_con_contornos = cv2.drawContours(img,contornos,-1,(0,0,255),3)
cv2.imshow("Imagen con contornos",img_con_contornos)

cv2.waitKey(0)
