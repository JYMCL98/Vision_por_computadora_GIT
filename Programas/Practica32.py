# importamos las librerias
import cv2
import numpy as np
import matplotlib as plt

# Selecionamos la imagen a tratar
img = cv2.imread("Imagenes/colibri.jpg")

# Mostramos una ventana de selección
x,y,w,h = cv2.selectROI(img,fromCenter=0)

# Aplicamos mascara
masc = np.zeros(img.shape[:2],dtype='uint8')
masc[int(y):int(y+h), int(x):int(x+w)]=255

# Mostramos la mascara creada
cv2.imshow("Mascara creada",masc)
cv2.waitKey(0)

cv2.imwrite("Imagen_mascara.jpg",masc)


