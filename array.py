from PIL import Image, ImageOps
import sys
import numpy as np
import matplotlib.pyplot as plt


i = Image.open(r'C:\Users\Gauthier Scherer\Desktop\info\TM\images\A2.jpg')
newi = ImageOps.grayscale(i)
tab = np.array(newi)
x,y = newi.size
largeur = x
hauteur = y
# for h in range(hauteur) and l in range(largeur):
#     couleur = newi.getpixel((h,))
#     print(couleur)


plt.imshow(newi)
plt.show()
