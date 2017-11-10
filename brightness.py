"""
Загрузите цветное изображение из файла img.png. Подсчитайте яркость этого изображения и сохраните в файл out_img.png. 
Результирующее изображение должно быть одноканальным. Для подсчета яркости используйте формулу 
Y=0.2126⋅R+0.7152⋅G+0.0722⋅BY=0.2126⋅R+0.7152⋅G+0.0722⋅B, не забудьте сначала перевести изображение в вещественные числа 
(функция img_as_float), а затем в целые числа (функция img_as_ubyte).
"""


from skimage.io import imread, imsave, imshow
from numpy import dstack
from skimage import img_as_float, img_as_ubyte


img = imread('tiger-color.png')
img_f = img_as_float(img) # перевод диапазона в вещественные числа


r = img_f[:, :, 0]
g = img_f[:, :, 1]
b = img_f[:, :, 2]

y = dstack((r, g, b))
y = 0.2126*r + 0.7152*g + 0.0722*b  
imsave('y.png', img_as_ubyte(y))
