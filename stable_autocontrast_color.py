from skimage.io import imread, imsave
from numpy import dstack
import numpy as np
from skimage import img_as_float, img_as_ubyte
import warnings
warnings.simplefilter("ignore")


def use_stable_autocontrast():

    img = imread('tiger-color.png')

    # 1. Перевод диапазона в вещественные числа
    img = img_as_float(img) 

    """2. Перевод изображения в пространство YUV"""
    r = img[:, :, 0]
    g = img[:, :, 1]
    b = img[:, :, 2]

    y =  0.2126*r + 0.7152*g + 0.0722*b
    u = -0.0999*r - 0.3360*g + 0.4360*b
    v =  0.6150*r - 0.5586*g - 0.0563*b

    """3. Найдём мин. и макс. для устойчивого автоконтраста с отбрасыванием 5% самых светлых и самых темных пикселей"""
    xmin, xmax = find_minmax_pixels(y)

    """4. Применим линейное растяжение канала Y по формуле"""
    y_contrast = make_linear_brightness(y, xmin, xmax)

    """5. Обрежем значения канала y от 0 до 1"""
    y_rescaled = np.clip(y_contrast, 0, 1)

    # 6. Переведём изображение в пространство RGB
    r = y_rescaled + 1.2803*v 
    g = y_rescaled - 0.2148*u - 0.3805*v
    b = y_rescaled + 2.1279*u
    img_rgb = dstack((r, g, b))

    # 7. Обрежем значения изображения от 0 до 1
    img_rgb = np.clip(img_rgb, 0, 1)

    # 8. Переведём изображение в целые числа от 0 до 255
    img_rgb = img_as_ubyte(img_rgb)
    imsave('out_img.png', img_rgb)


def find_minmax_pixels(y):

    """Подсчёт числа отбрасываемых пикселей (5%)"""
    k = round(y.size * 0.05)

    # Вытягивание массива пикселей
    extended_img = []
    for pixel_row in y:
        for pixel in pixel_row:
            extended_img.append(pixel)
    extended_img = np.array(extended_img)
    extended_img.sort()
    

    img_rescaled = extended_img[k:-k] # отбрасываем пиксели

    xmin = img_rescaled[0]
    xmax = img_rescaled[-1]
    return xmin, xmax



def make_linear_brightness(y, xmin, xmax):
    """Линейное выравнивание яркости"""

    y_contrast = (y - xmin) * (1 / (xmax - xmin)) # преобразование ко всему массиву y
    return y_contrast




use_stable_autocontrast()











