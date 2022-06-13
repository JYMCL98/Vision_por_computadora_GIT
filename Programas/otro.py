import numpy as np
import time
import matplotlib.pyplot as plt

x = np.linspace(0,10,100)
y = np.cos(x)

plt.ion()

figure, ax = plt.subplots(figsize=(8,6))
line = ax.plot(x,y)
point, = ax.plot(0,0,'bo')
plt.title('Simulación dinámica de la funcion cos(x)', fontsize=25)

plt.xlabel("X",fontsize=18)
plt.ylabel("cos(x)",fontsize=18)


for p in x:
	point.set_xdata(p)
	point.set_ydata(np.cos(p))

	figure.canvas.draw()
	figure.canvas.flush_events()
	time.sleep(0.1)