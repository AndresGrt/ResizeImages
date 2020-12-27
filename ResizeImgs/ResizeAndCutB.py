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

#try:
#    os.mkdir('Tools/gallery')
#except OSError as e:
#    if e.errno != errno.EEXIST:
#        raise

# Copia el archivo desde la ubicación actual a la
# carpeta "Documentos".
#shutil.copy("config.txt", "Tools/config.txt")
#shutil.copy("ruta.txt", "Tools/ruta.txt")
#shutil.copy("scenes.txt", "Tools/scenes.txt")
#shutil.copy("Readme.txt", "Tools/Readme.txt")

#f = open ('Tools/names.txt','wb')
#f.close()

directorio = "ProcesarB/"
files=ls1("ProcesarB/")

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
    
    
    #if count >= len(files):
    #    file = open("Tools/names.txt", "a")
    #    file.write(image_file )
    #    file.close()
    #else:
    #    file = open("Tools/names.txt", "a")
    #    file.write(image_file + '\n')
    #    file.close()
    
    
    #abrimos la imagen
    img = Image.open(f"{directorio}{image_file}")
    # img.save(f"{directorio}{image_file}", optimize = True, quality = 45)
    # cogemos la anchura y altura
    width, height = img.size
    print(img.size)

    folderImgOriginal = f"_{str(width)[0]}mb"

    direct = [folderImgOriginal, "_4mb", "_3mb", "_2mb", "_1mb", "_512b"]
    
    for i in direct:
        try:
            os.mkdir(f'Tools/{i}')
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        
        if i == folderImgOriginal:
            nW = int(width)
            w = 16
        elif i == "_4mb":
            nW = 4096
            w = 8
        elif i == "_3mb":
            nW = 3000
            w = 8
        elif i == "_2mb":
            nW = 2048
            w = 4
        elif i == "_1mb":
            nW = 1024
            w = 4
        elif i == "_512b":
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
                    path = f'Tools/{i}/{image_folder}/{x}_{y}({folderImgOriginal}).jpg'
                elif i == "_4mb":
                    path = f'Tools/{i}/{image_folder}/{x}_{y}(_4mb).jpg'
                elif i == "_3mb":
                    path = f'Tools/{i}/{image_folder}/{x}_{y}(_3mb).jpg'
                elif i == "_2mb":
                    path = f'Tools/{i}/{image_folder}/{x}_{y}(_2mb).jpg'
                elif i == "_1mb":
                    path = f'Tools/{i}/{image_folder}/{x}_{y}(_1mb).jpg'
                elif i == "_512b":
                    path = f'Tools/{i}/{image_folder}/{x}_{y}(_512b).jpg'
                    
                
                print (path)
                #region.save(path, optimize = True, quality = 45)
                region.save(path)
        
        print(nW, nH)
        
msvcrt.getch()
