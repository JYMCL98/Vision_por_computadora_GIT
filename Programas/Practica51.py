# Imprtamos las librerias
import cv2
import numpy as np
import imutils
import os

# Ejecutamos la camara
video = cv2.VideoCapture(0)

while True:
    # Mostramos el video
    _,frame = video.read()
    cv2.imshow("Imagen en rgb",frame)
    # Repetimos los frame para cada color
    rojo = frame[:,:,2]
    verde = frame[:,:,1]
    azul = frame[:,:,0]
    
    # Mostramos los colores cada uno en una ventana
    cv2.imshow("Rojo: ",rojo)
    cv2.imshow("Verde: ",verde)
    cv2.imshow("Azul: ",azul)


    k= cv2.waitKey(5)
    if k ==27:
        break

# Destruimos todas las ventanas y visualizamos las matrices
cv2.destroyAllWindows()
print(rojo)
print(verde)
print(azul)