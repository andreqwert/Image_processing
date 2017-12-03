"""
Прочитайте изображение из файла img.png. Подсчитайте минимум и максимум яркости для стабильного автоконтраста этого изображения. 
Необходимо отбросить 5% самых светлых и 5% самых темных пикселей. Для получения числа отбрасываемых пикселей используйте формулу
k=round(#pix⋅0.05)
k=round(#pix⋅0.05)
Два посчитанных числа (минимум и максимум) выведите на стандартный вывод через пробел.
"""

from skimage.io import imread, imsave, imshow
#from numpy import histogram
#from skimage import img_as_float, img_as_ubyte



def compute_minmax_autocontrast():
    img = imread('tiger-low-contrast.png')
    #img_f = img_as_float(img) # перевод диапазона в вещественные числа


    """Подсчёт числа отбрасываемых пикселей"""
    k = round(img.size * 0.05)
    print(k)


    # Отбросим k пикселей самых светлых и k пикселей самых тёмных
    # Для этого вытянем все значения яркостей пикселей в список и отсортируем
    extended_img = []
    for pixel in img:
        for pixel_brightness in pixel:
            extended_img.append(pixel_brightness)
    extended_img.sort()
    xmin = extended_img[k+1] # Значение (k+1) отсортированного пикселя
    xmax = extended_img[-(k+1)] # Значение (k+1) пикселя с конца
    print('%s %s' % (xmin, xmax))



minmax_autocontrast = compute_minmax_autocontrast()
