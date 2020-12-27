import msvcrt
from PIL import Image
import os
import errno
from os import listdir
from os.path import isfile, isdir
import shutil

def ls1(path):    
    return [obj for obj in listdir(path) if isfile(path + obj)]

folder_1 = "PNGtoJPG/"
folder_2 = "Procesar/"
files=ls1("PNGtoJPG/")

for file in files:
    indice = 0
    image_jpg = ""
    while indice < len(file):
        if file[indice] == ")":
            break
        image_jpg += file[indice]
        indice += 1

    image_jpg += ").jpg"
    print(image_jpg)
    
    image_file = file
    
    #abrimos la imagen
    img = Image.open(f"{folder_1}{image_file}")

    img.convert('RGB').save(f"{folder_2}{image_jpg}","JPEG") #this converts png image as jpeg
       
os.system('python ResizeAndCut.py')
