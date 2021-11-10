from PIL import Image
import numpy as np

for i in range(1,4):
    img = Image.open(
        f"/media/evgen/Big_disc/MIPT/2nd level/Chapter 3/Python/PythonLabs/Numpy/Ex1/lunar_images/lunar0{i}_raw.jpg")
    data = np.array(img)
    data = data - data.min()
    new_colors = np.linspace(0, 255, data.max() + 1)
    for index in range(len(data)):
        for jndex in range(len(data[0])):
            data[index, jndex] = int(new_colors[data[index, jndex]] + data[index, jndex])
    res_img = Image.fromarray(data)
    print(data.max(), data.min())
    res_img.save(f'lunar0{i}_raw_contrast.jpg')
