# Importamos librerías
import cv2
import numpy as np

# Visualizamos el video
video = cv2.VideoCapture(1)

# Visualizamos la camara en escala de grises
while True:
	_,frame = video.read()
	img_grises = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.imshow("background",img_grises)

	k = cv2.waitKey(5)
	if k == 27:
		break

# Volvemos a llamar a la camara
while True:
	_,frame = video.read()
	img_grises2 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	
	cv2.imshow("foreground",img_grises2)

	# Establecemos los parámetros de las diferencias
	diferencia = np.absolute(np.matrix(np.int16(img_grises))-np.matrix(np.int16(img_grises2)))
	diferencia[diferencia>255]=255
	diferencia=np.uint8(diferencia)
	cv2.imshow("Diferencia imagenes",diferencia)

	# Establecemos los limites de la diferencia
	Diff = diferencia
	Diff[Diff<=100]=0
	Diff[Diff>100]=1

	# Localización en x
	suma_columnas = np.matrix(np.sum(Diff,0)) # se suman las columnas
	# Se enumera cada uno de los elementos de la matriz
	columna_numeracion = np.matrix(np.arange(640)) # resolución de la cámara
	columna_multiplicacion = np.multiply(suma_columnas,columna_numeracion)
	total = np.sum(columna_multiplicacion)
	total_total = np.sum(np.sum(Diff))
	localizacion_columna = total/total_total
	print(f"Localizacion columna: {localizacion_columna}")

	k = cv2.waitKey(5)
	if k == 27:
		break
# Destruimos todas las ventanas
cv2.destroyAllWindows()