from PIL import Image
import os
import errno

try:
    os.mkdir('recorte')
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

imagen = Image.open("c0.jpg")

ancho = int(imagen.size[0]/16)
alto = int(imagen.size[1]/8)

i = 0
j = 0

for si in range (8):
    i=i+1
    for gh in range (16):
        j=j+1
        caja = (gh*ancho, si*alto, (gh*ancho) + ancho, (si*alto) + alto)
        print (caja)
        print ('tamaño: ' + str(imagen.size))
        region = imagen.crop(caja)
        path = f'recorte/{i}_{j}'+'.png'
        print (path)
        region.save(path)
