import msvcrt
from PIL import Image
import os
import errno
from os import listdir
from os.path import isfile, isdir

def ls1(path):    
    return [obj for obj in listdir(path) if isfile(path + obj)]

size_img = int(input("size: "));
value = int(input("Quality: "));

directorio = "Procesar/"
files=ls1("Procesar/")
for file in files:
    print(file)
    image_file = file
        
    #abrimos la imagen
    img = Image.open(f"{directorio}{image_file}")

    # cogemos la anchura y altura
    width, height = img.size
    print(img.size)
    
    nW = size_img
    aux = (height * nW)/width
    nH = int(aux)

    new_img = img.resize((nW,nH), Image.BILINEAR)

    new_img.save("Procesar/" + image_file, optimize=False, quality = value)

    print(nW, nH)

msvcrt.getch()
