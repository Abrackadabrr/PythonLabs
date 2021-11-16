from PIL import Image
import numpy as np

for i in range(1, 4):
    img = Image.open(
        f"Ex1/lunar_images/lunar0{i}_raw.jpg")
    data = np.array(img)
    data = data - data.min()
    data = data * (255/data.max())
    res_img = Image.fromarray(data.astype(np.uint8))
    res_img.save(f'Ex1/lunar0{i}_raw_contrast.jpg')
