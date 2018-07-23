import os

for file in os.scandir('e:/Foto/not_optimized/'):
    line = ''
    if file.is_file():
        line += 'файл'
        filename = file.name
        ext = filename[filename.rfind(".") + 1:]
    elif file.is_dir():
        line += 'папка'
        filename = ''
        ext = ''
    elif file.is_symlink():
        line += 'симлинк'
        filename = ''
        ext = ''
    print("{}\t{}\t\t{}".format(line, ext, filename))