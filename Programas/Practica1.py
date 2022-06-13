import math

print('hola mundo') # Esto sirve para imprimir un texto
print(3*4) #Multiplicación
print((3*4)/((2**2)+(4/2))) #suma, resta, multiplicación, división y potencia

#Utilizando una libreria
print(math.sqrt(4)) #Raiz cuadrada
print(math.sin(math.pi/2)) #La función seno evaluada en pi/2
print(math.exp(math.log(10))) #La función exponencial de logaritmo natural
print(math.exp(math.log10(10))) #Función ex´ponencial de logaritmo base 10
print(math.exp(3/4)) #Funcion exponencialde una fracción
print(1/math.inf) #División de 1 entre infinito
print(math.inf*2) #Multiplicación de infinito por 2
print(math.inf/math.inf) #división de infinito sobre infinito

#Manejo de tipo de numeros
print(type(1234)) #Conocer el tipo de numero
print(type(3.2)) #Conocer el tipo de numero
print(type(2+5j)) #Conocer el tipo de numero
print(2+5j) #Generar un numero complejo opcion 1
print(complex(2,5)) #Generar un numero complejo opcion 2

#Manejo de notación científica
print(1e6) #Visualizamos una forma de expresar un millon
print(1e-3) #Visualizamos una forma de expresar una milesima

#manejo de operadores
print(5==4) #Preguntamos si los numeros son iguales
print(5>4) #Preguntamos si 5 es mayor que 4
print(5>=4) #Preguntamos si 5 es mayor que 4
print(5<4) #Preguntamos si 5 es menor que 4
print(5<=4) #Preguntamos si 5 es menor o igual que 4
print(5!=4) #Preguntamos si 5 es diferente de 4

print((1+3)>(2+5)) #Preguntamos si 1+3 es mayor que 2+5
print((3>2)+(5>4)) #Preguntamos si 3 es mayor que 2 y si 5 es mayor que 4 
print((14*24+60+60)>1000000) #Preguntamos si 14*24+60+60 es mayor que 1000000