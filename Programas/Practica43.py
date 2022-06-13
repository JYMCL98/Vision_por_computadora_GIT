# Importamos las librerías
import cv2

# Cargamos la imagen a utilizar
img = cv2.imread("Imagenes/cubos.jpg")
img_grises = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Imagen en escala de grises",img_grises)

# Binarizamos la imagen utilizando el algoritmo OTSU
(T, img_binarizada) = cv2.threshold(img_grises,0,255,cv2.THRESH_OTSU)
cv2.imshow("Imagen binarizada con algoritmo OTSU",img_binarizada)

# Binarización inversa de la imagen
img_binarizada_inv = ~img_binarizada
cv2.imshow("Imagen binarizada inversa con el algoritmo OTSU",img_binarizada_inv)

# Ubicamos los contornos
contornos, jerarquias= cv2.findContours(img_binarizada_inv,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# Combinamos las imagenes
img_bgr = cv2.merge([img_binarizada_inv,img_binarizada_inv,img_binarizada_inv])

# mostramos los contornos
img_con_contornos = cv2.drawContours(img_bgr,contornos,-1,(255,0,0),-2)
cv2.imshow("Contornos detectados",img_con_contornos)

cv2.waitKey(0)

