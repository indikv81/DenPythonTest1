import tinify
import os
import json
import pandas
import pyexifinfo
from PIL import Image
from PIL.ExifTags import TAGS

def get_exif(fn):
    if pyexifinfo.check_if_this_file_exist(fn) == True:
        info.append(pyexifinfo.get_json(fn))
    #source = tinify.from_file("e:/Foto/" + x)
    #copyrighted = source.preserve("copyright", "creation", "location")
    #copyrighted.to_file("e:/Foto/Optimized/" + x)
    #print("Изображение - " + x + " успешно оптимизировано!")

tinify.key = "LC3QiqknWkCvmFVxAT6j1ZEPW7RwaeiY"
tinify.proxy = "http://10.15.1.24:8080"
info = []

if not os.path.exists("e:/Foto/not_optimized/"):
    os.mkdir("e:/Foto/not_optimized/")
if not os.path.exists("e:/Foto/optimized/"):
    os.mkdir("e:/Foto/optimized/")

images = os.listdir("e:/Foto/not_optimized/")
print('Найдено изображений: ' + str(len(images)))

for x in range(len(images)):
    print('Изображение ' + str(x + 1) + ': ' + images[x])
    get_exif("e:/Foto/not_optimized/" + images[x])

print(info)

    # return to JSON and have pandas build a csv
image_results_json = json.dumps(info)
data_frame = pandas.read_json(image_results_json)
csv = data_frame.to_csv('e:/Foto/optimized/results.csv')
print("[*] Данные записаны в results.csv")

print('Оптимизация изображений успешно завершена!')
compressions_this_month = tinify.compression_count
print('Количество оптимизаций за этот месяц: ' + str(compressions_this_month) + ' из 500')