"""
Прочитайте изображение из файла img.png. У этого изображения нечетное количество строк и столбцов. 
Поменяйте цвет центрального пикселя этого изображения на зеленый цвет rgb (102, 204, 102) и сохраните изображение в файл out_img.png.

В примере входа и выхода указаны ссылки на файлы. Это сделано для вашего удобства. 
Вы можете скачать эти файлы, сохранить вход как img.png и протестировать решение на своем компьютере, сравнив с выходным изображением.
"""


from skimage.io import imread, imshow, imsave
import numpy as np

img = imread('img.png')
width = img.shape[0]  #ширина фото в пикселях
height = img.shape[1] #высота


#Находим центральный пиксель в изображении:
central_pixel_width = int((width - 1) / 2)
print(central_pixel_width)
central_pixel_height = int((height - 1) / 2)
print(central_pixel_height)
img[(central_pixel_width-3):(central_pixel_width+4), (central_pixel_height-7):(central_pixel_height+8)] = [102, 204, 102]
imsave('out_img.png', img)
