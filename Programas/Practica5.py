# Jym Emmanuel Cocotle Lara
# Manejo de iteraciones en Python
n = 0  # Declaramos una variable y la inicializamos en 0


# Manejamos el incremento de una variable y los mostramos
for i in range(0, 5):  # Declarando el ciclo for (indice (i), rango(0.5), incremento)
    n = n+1  # se suma 1 a la variable n durante el ciclo for
    print (n)  # Visualizamos los valores de la variable n


# Mostrar el valor del indice
for i in range(0, 5):  # El ciclo for se ejecuta hasta que la variable i sea igual a 5
    print (i)  # Visualizamos los valores de la variable i


# Manejo de listas con for
lista = [2, 3, 1, 4, 5, 7, 6]  # Declaramos una lista con diferentes valores


for j in lista:  # Con ayuda de la variable j y con un ciclo for recorremos los valores de la lista
    print(j)  # Visualizamos los valores de la lista


# Manejo de los valores de la lista como indices
lista_nueva = [2, 3, 1, 4, 5, 7, 6, 8]  # Declaramos una lista con diferentes valores
k = 0  # Declaramos la variable k y lo igualamos con 0


for i in lista:  # Con ayuda de la variable i y con un ciclo for recorremos los valores de la lista
    k = k+i  # Se suma 1 a la variable k durante el ciclo for
    print(k)  # Visualizamos los valores de la variable k


# Manejo de dos listas para crear una lista
lista_a = ["one", "two", "three"]  # Declaramos una primera lista con valores
lista_b = [1, 2, 3]  # Declaramos una segunda lista con valores


for i, j in zip(lista_a, lista_b):  # Iteramos dos listas al mismo tiempo
	print (i, j)  # Visualizamos los valores de las dos listas


# Ejemplo de una funcion que detecta digitos
def tiene_digitos(s):  # Creamos una nueva funcion
	out = 0  # Declaramos la variable out y lo igualamos con 0
	for c in s:  # Con ayuda de la variable c se recorre la variable s
		if c.isdigit():  # Si el valor en la variable s es un digito entra al ciclo
			out = out+1  # Cada vez que se cumple la condición se suma 1 a la variable
	return out  # Devuelve el valor de la variable out


print(tiene_digitos("La chica del apartamento 512"))  # Detectamos el numero de digitos que tiene la frase
print(tiene_digitos("La chica del apartamento 2e"))  # Detectamos el numero de digitos que tiene la frase
print(tiene_digitos("La chica del apartamento 12"))  # Detectamos el numero de digitos que tiene la frase


for i in range(5):  # El iterador i recorre hasta el valor 5
	if i == 2:  # Si el valor de i es igual a 2, se entra en la condicion
		continue  # El ciclo for se sigue ejecutando
	elif i == 3:  # Si el valor de i es igual a 3 se rompe el ciclo
		break  # El ciclo for se termina
	print(i)  # Visualizamos el valor de i


# Sentencia de programacion IF-ELSE (Si-SINO)
def termostato(temperatura_real, temperatura_deseada):  # Creamos una funcion con dos parametros de entrada
	if temperatura_real < temperatura_deseada:  # Si la temperatura real es menor que la temperatura deseada la condicion funciona
		status = "Heat"  # A la variable status se le asigna la palabra Heat
	elif temperatura_real > temperatura_deseada:  # Si la temperatura deseada es menor que la temperatura reak la condicion funciona
		status = "Air Cooling"  # A la variable status se le asigna la palabra Air cooling
	else:  # Si ninguna de las condiciones se cumple entonces:
		status = "Off"  # A la variable status se le asigna la palabra Off
	return status  # Devolvemos el valor de la variable status


print(termostato(25, 25))  # Se evaluan dos temperaturas y se muestra el valor de status
print(termostato(18, 25))  # Se evaluan dos temperaturas y se muestra el valor de status
print(termostato(38, 25))  # Se evaluan dos temperaturas y se muestra el valor de status


# Estructura anidada del IF
def comparacion_anidada(x, y):  # Creamos una funcion con dos parametros de entrada
	if x > 2:  # Si la variable x es mayor que 2 entonces:
		if y < 2:  # Si la variable y es menor que 2 entonces:
			out = x+y  # La variable out es igual a x mas y
		else:  # Si y no es menor que 2 entonces:
			out = x-y  # La variable out es igual a x menos y
	else:  # Si x no es mayor que x entonces:
		if y > 2:  # Si la variable y es mayor que 2 entonces:
			out = x*y  # La variable out es igual a x por y
		else:  # Si y no es mayor que 2 entonces:
			out = 0  # La variable out es igual a 0
	return out  # Devolvemos el valor de la variable out


print(comparacion_anidada(8, 1))  # Evaluamos dos numeros y se muestra el valor de out
print(comparacion_anidada(8, 9))  # Evaluamos dos numeros y se muestra el valor de out
print(comparacion_anidada(1, 9))  # Evaluamos dos numeros y se muestra el valor de out
print(comparacion_anidada(-1, 1))  # Evaluamos dos numeros y se muestra el valor de out


# Estructura while
i = 0  # Declaramos la variable i y la igualamos a 0
n = 8  # Declaramos la variable n y la igualamos a 8


while n >= 1:  # La condicion while permanece activa mientras la condicion es verdadera
	n /= 2  # El valor de n se divide entre 2 y se reestablece el valor de n
	i += 1  # A la variable i se le suma 1 y se reestablece el valor de i
print(f"n = {n}, i = {i}")  # Visualizamos el valor de n e i
