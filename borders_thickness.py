"""Загрузите изображение из файла img.png. Изображение состоит из рамки сплошного цвета и внутренней части изображения. 
Цвет рамки можно узнать, посмотрев на левый верхний пиксель. Рамка может иметь разную ширину со всех четырех сторон. 
Определите размеры рамки и выведите эти размеры через пробел. Размеры рамки выводите в следующем порядке: левый, верхний, правый, нижний."""



from skimage.io import imread, imshow, imsave
import numpy as np


img = imread('tiger-border.png')


def remove_borders(img):
    border = [0, 0, 0, 0] #граница ЛЕВАЯ ВЕРХНЯЯ ПРАВАЯ НИЖНЯЯ
    width = img.shape[0]  #ширина фото в пикселях
    height = img.shape[1] #высота
    #print(width, height)
    #print(img.shape)

    #Посмотрим на число, кодирующее цвет левого верхнего пикселя (рамки)
    border_color = img[0, 0]  # [ 81 243 165]

    for i in range(width): # Цикл идет СЛЕВА 
        for j in range(height): # Цикл идет СВЕРХУ
            if not np.array_equal(img[i,j], border_color): # если вдруг пиксели стали не равны зеленому цвету...
                # обозначаем место, где прошла граница между зеленым и незеленым
		left = width - i - 1  # граница СЛЕВА
		top = height - j - 1  # граница СВЕРХУ


    for k in reversed(range(width)): # Цикл идет СПРАВА
        for l in reversed(range(height)): # Цикл идет СНИЗУ
            if not np.array_equal(img[k,l], border_color): # если вдруг пиксели стали не равны зеленому цвету...
		right = k # граница СПРАВА
		bottom = l # граница СНИЗУ

    border = list(reversed([left, top, right, bottom]))
    print('Left, Top, Right, Bottom: ')
    for i in border:
        print(i, end=' ')


remove_borders(img)

