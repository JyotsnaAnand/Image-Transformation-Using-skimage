from skimage.color import rgb2gray
from skimage import data
import scipy.misc as ms

#Read input image file into an nd array using scipy's imread method
imgsource="doheny.jpg"
img = ms.imread(imgsource)

#Save the ndarray as a jpeg image file
ms.imsave('original1.jpeg', img)

#Apply color to grey scale transformation using skimage and save the ndarray as a jpeg image output
img_gray = rgb2gray(img)
ms.imsave('outfile1.jpeg', img_gray)
print(type(img))
