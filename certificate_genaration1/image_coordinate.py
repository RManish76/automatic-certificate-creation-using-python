#%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#import numpy as np
#from PIL import Image
img =mpimg.imread("D:\certificate_genaration\Certificate-sender\Template.jpg")
print(img)
imgplot = plt.imshow(img)
plt.show()
