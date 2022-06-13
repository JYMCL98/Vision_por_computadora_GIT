# Cascada y reconocimiento facial
import cv2
import numpy as np

# seleccionamos la imagen
img = cv2.imread("Imagenes/personas.jpg")

# Seleccionamos el clasificador
ruta_clasif = "data/haarcascade_frontalface_alt.xml"

# Pasamos la imagen a escala de grises
img_grises = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
clasif = cv2.CascadeClassifier(ruta_clasif)

# Detectamos los rostros en la imagen
rostros_detectados = clasif.detectMultiScale(img_grises,1.2,1)

# Dibujamos un rectángulo alrededor de los rostros
for rostro in rostros_detectados:
	x,y,w,h = rostro
	cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

# Mostramos el resultado
cv2.imshow("Rostro en una imagen",img)

cv2.waitKey(0)
