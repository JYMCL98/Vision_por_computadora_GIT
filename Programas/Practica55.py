# Importamos las librerías
import cv2
import numpy as np

# Seleccionamos la camara
video=cv2.VideoCapture(1)
RecursionError# Establecemos la relación entre cm y pixel
ancho = 640 #x
alto = 480 #y

cm_por_pixel_x = 19/ancho
cm_por_pixel_y = 14/alto


while True:
    # Visualizamos la camara en escala de grises
    _,frame=video.read()
    imagen_grises = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Background",imagen_grises)

    k=cv2.waitKey(5)
    if k==27:
        break

while True:
    # Viasualizamos la imagen en escala de grises
    _,frame=video.read()
    imagen_grises2 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Foreground",imagen_grises2)

    # Restamos los valores de las imagenes
    diferencia_imagenes = np.absolute(np.matrix(np.int16(imagen_grises))-np.matrix(np.int16(imagen_grises2)))
    diferencia_imagenes[diferencia_imagenes>255]=255
    diferencia_imagenes=np.uint8(diferencia_imagenes)
    cv2.imshow("diferencia_imagenes",diferencia_imagenes)    
    
    # Establecemos los limites de la diferencia
    Diff = diferencia_imagenes
    Diff[Diff<=100]=0
    Diff[Diff>100]=1

    columnaSuma=np.matrix(np.sum(Diff,0))

    # Enumeramos cada uno de los elementos en X
    columnaNum=np.matrix(np.arange(ancho))
    columnaMult=np.multiply(columnaSuma,columnaNum)
    total=np.sum(columnaMult)
    totalTotal=np.sum(np.sum(Diff))
    columnaLocal=total/totalTotal

    # Localización en x
    x_localizacion = columnaLocal*cm_por_pixel_x

    filaSuma=np.matrix(np.sum(Diff,1))
    filaSuma = filaSuma.transpose()

    # Enumeramos cada uno de los elementos en Y
    filaNum=np.matrix(np.arange(alto))
    filaMult=np.multiply(filaSuma,filaNum)
    total=np.sum(filaMult)
    totalTotal=np.sum(np.sum(Diff))
    filaLocal=total/totalTotal

    # Mostramos la localización en Y
    y_localizacion = filaLocal*cm_por_pixel_y
    print(x_localizacion,y_localizacion)

    k=cv2.waitKey(5)
    if k==27:
        break
# Destruimos todas las ventanas
cv2.destroyAllWindows()