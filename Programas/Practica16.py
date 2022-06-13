# Importamos la librería
import cv2 as cv
import numpy as np
import time

# Seleccionamos la camara
video_cap = cv.VideoCapture(0)




# Condicional en el caso de que la camara no se abra
if not video_cap.isOpened():
	print("No se puede abrir la camara")
	exit()

# Bucle de la camara
while True:
    # Captura trama a trama
    ret,frame = video_cap.read()
    #   qqcv.resizeWindow("camera", 80, 80)
    
    #time.sleep(1)
    #print(frame)
    time.sleep(0.300)
    #fotograma = frame
    
    
    
    if not ret:
        print("No se puede recibir el frame, el video ha termindao")
        break
    
    # Escala de grises
    escala_grises = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    fotog = cv.resize(escala_grises, (80,80))
    print(fotog)
    cv.imshow("camera",escala_grises)
    if cv.waitKey(1)==ord('q'):
        break

    

video_cap.release()
cv.destroyAllWindows()
