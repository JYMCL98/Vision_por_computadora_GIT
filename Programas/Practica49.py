#Importamos librerias
import cv2
import numpy as np

#Seleccionamos la imagen
imagen=cv2.imread("Imagenes/group1.jpg")

#Seleccionamos la ruta del clasificador de ojos
rutClas="data/haarcascade_eye.xml"

#Pasamos a escala de grises la imagen
imgGris=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

#Definimos el clasificador
clas=cv2.CascadeClassifier(rutClas)
rostros=clas.detectMultiScale(imgGris,1.2,1)

#Dibujamos rectangulos en los ojos que se detecten
for rostro in rostros:
	x,y,w,h=rostro
	cv2.rectangle(imagen,(x,y),(x+w,y+h),(0,0,255),3)

#Mostramos el resultado
cv2.imshow("Detección de ojos",imagen)
cv2.waitKey(0)