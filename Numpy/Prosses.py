import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def next_frame(i):
    """
    Create next frame of calculations
    :param i: number of a frame
    :return: tuple with line object first
    """
    global matrix
    line.set_ydata(matrix @ line.get_ydata())
    return line,


fig, ax = plt.subplots()

# loading initial data
p = np.loadtxt('Ex3/start.dat')

# creation of a matrix
matrix = (np.eye(p.size) + np.roll(np.eye(p.size), 1, axis=0)) / 2
line, = ax.plot(np.arange(0, p.size, 1), p)

# create an animation instance
ani = animation.FuncAnimation(fig, next_frame, interval=120, frames=np.arange(0, 255, 1), repeat=False)

ax.set_xticks(np.arange(0, p.size+1, 5))
ax.set_yticks(np.arange(0, p.max() + 1,  (p.max() + 1)//10))
ax.grid()
ax.set_title('Расчет течения процесса по времени')

# saving animation
ani.save("Ex3/process.gif", animation.PillowWriter(fps=25))
