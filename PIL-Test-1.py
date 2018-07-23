from PIL import Image, ImageDraw
import random

def generate_image():
    image_width = 200
    image_height = 100
    image = Image.new("1", (image_width, image_height), (0))

    for y in range(100):
        for x in range(200):
            color = 1 if random.randrange(0,255) > 127 else 0
            image.putpixel([x, y],color)
    image.save("image.png")

def get_image():

    image = Image.open("image.png")
    image_width, image_height = image.size
    #image.save('result.png')
    byteset = ""
    for x in range(0,image_width):
        for y in range(0, image_height):
            if image.getpixel((x, y)) > 127:
                byteset += '1'
            else:
                byteset += '0'
    print(int(byteset))
    print(int(byteset, 2).bit_length())



def main():
    print("Загрузить изображение (0) или генерировать изображение (1) ?")
    choice = int(input())
    if choice > 1:
        main()
    else:
        if choice == 0:
            get_image()
        else:
            generate_image()


if __name__ == '__main__':
    main()