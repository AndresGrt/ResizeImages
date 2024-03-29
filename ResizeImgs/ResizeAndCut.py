import msvcrt
from PIL import Image
import os
import errno
from os import listdir
from os.path import isfile, isdir
import shutil

def ls1(path):    
    return [obj for obj in listdir(path) if isfile(path + obj)]

try:
    os.mkdir('Tools')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

try:
    os.mkdir('Tools/gallery')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

# Copia el archivo desde la ubicación actual a la
# carpeta "Documentos".
shutil.copy("config.txt", "Tools/config.txt")
shutil.copy("ruta.txt", "Tools/ruta.txt")
shutil.copy("scenes.txt", "Tools/scenes.txt")
shutil.copy("rotacionCamara.txt", "Tools/rotacionCamara.txt")
shutil.copy("rotaciones.txt", "Tools/rotaciones.txt")


f = open ('Tools/names.txt','wb')
f.close()

directorio = "Procesar/"
files=ls1("Procesar/")

count = 0

for file in files:
    count += 1
    print(len(files))

    indice = 0
    image_folder = ""
    while indice < len(file):
        if file[indice] == "_":
            break
        image_folder += file[indice]
        indice += 1

    print(image_folder)
    image_file = file

    if count >= len(files):
        file = open("Tools/names.txt", "a")
        file.write(image_file )
        file.close()
    else:
        file = open("Tools/names.txt", "a")
        file.write(image_file + '\n')
        file.close()
    
    
    #abrimos la imagen
    img = Image.open(f"{directorio}{image_file}")
    # img.save(f"{directorio}{image_file}", optimize = True, quality = 45)
    # cogemos la anchura y altura
    width, height = img.size
    print(img.size)

    folderImgOriginal = f"_{str(width)[0]}m"

    direct = [folderImgOriginal, "_4mA","_4mM","_4mL", "_3m", "_2m", "_1m", "_512"]
    
    for i in direct:
        try:
            os.mkdir(f'Tools/{i}')
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        
        if i == folderImgOriginal:
            nW = int(width)
            w = 16
        elif i == "_4mA":
            nW = 4096
            w = 16
        elif i == "_4mM":
            nW = 4096
            w = 8
        elif i == "_4mL":
            nW = 4096
            w = 4
        elif i == "_3m":
            nW = 3000
            w = 8
        elif i == "_2m":
            nW = 2048
            w = 4
        elif i == "_1m":
            nW = 1024
            w = 4
        elif i == "_512":
            nW = 512
            w = 4
        
        divide = w / 2
        h = int(divide)
        aux = (height * nW)/width
        nH = int(aux)

        if i == folderImgOriginal:
            new_img = img
        else:
            new_img = img.resize((nW,nH), Image.ANTIALIAS)

        try:
            os.mkdir(f'Tools/{i}/{image_folder}')
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

        ancho = int(new_img.size[0]/w)
        alto = int(new_img.size[1]/h)

        x = 0
        y = 0

        for si in range (h):
            x=x+1
            y=0
            for gh in range (w):
                y=y+1
                caja = (gh*ancho, si*alto, (gh*ancho) + ancho, (si*alto) + alto)
                print (caja)
                print ('tamaño: ' + str(new_img.size))
                region = new_img.crop(caja)
                if i == folderImgOriginal:
                    path = f'Tools/{i}/{image_folder}/{x}_{y}({folderImgOriginal}).webp'
                elif i == "_4mA":
                    path = f'Tools/{i}/{image_folder}/{x}_{y}(_4mA).webp'
                elif i == "_4mM":
                    path = f'Tools/{i}/{image_folder}/{x}_{y}(_4mM).webp'
                elif i == "_4mL":
                    path = f'Tools/{i}/{image_folder}/{x}_{y}(_4mL).webp'
                elif i == "_3m":
                    path = f'Tools/{i}/{image_folder}/{x}_{y}(_3m).webp'
                elif i == "_2m":
                    path = f'Tools/{i}/{image_folder}/{x}_{y}(_2m).webp'
                elif i == "_1m":
                    path = f'Tools/{i}/{image_folder}/{x}_{y}(_1m).webp'
                elif i == "_512":
                    path = f'Tools/{i}/{image_folder}/{x}_{y}(_512).webp'
                    
                
                print (path)
                region = region.convert('RGB')
                region.save(path, 'webp')
        
        print(nW, nH)
        
msvcrt.getch()
