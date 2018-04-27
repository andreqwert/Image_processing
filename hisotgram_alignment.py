"""
Выравнивание гистрограммы.

Когда применять: когда все пикселм похожи друг на друга и сложно визуально понять, что находится на изображении.

Функция распределения в таком случае очень неравномерна.
Задача состоит в том, чтобы сделать функцию распределения (cdf) равномерной, превратив ее в линейную.
Функция распределения имеет вид:
cdf(x) = h(0) + h(1) + h(2) + ... + h(x), где 0, 1, 2, .., x - пиксели изображения от 0 до 255.

Формула:
f(x) = round( 255 * (cdf(x) - cdf_min) / (кол-во_пикселей_в_изображений - 1) )
cdf_min - такое значение cdf(x), что cdf(x) != 0
"""


from skimage.io import imread, imsave
import skimage
import itertools
import numpy as np


def load_image(file_path):
    img = imread(file_path)
    return img


def count_pixels_num(img):
    return img.shape[0] * img.shape[1]


def make_histogram(img):
    """Функция принимает целое число 0, ..., 255 и возвращает количество пикселей с яркостью, равной аргументу"""

    h = np.zeros(256, np.uint32) # создаем массив из 256 нулей 
    for value in img.flatten(): # flatten returns a copy of the array collapsed into one dimension.
        h[value] += 1 # строим гистограмму
    return np.array(h)


def make_cdf(h):
    """Строим функцию распределения"""
    # Как работает itertools.accumulate:
    # 2 -> h(0) + h(1) + h(2)
    # 5 -> h(0) + h(1) + h(2) + h(3) + h(4) + h(5)
    # 179 -> h(0) + h(1) + ... + h(179)
    cdf = np.zeros(256, np.uint32) # массив из 256 нулей
    for value in range(256):
        cdf = list(itertools.accumulate(h)) # аккумулируем сумму
    return np.array(cdf)


def compute_cdf_min(cdf):
    """Вычисляем минимальное значение функции распределения (для формулы)"""
    values = sorted(list(set(cdf))) # удалили повторяющиеся значения
    for value in values:
        if values[0] == 0:
            min_cdf = values[1]
        else:
            min_cdf = values[0]
    return min_cdf


def align_histogram(img, min_cdf, pixels_num, output_name):
    """Применяем функцию выравнивания гистограммы"""

    aligned = img.copy()
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            pixel = img[x][y]
            aligned[x][y] = round(255 * (cdf[pixel] - min_cdf) / (pixels_num - 1))
    imsave('{}'.format(output_name), aligned)


image = load_image('landscape.png')
pixels_num = count_pixels_num(image)
hist = make_histogram(image)
cdf = make_cdf(hist)
min_cdf = compute_cdf_min(cdf)
aligned_image = align_histogram(image, min_cdf, pixels_num, 'aligned.png')


