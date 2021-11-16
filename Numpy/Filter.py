import numpy as np
import matplotlib.pyplot as plt
steps = [0, 3, 1, 2]


def slide_average(N):
    global data
    return data[max(0, N-9): N + 1].mean()


for i in range(1, 4):
    with open(f'Ex2/signals/signal0{i}.dat') as file:
        data = np.array(file.readlines(), dtype=np.float64)
    # скользящее среднее - частный случай свёртки
    res = list(np.convolve(data, np.ones(10)/10, mode='valid'))
    res0 = [*map(slide_average, [0, 1, 2, 3, 4, 5, 6, 7, 8])]
    res = np.array(res0 + res)

    fix, (ax, ox) = plt.subplots(ncols=2)
    ox.plot(np.arange(0, data.size, 1), res)
    ax.plot(np.arange(0, data.size, 1), data)
    ax.set_xticks(np.arange(0, data.size + 1, 15))
    ax.set_yticks(np.arange(0, int(data.max()) + 1, steps[i]))
    ax.grid()

    ox.set_xticks(np.arange(0, res.size + 1, 15))
    ox.set_yticks(np.arange(0, int(res.max()) + 1, steps[i]))
    ox.grid()
    ax.set_title('До обработки')
    ox.set_title('После обработки')
    plt.savefig(f'Ex2/signal0{i}_filtered.png')
    plt.show()
