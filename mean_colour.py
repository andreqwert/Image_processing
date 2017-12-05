# Преобразование серого мира 
# (предполагает, что средний уровень цвета по каждому из каналов должен быть одинаков)
from skimage.io import imread, imsave
from numpy import dstack
import numpy as np
from skimage import img_as_float, img_as_ubyte



img = imread('railroad.png')
img = img_as_float(img) 

r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]

rmean, gmean, bmean = r.mean(), g.mean(), b.mean()

avg = (rmean + gmean + bmean) / 3

# Поправочные коэффициенты
rw, gw, bw = rmean / avg, gmean / avg, bmean / avg

# Производим, непосредственно, цветокоррекцию
r /= rw
g /= gw
b /= bw

img_rgb = dstack((r, g, b))
img_rgb = np.clip(img_rgb, 0, 1)
print(img_rgb)
img = imsave('out_img.png', img_rgb)
