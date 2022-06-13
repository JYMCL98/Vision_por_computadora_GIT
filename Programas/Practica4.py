# Manejo de funciones
# Algunos ejemplos son los que ya hemos trabajado en la libreria math
# sin, cos, len, array

import numpy as np # Importamos la libreria numpy

# Estructura para definir una funcion
def nombre_funcion(parametro1, parametro2): #Creamos una función que recibe 2 parametros
	print(2+2) #Imprimimos la operación de 2+2

# Existen 4 tipos de funciones

# a) la funcion que recibe y devuelve valores
def suma_digitos(a,b): #Creamos una funcion que recibe dos valores
	operacion_salida = a+b #Creamos una operacion en la que sumamos los dos valores recibidos
	return operacion_salida #Devolvemos el valor de la operacion

# b) La funcion que recibe valores pero  no devuelve valores
def suma_digitos2(a,b): #Creamos una funcion que recibe dos valores
	suma_parametros = a+b #Creamos una operación en la que sumamos los dos valores recibidos
	print(suma_parametros) #Visualizamos la operación

# c) La funcion que no recibe valores y no devuelve valores
def suma_digitos3(): #Creamos una funcion la cual no recibe valores
	print(3+4) #Visualizamos la operacion de 3+4

# d) La funcion que no recibe valores pero si devuelve valores
def suma_digitos4(): #Creamos una funcion la cual no recibe valores
	suma_parametros = 3+4 #Creamos una operacion en la que sumamos dos valores establecidos
	return(suma_parametros) #Devolvemos el valor de la operacion

# Llamado de funciones
print(suma_digitos(3,4)) # Llamamos a la funcion tipo a)
suma_digitos2(5,9) # Llamamos a la funcion tipo b)
suma_digitos3() # Llamamos a la funcion tipo c)
print(suma_digitos4()) # Llamamos a la funcion tipo d)

# Regresar mas de un valor en una funcion
def suma_trigonometrica(a,b): #Creamos una funcion que recibe dos valores
	salida1 = np.sin(a) + np.cos(b) #Con ayuda de la libreria numpy creamos una operacion en la que sumamos el seno con el coseno de los valores recibidos
	salida2 = np.sin(b) + np.cos(b) #Con ayuda de la libreria numpy creamos una operacion en la que sumamos el seno con el coseno de los valores recibidos
	return salida1,salida2,[salida1,salida2] #Devolvemos los valores obtenidos de las operaciones

print(suma_trigonometrica(2,3)) #Hacemos uso de la funcion creada con los valores de 2 y 3

def imprimir_porra(frase1="Jauri",frase2="ra"): #Creamos una funcion con dos cadenas establecidas
	print(f"{frase1} ju, {frase1} ja, Chapingo {frase2}, toros salvajes {frase2}{frase2}{frase2}") #Visualizamos un texto mandando a llamar las cadenas establecidas

imprimir_porra() #Mandamos a llamar a la funcion creada

#Ejemplos de variables localoes y variables globales
#Ejemplo de variable local
def suma_variables(a,b,c): #Creamos una funcion que recibe 3 valores
	operacion = a+b+c #Sumamos los valores recibidos
	print(f"El valor de la variable adentro de la funcion es {operacion}") #Visualizamos el resultado de la suma
	return operacion #Devolvemos el valor obtenido de la operación

operacion = 1 #Igualamos a la variable operacion con 1
suma_variables(1,2,3) #Mandamos a llamar a la funcion creada ay a las variables les damos el valor de 1, 2, 3 respectivamente

print(f"El valor de la variable afuera de la funcion es {operacion}") #Visualizamos el valor de la variable que colocamos fuera de la función

#Ejemplo de variable global
n = 24 #Declaramos una variable
def funcion(): #Creamos una funcion
	global n #Se manda a llamar a la variable globval n
	print(f"Adentro de la funcion el valor de n es {n}") #Visualizamos el valor de la variable global
	n = 3 #Reasiganmos el valor de la variable global
	print(f"Adentro de la funcion el nuevo valor asignado de n es {n}") # Visualizamos el nuevo valor de la variable

funcion() #Llamamos a la funcion creada
print(f"Afuera de la funcion el valor de n es {n}") #Visualizamos el valor de la variable n actual

#Ejemplo de funciones anidadas
def funcion_xyz(x,y,z): #Creamos una funcion que recibe 3 valores
	def funcion_xy(x,y): #Creamos una segunda funcion dentro de la funcion la cual recibe dos valores
		out = np.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2) #Realizamos una operacion en la cual referenciamos los valores en base a la pasicion
		return out #Devolvemos el valor obtenido de la operacion
	d0 = funcion_xy(x,y) #Hacemos uso de la segunda funcion y la igualamos con la variable d0
	d1 = funcion_xy(x,z) #Hacemos uso de la segunda funcion y la igualamos con la variable d1
	d2 = funcion_xy(y,z) #Hacemos uso de la segunda funcion y la igualamos con la variable d2
	return [d0,d1,d2] #Devolvemos los valores de las variables d0, d1, d2

print(funcion_xyz((15,0),(0,1),(1,1))) #Hacemos uso de la función anidada

#Funcion lambda

print(3**2) #Visualizamos el cuadrado de 3

cuadrado = lambda x:x**2 #Creamos una funcion lambda con la cual obtenemos el cuadrado de un numero

print(cuadrado(3)) #Visualizamos el valor del cuadrado de 3 usando la funcion lambda

def variable_cuadrado(x): #Creamos una funcion con una variable de entrada
	salida = x**2 #Realizamos una operacion en la que obtenemos el cuadrado de un numero y lo igualamos con una variable
	return salida #Devolvemos la variable de salida
print(variable_cuadrado(3)) #Hacemos uso de la funcion visualizando el cuadrado de 3