import msvcrt
from PIL import Image
import os
import errno
from os import listdir
from os.path import isfile, isdir

def ls1(path):    
    return [obj for obj in listdir(path) if isfile(path + obj)]

value = int(input("Quality: "));

f = open ('names.txt','wb')
f.close()

directorio = "Procesar/"
files=ls1("Procesar/")
for file in files:
    print(file)
    image_file = file
    file = open("names.txt", "a")
    file.write(image_file + '\n')
    file.close()
    
    #abrimos la imagen
    img = Image.open(f"{directorio}{image_file}")
     
    # cogemos la anchura y altura
    width, height = img.size
    print(img.size)

    direct = ["8m", "4m", "2m", "1m"]
    for i in direct:
        try:
            os.mkdir(i)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
            
        if i == "8m":
            nW = 8192
        elif i == "4m":
            nW = 4096
        elif i == "2m":
            nW = 2048
        elif i == "1m":
            nW = 1024
        
        aux = (height * nW)/width
        nH = int(aux)

        new_img = img.resize((nW,nH), Image.ANTIALIAS)

        new_img.save(i + "/" + image_file, optimize=True, quality = value)

        print(nW, nH)

msvcrt.getch()
