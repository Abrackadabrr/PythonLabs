import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

with open('Ex2/bigsystem.txt') as f:
    data = f.readlines()
    for i in range(len(data)):
        data[i] = data[i].split()

n = int(data[0][0])
a = np.array(data[1:n+1], dtype=np.float64)
b = np.array(data[n+1])
x = linalg.solve(a, b)

fig, ax = plt.subplots()
ax.bar(np.arange(1, n+1), x)
ax.set_title('Решение СЛАУ')
ax.grid(True)
plt.savefig('Ex2/solution.png')
plt.show()
