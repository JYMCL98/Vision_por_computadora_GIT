# Importamos las librerías
import cv2
import numpy as np

# Ejecutamos la camara
video = cv2.VideoCapture(0)

while True:
    # Visualizamos la camara
    _,frame = video.read()
    cv2.imshow("Imagen en rgb",frame)
    # Repetimos fgrames para cada color
    rojo = frame[:,:,2]
    verde = frame[:,:,1]
    azul = frame[:,:,0]
    
    # Establesemos los limites para rojo
    solo_rojo = np.int16(rojo)-np.int16(verde)-np.int16(azul)
    
    solo_rojo[solo_rojo<0]=0 #si es menor a cero, lo pone en 0
    solo_rojo[solo_rojo>255]=255 #si es mayor a 255, lo pone en 255
    solo_rojo = np.uint8(solo_rojo)

    # Localización en x
    suma_columnas = np.matrix(np.sum(solo_rojo,0)) # se suman las comlumnas
    # enumero cada uno de los elementos de la matriz
    columna_numeracion = np.matrix(np.arange(640)) # resolución de la cámara
    columna_multiplicacion = np.multiply(suma_columnas,columna_numeracion)
    total = np.sum(columna_multiplicacion)
    total_total = np.sum(np.sum(solo_rojo))
    localizacion_columna = total/total_total


    # Mostramos las ventanas para cada color
    cv2.imshow("Rojo: ",rojo)
    cv2.imshow("Verde: ",verde)
    cv2.imshow("Azul: ",azul)
    cv2.imshow("Color solo rojo: ",solo_rojo)

    print(f"Localizacion columna: {localizacion_columna}")

    k= cv2.waitKey(5)
    if k ==27:
        break

# Destruimos todas las ventanas y mostramos las matrices
cv2.destroyAllWindows()
print(f"Rojo: {rojo}\n")
print(f"Verde: {verde}\n")
print(f"Azul: {azul}\n")

print(f"Solo rojo: {solo_rojo}\n")