from skimage.color import rgb2gray
from skimage import data
import scipy.misc as ms

'''
img = data.astronaut()
scipy.misc.imsave('original1.jpeg', img)
img_gray = rgb2gray(img)
scipy.misc.imsave('outfile1.jpeg', img_gray)
'''


imgsource="doheny.jpg"
#ms.imsave('pic.png', imgsource) # First we need to create the PNG file
img = ms.imread(imgsource)
ms.imsave('original1.jpeg', img)
img_gray = rgb2gray(img)
ms.imsave('outfile1.jpeg', img_gray)
print(type(img))