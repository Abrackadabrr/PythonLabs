import numpy as np
import matplotlib.pyplot as plt
steps = [0, 3, 1, 2]


def slide_average(N):
    global data
    return data[max(0, int(N)-9): min(int(N) + 1, data.size - 1)].mean()


for i in range(1, 4):
    with open(f'/media/evgen/Big_disc/MIPT/2nd level/Chapter 3/Python/PythonLabs/Numpy/Ex2/signals/signal0{i}.dat') as file:
        data = np.array(file.readlines(), dtype=np.float64)
    new_data = np.array(list(map(slide_average, list(np.arange(0, data.size, 1)))))

    fix, (ax, ox) = plt.subplots(ncols=2)
    ox.plot(np.linspace(0, data.size, data.size), new_data)
    ax.plot(np.linspace(0, data.size, data.size), data)
    ax.set_xticks(np.arange(0, data.size + 1, 10))
    ax.set_yticks(np.arange(0, int(data.max()) + 1, steps[i]))
    ax.grid()

    ox.set_xticks(np.arange(0, new_data.size + 1, 10))
    ox.set_yticks(np.arange(0, int(new_data.max()) + 1, steps[i]))
    ox.grid()
    ax.set_title('До обработки')
    ox.set_title('После обработки')
    plt.savefig(f'signal0{i}_filtered.png')
    plt.show()
