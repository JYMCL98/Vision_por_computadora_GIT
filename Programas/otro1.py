import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = 5
y = 6
z = 3

#Convertir theta a grados
grados = 180/math.pi

print(f'Las coordenadas rectangulares son x = {x}, y = {y}, z = {z}')

R = math.sqrt(x**2 + y**2)
theta = math.degrees(math.atan(y/x))#*grados
Z = z

print(f'Las coordenadas cilíndricas son R = {R}, theta = {theta}, z = {Z}')

r = math.sqrt(x**2+y**2+z**2)
theta = math.degrees(math.atan(y/x))#*grados
phi = math.acos(z/r)*grados
print(f'Las coordenadas esféricas son r = {r}, theta = {theta}, phi = {phi}')

fig = plt.figure()
ax = Axes3D(fig)

ax.plot(x,y,z,'bo')
plt.show()