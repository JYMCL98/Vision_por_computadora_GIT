# Importamos las librerías
import cv2
import numpy as np

# Cargamos la imagen a utilizar
img = cv2.imread("Imagenes/ball.jpg")
img_cop = img.copy()
cv2.imshow("Imagen original",img)

#(Blue, Green, Red)
blanco_bajo = np.array([41,49,41])
blanco_alto = np.array([235,241,248])

# Definimos la mascara
img_masc = cv2.inRange(img,blanco_bajo,blanco_alto)
cv2.imshow("Objeto de blanco",img_masc)

# Pasamos la imagen a escala de grises
img_esc_grises = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Imagen en escala de grises",img_esc_grises)

# Binarizamos la imagen
ret,img_binarizada = cv2.threshold(img_esc_grises,120,255,cv2.THRESH_BINARY)
cv2.imshow("Imagen binarizada",img_binarizada)

# Ubicamos los contornos
contornos, jerarquias = cv2.findContours(img_binarizada,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contornos_fig = -1
color_figura = (0,255,0)
grosor = -1

# Definimos a la imagen con contornos
img_con_contornos = cv2.drawContours(img,contornos,contornos_fig,color_figura,thickness=grosor)
cv2.imshow("Imagen con contornos",img_con_contornos)

for contador in contornos:
	x,y,w,h = cv2.boundingRect(contador)
	img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)

cv2.imshow("Objeto",img)

# Dibujamos le contorno dependiendo del tamaño de su área
contorno_requerido = max(contornos,key = cv2.contourArea)
x,y,w,h = cv2.boundingRect(contorno_requerido)
img_cop = cv2.rectangle(img_cop,(x,y),(x+w,y+h),(0,255,255),2)
cv2.imshow("Imagen con contorno", img_cop)

cv2.waitKey(0)
