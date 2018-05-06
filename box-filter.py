"""
Box-фильтр - нужен для размытия изображения.

Реализуйте box-фильтрацию изображения окном 5×5 пикселей. Дополнять изображение не нужно (т.е. изображение после фильтрации уменьшится).
Прочитайте изображение из файла img.png и сохраните результат фильтрации в файл out_img.png. 
"""


from skimage.io import imread, imsave, imshow, imshow_collection
import numpy as np
from scipy.signal import convolve2d
import skimage
import warnings
warnings.filterwarnings("ignore") 
import matplotlib.pyplot as plt


def load_image(file_path):
    img = imread(file_path)
    return img


image = load_image('/Users/user/Desktop/computer_vision/images/tiger_gray.png')
plt.figure(figsize=(5, 5))
convolved = convolve2d(skimage.color.rgb2gray(image), np.ones((5, 5)))
plt.imsave('out.png', convolved, cmap='gray')

