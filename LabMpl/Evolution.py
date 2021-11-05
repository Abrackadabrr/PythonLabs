import numpy as np
import matplotlib.pyplot as plt

SCALE_CONSTANT = 0.005

with open("/media/evgen/Big_disc/MIPT/2nd level/Chapter 3/Python/LabMpl/Ex2/data.txt") as f:
    data = np.array([i.split() for i in f.readlines()], dtype=float)

fig, ax = plt.subplots(ncols=2, nrows=3)

ax = ax.flatten()
fig.set_figheight(10)
fig.set_figwidth(10)
fig.suptitle("Evolution of system")
for i in range(len(ax)):
    ax[i].set_title(f"Frame {i}")
    ax[i].plot(data[i * 2], data[i * 2 + 1], color='red')
    ax[i].grid(which='major')
    ax[i].set_ylim(-12, 12)
    ax[i].set_xticks(np.arange(0, int(max(data[i * 2])) + 2, 2))
    ax[i].set_yticks(np.arange(-12, 12, 2))
    ax[i].grid(True)
    ax[i].get_xaxis().set_ticks_position('bottom')
    ax[i].get_yaxis().set_ticks_position('left')
    pos = ax[i].get_position().corners()
    pos = [*pos[0]] + [pos[3][0] - pos[0][0], pos[3][1] - pos[0][1]]
    pos[1] += SCALE_CONSTANT * (5 - (i - i % 2))
    ax[i].set_position(pos)

fig.set_figheight(SCALE_CONSTANT*1900 + 2)
fig.set_figwidth(SCALE_CONSTANT*1900)

plt.savefig("/media/evgen/Big_disc/MIPT/2nd level/Chapter 3/Python/LabMpl/Ex2/evolution.png")
plt.show()
