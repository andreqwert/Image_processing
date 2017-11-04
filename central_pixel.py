from skimage.io import imread, imshow, imsave
import numpy as np

img = imread('img.png')
width = img.shape[0]  #ширина фото в пикселях
height = img.shape[1] #высота


#Находим центральный пиксель в изображении и меняем его цвет на зеленый:
central_pixel_width = int((width - 1) / 2)
print(central_pixel_width)
central_pixel_height = int((height - 1) / 2)
print(central_pixel_height)
img[central_pixel_width, central_pixel_height] = [102, 204, 102]
imsave('out_img.png', img)
