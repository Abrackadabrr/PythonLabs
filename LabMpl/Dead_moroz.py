import matplotlib.pyplot as plt

s = [4, 20, 6, 4, 3]
size = [[4, 12], [8, 8], [6, 14], [6, 14], [6, 14]]
for i in range(1, 6):
    with open(f"/media/evgen/Big_disc/MIPT/2nd level/Chapter 3/Python/LabMpl/Ex1/data_dead_moroz/00" + str(
            i) + ".dat") as f:
        n = int(f.readline())
        points = [i.split() for i in f.read().split("\n")]
        points = points[0:n]
    fig, ax = plt.subplots()
    points_x = [float(i[0]) for i in points]
    points_y = [float(i[1]) for i in points]
    max_x = max(points_x)
    min_x = min(points_x)
    max_y = max(points_y)
    min_y = min(points_y)

    ax.set_aspect('equal')
    fig.set_figheight(size[i - 1][0])
    fig.set_figwidth(size[i - 1][1])
    ax.set_title(f"Number of points {n}")
    ax.scatter(points_x, points_y, s=s[i - 1], color='g')
    plt.savefig("Ex1/" + str(i) + ".png")
