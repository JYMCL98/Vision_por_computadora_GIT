# Importamos las librerías
import cv2

# Cargamos la imagen a utilizar
img = cv2.imread("Imagenes/frt.png")
img_copia = img.copy()
img_grises = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,img_binarizada = cv2.threshold(img_grises,245,255,cv2.THRESH_BINARY)
img_binarizada_inv = ~img_binarizada

# Encontramos los contornos y los dibujamos
contornos,jeraquia = cv2.findContours(img_binarizada_inv,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
img_con_contornos = cv2.drawContours(img,contornos,-1,(0,0,255),3)
cv2.imshow("Imagen con contornos",img_con_contornos)

# Usamos la imagen de referencia
img_ref = cv2.imread("Imagenes/refe1.png")
# Ponemos la imagen de referencia en escala de grises
img_ref_grises = cv2.cvtColor(img_ref,cv2.COLOR_BGR2GRAY)
# Binarizamos la imagen de referenecia
ret, img_ref_binarizada = cv2.threshold(img_ref_grises,245,255,cv2.THRESH_BINARY)
# Obtenemos la binarización inversa de la imagen de referencia
img_ref_binarizada_inv = ~img_ref_binarizada

# Encontramos los contornos
contor_ref, jerarquia_ref = cv2.findContours(img_ref_binarizada_inv,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
img_ref_contorno = cv2.drawContours(img_ref,contor_ref,-1,(0,0,255),3)

# Mostramos la cantidad de contornos
print("Total de contornos: ")
print(len(contor_ref))

contorno_ref = contor_ref[0]

# Creamos una lsita para los contornos
new_lista = []

for cnt in contornos:
	variable = cv2.matchShapes(cnt, contorno_ref,1,0)
	new_lista.append(variable)

# Hacemos una copia de la lista y se ordena de menor a mayor
sorted_list = new_lista.copy()
sorted_list.sort()
# Se guardan las variables para nuevas listas
ind1_dist = new_lista.index(sorted_list[0])
ind2_dist = new_lista.index(sorted_list[1])

# Ingresamos los contornos
ejote_cnts = []
ejote_cnts.append(contornos[ind1_dist])
ejote_cnts.append(contornos[ind2_dist])

# Dibujamos los contornos
img_con_contornos2 = cv2.drawContours(img,ejote_cnts,-1,(255,0,0),3)
cv2.imshow("Objeto detectado en imagen", img_con_contornos2)

# Dibujamos un rectángulo en lugar del contorno
for cnt in ejote_cnts:
	x,y,w,h = cv2.boundingRect(cnt)
	if h>w:
		cv2.rectangle(img_copia,(x,y),(x+w,y+h),(255,0,0),2)

# Mostramos la imagen con el rectángulo
cv2.imshow("Imagen detectado en RGB",img_copia)

cv2.waitKey(0)
