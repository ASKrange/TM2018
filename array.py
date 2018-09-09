from PIL import Image, ImageOps
import sys
import numpy as np
import matplotlib.pyplot as plt


i = Image.open(r'C:\Users\Gauthier Scherer\Desktop\info\TM\images\A3.jpg')
newi = ImageOps.grayscale(i)
tab = np.array(newi)
x,y = newi.size
largeur = x
hauteur = y

for h in range(hauteur):
    py = h
    for l in range(largeur):
        px =l
        print (px,py)
        couleur = newi.getpixel((px,py))
        print('pixel(',px,py,')=',couleur)
        if couleur < 200:
            print ('black')
        else:
            print('white')

plt.imshow(newi)
plt.show()
