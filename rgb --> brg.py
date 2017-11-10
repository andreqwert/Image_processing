"""
Загрузите изображение из файла img.png. У этого изображения поменяйте местами каналы так, чтобы вместо порядка RGB каналы шли в порядке BRG. 
Сохраните изображение с измененными каналами в файл out_img.png.
"""


from skimage.io import imread, imsave, imshow
from numpy import dstack
from skimage import img_as_float


img = imread('tiger-color.png')
img_f = img_as_float(img) # перевод диапазона в вещественные числа


# Берем все строки и все столбцы изображения. Последний аргумент - номер цветового канала
b = img_f[:, :, 2]
r = img_f[:, :, 0]
g = img_f[:, :, 1]

img_combined = dstack((b, r, g))

imsave('rgb -> brg.png', img_combined)
