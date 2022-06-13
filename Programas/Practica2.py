#Manejo de variables

x = 1 #Declaracion de una variable
print(x) #impresión de una variable

y=2 #Declaramos otra variable
print(y*3) #Multiplicacion de una variable por un escalar.

x = x + 1 #Reasignamos el valor de la variable
print(x) # Visualizamos el resultado

mensaje1= "Hola" #Declaramos una variable de tipo cadena
mensaje2= "mundo" #Declaramos una variable de tipo cadena

print(mensaje1+mensaje2) #Concatenación de dos variables de tipo cadena
print(mensaje1+" "+mensaje2) #Concatenación de variables de tipo cadena

mensaje_completo = mensaje1+" "+mensaje2 #Definimos una variable de tipo cadena
print(len(mensaje_completo)) #Contamos los caracteres de la variable

print(mensaje_completo[9]) #Acceder a cualquier espacio dentro del mensaje
print(mensaje_completo[2:7]) #Accedemos a un fragmento de la cadena
print(mensaje_completo[5:]) #Accedemos a un espacio completo de la variable desde un punto
print(mensaje_completo[:4]) #Accedemos a un espacio completo de la variable desde un punto

print("El valor de y="+str(y)) #Convertimos y concatenamos el valor de una variable int

lema = "Solo aquel que este dispuesto a morir deberia tener el poder de matar!!" #Declaramos una variable de tipo cadena

print(lema) #Visualizamos el contenido de la variable
print(lema.upper()) #Cambiamos de minusculas a mayusculas todas las letras del mensaje
print(lema.count("e")) #Contamos todas las letras e
print(lema.count("a")) #Contamos todas las letras a
print(lema.replace("morir","vivir")) #Reemplazamos la palabra morir por vivir en el lema


universidad = "Chapingo" #Declaramos una variable de tipo cadena
departamento = "DIMA" #Declaramos una variable de tipo cadena

print("El mejor departamento de %s es el %s"%(universidad,departamento)) #Imprimimos el mensaje con las variables declaradas
print(f"El mejor departamento de {universidad} es el {departamento}") #Imprimimos el mensaje con las variables declaradas de manera diferente

#Estructura de tipo lista
lista_numeros = [1,2,3] #Declaramos una variable de tipo lista
print(lista_numeros) #Visualizamos el contenido de la variable

lista_palabras = ["Manzana","Pera","Guayaba"] #Declaramos una variable de tipo lista
print(lista_palabras) #Visualizamos el contenido de la variable

lista_concatenada = [1,2,3,"Manzana","Pera","Guayaba"] #Declaramos la lista concatenada
print(lista_concatenada) #Visualizamos el contenido de la variable

lista_concatenada2 = [lista_numeros,lista_palabras] #Concatenamos 2 listas
print(lista_concatenada2) #Visualizamos el contenido de la variable

print(lista_concatenada[0]) #Accesamos al valor 0 de la lista
print(lista_concatenada[3]) #Accesamos al valor 3 de la lista
print(lista_concatenada[5]) #Accesamos al valor 5 de la lista

lista_concatenada3 = lista_numeros+lista_palabras #Concatenamos dos listas
print(lista_concatenada3) #Visualizamos el contenido de la variable

lista_concatenada3.insert(3,"sandia") #Insertamos un nuevo valor a la lista
print(lista_concatenada3)#Visualizamos el contenido de la variable

del lista_concatenada3[6] #Borramos el valor ubicado en el espacio 6
print(lista_concatenada3) #Visualizamos el contenido de la variable

#Estructura de tuplas
variable_tupla = (1,2,3,4) #Declaramos una variable de tipo tupla
print(variable_tupla) #Visualizamos el contenido de la variable tupla
print(len(variable_tupla)) #Contamos los elementos de la variable tupla
print(variable_tupla[1:3]) #Accesamos al intervalo de valores dentro de la variable

lista_tuplas = [("Manzana",1),("Naranja",2),("Pera",3)] #Declaramos una variable de tipo tupla
print(lista_tuplas) #Visualizamos el contenido de la variable tupla

a,b,c = lista_tuplas #Declaramos una variable de tipo tupla
print(a) #Visualizamos el contenido de la variable tupla
print(b) #Visualizamos el contenido de la variable tupla
print(c) #Visualizamos el contenido de la variable tupla

#Estructura set
datos = {3,3,2,1,4,5,6,4,2} #Declaramos una variable tipo set
print(datos) #Visualizamos el contenido de la variable set

lista_enteros = [1,2,3,3,2,1,2] #Declaramos una variable de tipo lista
print(set(lista_enteros)) #Visualizamos el contenido de la lista

fruta = "Manzana" #Declaramos una variable de tipo cadena
print(set(fruta)) #Visualizamos el contenido de la variable

#Estructura de tipo diccionario
diccionario = {"Apple":3,"Orange":6,"Watermelon":1} #Declaramos una variable de tipo diccionario
print(diccionario) #Visualizamos su valor

print(diccionario["Apple"]) #Accesamos al valor del diccionario con la palabra apple
print(diccionario.keys()) #Conocemos todas las palabras clave del diccionario
print(diccionario.values()) #Conocemos todas las definiciones del diccionario
print(len(diccionario)) #Contamos los elementos del diccionario

diccionario_string = {"Apple":"tres","Orange":"seis","Watermelon":"uno"} #Declaramos una variable de tipo diccionario con valores tipo cadena
print(diccionario_string["Apple"]) #Accesamos al valor del diccionario con la palabra apple
print(diccionario_string.keys()) #Conocemos todas las palabras clave del diccionario
print(diccionario_string.values()) #Conocemos todas las definiciones del diccionario
print(len(diccionario_string)) #Contamos los elementos del diccionario

print("Apple" in diccionario) #Buscamos esta palabra clave "Apple" en el diccionario
print("Sandia" in diccionario) #Buscamos esta palabra clave "Sandia" en el diccionario
print(list(diccionario)) #Visualizamos los palabras del diccionario sin sus valores

