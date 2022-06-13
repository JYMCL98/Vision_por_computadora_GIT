#  Importamos lasw librerias
import cv2
import numpy as np
import time

# Seleccionamos la camara a utilizar
video = cv2.VideoCapture(1)

while True:
	# Visualizamos la camara
	_,frame = video.read()
	cv2.imshow("Imagen en RGB",frame)

	# Declaramos matrices para los colores
	rojo = frame[:,:,2]
	verde = frame[:,:,1]
	azul = frame[:,:,0]

	# Restamos las matrices para solo tener el color rojo
	solo_rojo = np.int16(rojo)-np.int16(verde)-np.int16(azul)
	solo_rojo[solo_rojo<0] = 0
	solo_rojo[solo_rojo>255] = 255

	# Esperamos un segundo
	time.sleep(0.1)
	# Visualizamos el video en una nueva ventana
	_,frame = video.read()

	# Declaramos las segundas matrices para los colores
	rojo2 = frame[:,:,2]
	verde2 = frame[:,:,1]
	azul2 = frame[:,:,0]

	# Restamos las matrices
	solo_rojo2 = np.int16(rojo)-np.int16(verde)-np.int16(azul)
	solo_rojo2[solo_rojo2<0] = 0
	solo_rojo2[solo_rojo2>255] = 255

	# Restamos solo los colores rojos
	movimiento = solo_rojo2-solo_rojo
	solo_rojo = np.uint8(solo_rojo)
	columna_suma = np.matrix(np.sum(solo_rojo,0))

	# Enumero cada uno de los elementos de la matriz
	columna_numeración = np.matrix(np.arange(640))  # Número de pixeles
	columna_multiplicacion = np.multiply(columna_suma,columna_numeración)
	total = np.sum(columna_multiplicacion)
	total_total = np.sum(np.sum(solo_rojo))
	columna_localizacion = total/total_total

	# imprimimos la columna de valores
	print(columna_localizacion)
	movimiento = np.uint8(movimiento)

	# Mostramos la imagen rojo y su movimiento
	cv2.imshow("Imagen",rojo)
	cv2.imshow("Movimiento",movimiento)

	k = cv2.waitKey(5)
	if k == 27:
		break

# Destruimos todas las ventanas y visualizamos las matrices
cv2.destroyAllWindows()
print(rojo)
print(solo_rojo)