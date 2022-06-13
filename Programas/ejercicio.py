		# Universidad Autonoma Chapingo
		# Mecatronica 6° 7
		# Jym Emmanuel Cocotle Lara


import math # Importamos la libreria math
import matplotlib.pyplot as plt # Importamos la libreria matplotlib.pyplot
from mpl_toolkits.mplot3d import Axes3D # Importamos Axes3D de mpl_toolkits.mplot3d


# Ejercicio 1
print("Ejercicio 1") # Establecemos el inicio del ejercicio 1 con un mensaje
# Coordenadas rectangulares
# x=5 y=6 z=3
x = 5 # Asignamos el valor 5 a la variable x
y = 6 # Asignamos el valor 5 a la variable y
z = 3 # Asignamos el valor 5 a la variable z

print(f'Las coordenadas rectangulares son x = {x}, y = {y}, z = {z}') # Visualizamos las coordenadas rectangulares
# Convertimos las coordenadas cuadradas a cilíndricas
R = math.sqrt(x**2 + y**2) # Asignamos el valor correspondiente a R con ayuda de la fórmula
theta = math.degrees(math.atan(y/x)) # Asignamos el valor correspondiente a theta con ayuda de la fórmula y con ayuda de la librería math podemos obtener el valor de atan y asi mismo poder convertirlo a grados
Z = z #Asignamos el valor correspondiente a Z con ayuda de la fórmula
print(f'Las coordenadas cilíndricas son R = {R}, theta = {theta}, z = {Z}') # Visualizamos las coordenadas cilíndricas
# Convertimos las coordenadas cuadradas a esféricas
r = math.sqrt(x**2+y**2+z**2) #Asignamos el valor correspondiente a r con ayuda de la fórmula
phi = math.degrees(math.atan(y/x)) #Asignamos el valor correspondiente a phi con ayuda de la fórmula, y con ayuda de la librería math podemos obtener el valor de atan y asi mismo poder convertirlo a grados
theta1 = math.degrees(math.acos(z/r)) #Asignamos el valor correspondiente a theta1 con ayuda de la fórmula y con ayuda de la librería math podemos obtener el valor de acos y asi mismo poder convertirlo a grados
print(f'Las coordenadas esféricas son r = {r}, theta = {theta1}, phi = {phi}') # Visualizamos las coordenadas esféricas

fig = plt.figure() # Se crea una figura
ax = Axes3D(fig) # Se crea una variable a graficar
ax.plot(x,y,z,'bo') # Se gráfica el punto de interes a partir de las coordenadas rectangulares, con ayuda de la librería matplotlib


# Ejercicio 2
print("Ejercicio 2") # Establecemos el inicio del ejercicio 2 con un mensaje
# Coordenadas cilíndricas
# R=5 phi=20 z=10
R2 = 5 # Asignamos el valor 5 a la variable R2
theta2 = 20 # Asignamos el valor 20 a la variable theta2
Z2 = 10 # Asignamos el valor 10 a la variable Z2

# Convertimos las coordenadas cilíndricas a cuadradas
x2 = R2*math.cos(math.radians(theta2)) #Asignamos el valor correspondiente a x2 con ayuda de la fórmula y con ayuda de la librería math podemos obtener el valor en radianes
y2 = R2*math.sin(math.radians(theta2)) #Asignamos el valor correspondiente a y2 con ayuda de la fórmula
z2 = Z2 #Asignamos el valor correspondiente a z2 con ayuda de la fórmula
print(f'Las coordenadas rectangulares son x = {x2}, y = {y2}, z = {z2}') # Visualizamos las coordenadas rectangulares

print(f'Las coordenadas cilíndricas son R = {R2}, theta = {theta2}, z = {Z2}') # Visualizamos las coordenadas cilíndricas

# Convertimos las coordenadas cuadradas a esféricas
r2 = math.sqrt(x2**2+y2**2+z2**2) #Asignamos el valor correspondiente a r2 con ayuda de la fórmula
phi2 = math.degrees(math.atan(y2/x2)) #Asignamos el valor correspondiente a phi2 con ayuda de la fórmula
theta2 = math.degrees(math.acos(z2/r2)) #Asignamos el valor correspondiente a theta2 con ayuda de la fórmula
print(f'Las coordenadas esféricas son r = {r2}, theta = {theta2}, phi = {phi2}') # Visualizamos las coordenadas esféricas

fig2 = plt.figure() # Se crea una figura
ax2 = Axes3D(fig2) # Se crea una variable a graficar
ax2.plot(x2,y2,z2,'go') # Se gráfica el punto de interes a partir de las coordenadas rectangulares, con ayuda de la librería matplotlib


# Ejercicio 3
print("Ejercicio 3") # Establecemos el inicio del ejercicio 3 con un mensaje
# Coordenadas esféricas
# r=7 phi=12 theta=45
r3 = 7 # Asignamos el valor 7 a la variable r3
phi3 = 12 # Asignamos el valor 12 a la variable phi3
theta3 = 45 # Asignamos el valor 45 a la variable theta3

# Convertimos las coordenadas esféricas a rectangulares
x3 = r3*math.sin(math.radians(theta3))*math.cos(math.radians(phi3)) #Asignamos el valor correspondiente a x3 con ayuda de la fórmula
y3 = r3*math.sin(math.radians(theta3))*math.sin(math.radians(phi3)) #Asignamos el valor correspondiente a y3 con ayuda de la fórmula
z3 = r3*math.cos(math.radians(theta3)) #Asignamos el valor correspondiente a z3 con ayuda de la fórmula
print(f'Las coordenadas rectangulares son x = {x3}, y = {y3}, z = {z3}') # Visualizamos las coordenadas rectangulares

# Convertimos las coordenadas rectangulares obtenidas a cilíndricas
R3 = math.sqrt(x3**2 + y3**2) # Asignamos el valor correspondiente a R3 con ayuda de la fórmula
theta4 = math.degrees(math.atan(y3/x3)) # Asignamos el valor correspondiente a theta4 con ayuda de la fórmula
Z3 = z3 # Asignamos el valor correspondiente a Z3 con ayuda de la fórmula
print(f'Las coordenadas cilíndricas son R = {R3}, theta = {theta4}, z = {Z3}') # Visualizamos las coordenadas cilíndricas

print(f'Las coordenadas esféricas son r = {r3}, theta = {theta3}, phi = {phi3}') # Visualizamos las coordenadas esféricas

fig3 = plt.figure() # Se crea una figura
ax3 = Axes3D(fig3) # Se crea una variable a graficar
ax3.plot(x3,y3,z3,'ro') # Se gráfica el punto de interes a partir de las coordenadas rectangulares, con ayuda de la librería matplotlib

plt.show() # Arroja las gráficas para visualizarla
#