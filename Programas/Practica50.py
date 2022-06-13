# Importamos las librerías
from __future__ import division
import cv2
import numpy as np


def nothing(*ang):
	pass

# Valores iniciales de los colores
colores = (30,20,50,255,255,255)  # Verde

cv2.namedWindow('Prueba_color')

# Declaramos los valores minimos de los trackbars
cv2.createTrackbar('lowHue','Prueba_color',colores[0],255,nothing)
cv2.createTrackbar('lowSat','Prueba_color',colores[1],255,nothing)
cv2.createTrackbar('lowVal','Prueba_color',colores[2],255,nothing)

# Declaramos los valores máximos de los trackbars
cv2.createTrackbar('highHue','Prueba_color',colores[3],255,nothing)
cv2.createTrackbar('highSat','Prueba_color',colores[4],255,nothing)
cv2.createTrackbar('highVal','Prueba_color',colores[5],255,nothing)

img = cv2.imread('D:/Downloads/PM.jpeg')

while True:
	# Extraigo los valores de las trackbars
	lowHue = cv2.getTrackbarPos('lowHue','Prueba_color')
	lowSat = cv2.getTrackbarPos('lowSat','Prueba_color')
	lowVal = cv2.getTrackbarPos('lowVal','Prueba_color')

	highHue = cv2.getTrackbarPos('highHue','Prueba_color')
	highSat = cv2.getTrackbarPos('highSat','Prueba_color')
	highVal = cv2.getTrackbarPos('highVal','Prueba_color')

	cv2.imshow("Prueba colores",img)

	# Metodos de filtrado para el mejoramiento de imagenes
	imgBGR = cv2.GaussianBlur(img,(7,7),0)
	kernel_1 = np.ones((15,15),np.float32)/255
	imgBGR = cv2.filter2D(imgBGR,-1,kernel_1)

	#cv2.imshow("Imagen con mejoramiento",imgBGR)

	#cv2.imshow("Imagen con mejoramiento",imgBGR)

	# HSV (Hue, Saturation, Value)
	hsv= cv2.cvtColor(imgBGR, cv2.COLOR_BGR2HSV)

	# Definimos los valores máximos y mínimos de HSV
	color_low = np.array([lowHue,lowSat,lowVal])
	color_high = np.array([highHue,highSat,highVal])

	mascara = cv2.inRange(hsv,color_low,color_high)

	cv2.imshow("Imagen con mascara HSV",mascara)

	# Realizamos una transformación morfologica
	kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))
	mascara = cv2.morphologyEx(mascara,cv2.MORPH_CLOSE,kernel)
	mascara = cv2.morphologyEx(mascara,cv2.MORPH_OPEN,kernel)

	cv2.imshow("Imagen con transformación",mascara)

	# Ponemos la mascara a la imagen original
	resultado = cv2.bitwise_and(img,img,mask=mascara)
	cv2.imshow('Prueba color', resultado)
	k = cv2.waitKey(5) & 0xFF
	
	if k==27:
		break
