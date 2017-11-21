"""
Прочитайте изображение из файла img.png. Примените к нему линейное выравнивание яркости: примените к каждому пикселю функцию.
После вычисления функции значения изображения окажутся вещественными. Чтобы привести их к целым числам, используйте метод 
img.astype('uint8'), который возвращает изображение в целых числах. Результат сохраните в файл out_img.png.
"""

from skimage.io import imread, imsave, imshow
from numpy import histogram
import numpy as np
import matplotlib.pyplot as plt
from skimage import img_as_float



def pixel_min_max_brightness():
    """Найдем пиксели с минимальной и максимальной яркостями"""
    img = imread('tiger-low-contrast.png')

    values, bin_edges = histogram(img, bins=range(257))

    # Сначала вычисляем, для каких яркостей вообще имеются пиксели
    num_pix_higher0 = []
    for bright in values: 
        if bright > 0:
            num_pix_higher0.append(bright)

    #values, bin_edges, patches = plt.hist(img.ravel(), bins=range(257)) #bins - границы гистограммы
    #plt.xlabel(u'ЯРКОСТЬ')
    #plt.ylabel(u'КОЛИЧЕСТВО ПИКСЕЛЕЙ')
    #plt.show()

    min_br = values.tolist().index(num_pix_higher0[0]) # посмотрим на гистрограмму: наименее яркие пиксели - слева
    max_br = values.tolist().index(num_pix_higher0[-1]) # а наиболее яркие - справа
    return img, min_br, max_br



def f(img, min_br, max_br):
    #width = img.shape[0]
    #height = img.shape[1]

    img_contrast = (img - min_br) * (255 / (max_br - min_br)) # преобразование ко всему массиву img
    img_i = img_contrast.astype('uint8') # перевод из вещественных в целые числа
    imsave('123.png', img_i)


pixels_min_max_bright = pixel_min_max_brightness()
f(pixels_min_max_bright[0], pixels_min_max_bright[1], pixels_min_max_bright[2])
