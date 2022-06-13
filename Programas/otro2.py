import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
x = np.arange(0,2*np.pi,0.01)
line, = ax.plot(x,np.sin(x))
point, = ax.plot([],[],'bo')

def animate(i):
	point.set_xdata(x[i])
	point.set_ydata(np.sin(x[i]))
	return line,point

ani = animation.FuncAnimation(fig,animate,frames=624,interval=2,blit=True,save_count=50)

plt.show()