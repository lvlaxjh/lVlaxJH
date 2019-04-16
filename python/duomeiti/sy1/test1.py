
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage import exposure,data
from PIL import Image
#灰度处理----------------------------------------------------------------------
def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])


img = mpimg.imread('1.jpg')
gray = rgb2gray(img)
#显示原图----------------------------------------------------------------------
plt.imshow(gray, cmap=plt.get_cmap('gray'))
plt.show()
#显示灰度图----------------------------------------------------------------------
plt.imshow(img,cmap=plt.get_cmap('gray'))
plt.show()


#二值化处理----------------------------------------------------------------------
img = Image.open('1.jpg')

Img = img.convert('L')

# 自定义灰度界限，大于这个值为黑色，小于这个值为白色
threshold = 110

table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

#灰度处理----------------------------------------------------------------------
photo = Img.point(table, '1')
plt.imshow(photo,cmap=plt.get_cmap('gray'))
plt.show()
#photo.save("3.jpg")

#import numpy as np

#直方图计算----------------------------------------------------------------------
image =data.camera()*1.0
hist1=np.histogram(image, bins=2)   #用numpy包计算直方图
hist2=exposure.histogram(image, nbins=2)  #用skimage计算直方图
print(hist1)
print(hist2)
#绘制直方图----------------------------------------------------------------------
img2 = np.array(Image.open('1.jpg'))
plt.figure('zhilangtu')
arr = img2.flatten()
n, bins, patches = plt.hist(arr, bins=256, normed=1, facecolor='green', alpha=0.75)
plt.show()
