from PIL import Image, ImageDraw

def CreateImage(mytext):
    color = (0, 0, 120)
    img = Image.new('RGB', (130, 30), color)
    imgDrawer = ImageDraw.Draw(img)
    imgDrawer.text((10, 10), mytext)
    font = imgDrawer.getfont()
    print(font.getsize(mytext))
    img.save("test.png")

def ImageInfo():
    img = Image.open('test.png')  # открываем картинку
    size = img.size  # размер картинки
    format = img.format  # формат картинки
    mode = img.mode  # мод(RGBA...)

    print('Размер изображения: {}\nФормат изображения: {}\nЦветовая модель: {}'.format(size, format, mode))  # выводим массив

#CreateImage('This is my test 2:)')
ImageInfo()
