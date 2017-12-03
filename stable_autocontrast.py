"""
Прочитайте изображение из файла img.png. Примените к нему линейное выравнивание яркости: примените к каждому пикселю функцию
f(x) = (x-xmin) * (255/(xmax-xmin))
Для вычисления максимума и минимума отбрасывайте по 5% самых светлых и самых темных пикселей (как в предыдущем задании). 
Перед вычислениями приведите изображение в вещественные числа (img.astype('float')), иначе может возникнуть переполнение 
(т.к. значения некоторых пикселей мы игнорируем при подсчете минимума и максимума). 
После растяжения яркости обрежьте значения изображения от 0 до 255 с помощью функции numpy.clip.
После вычисления функции значения изображения окажутся вещественными. 
Чтобы привести их к целым числам, используйте метод img.astype('uint8'), который возвращает изображение в целых числах. 
Результат сохраните в файл out_img.png
"""

from skimage.io import imread, imsave
from numpy import histogram
import numpy as np


def find_minmax_pixels():
	img = imread('tiger-low-contrast.png')
	img = img.astype('float') # перевод диапазона в вещественные числа

	"""Подсчёт числа отбрасываемых пикселей"""
	k = round(img.size * 0.05)

	# Вытягивание массива пикселей
	extended_img = []
	for pixel_row in img:
		for pixel in pixel_row:
			extended_img.append(pixel)
	extended_img.sort()
	extended_img = np.array(extended_img)

	img_rescaled = extended_img[(k+1):-(k+1)] # отбрасываем пиксели

	xmin = img_rescaled[0]
	xmax = img_rescaled[-1]
	return img, xmin, xmax



def make_linear_brightness(img, xmin, xmax):
	"""Линейное выравнивание яркости"""
	img_contrast = (img - xmin) * (255 / (xmax - xmin)) # преобразование ко всему массиву img
	done_img = np.clip(img_contrast, 0, 255) # если пиксель < 0 -> поставить 0; если > 0 -> поставить 255
	done_img = done_img.astype('uint8')
	imsave('out.png', done_img)




minmax_pixels = find_minmax_pixels()
linear_brightness_equalization = make_linear_brightness(minmax_pixels[0], minmax_pixels[1], minmax_pixels[2])











