from PIL import Image, ImageOps
import sys
import numpy as np

i = Image.open(r'C:\Users\Gauthier Scherer\Desktop\info\TM\images\acouleur.jpg')
newi = ImageOps.grayscale(i)
tab = np.array(newi)
print(newi.size)
print(tab)
couleur = newi.getpixel((1,1))
print(couleur)
newi.show()
i.show()
