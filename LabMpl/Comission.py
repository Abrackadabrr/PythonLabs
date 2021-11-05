import csv
import matplotlib.pyplot as plt
import numpy as np
from itertools import accumulate as acc

with open('Ex3/students.csv') as File:
    reader = [i for i in csv.reader(File, delimiter=';')]

marks_per_preps = {key: [[i[2] for i in reader if key in i].count(str(key_mark)) for key_mark in np.arange(0, 11, 1)] for key in np.unique([i[0] for i in reader])}
marks_per_groups = {key: [[i[2] for i in reader if key in i].count(str(key_mark)) for key_mark in np.arange(0, 11, 1)] for key in np.unique([i[1] for i in reader])}

preps = marks_per_preps.keys()
groups = marks_per_groups.keys()
bottom_groups = [list(acc(marks_per_groups[group])) for group in groups]
bottom_preps = [list(acc(marks_per_preps[prep])) for prep in preps]

fig, ax = plt.subplots(ncols=2)

for mark in range(1, 11):
    ax[1].bar(preps, [marks_per_preps[prep][mark] for prep in preps], bottom=[i[mark-1] for i in bottom_preps], label=f'{mark}')

ax[1].set_title("Marks per preps")
ax[1].set_yticks(np.arange(0, max(np.array([i[len(bottom_preps[1])-1] for i in bottom_preps]) + [marks_per_preps[key][len(marks_per_preps[key])-1] for key in preps]), 1))


for mark in range(1, 11):
    ax[0].bar(groups, [marks_per_groups[group][mark] for group in groups], bottom=[i[mark-1] for i in bottom_groups])

ax[0].set_title("Marks per groups")
ax[0].set_yticks(np.arange(0, max(np.array([i[len(bottom_groups[1])-1] for i in bottom_groups]) + [marks_per_groups[key][len(marks_per_groups[key]) - 1] for key in groups]), 1))

fig.legend()
fig.supylabel("Blocks_of_marks")
fig.set_figheight(8)
fig.set_figwidth(12)
plt.savefig("Ex3/Distribution_of_marks.png")
plt.show()
