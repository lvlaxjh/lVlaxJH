
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage import exposure,data
from PIL import Image
import scipy
import cv2 as cv
#灰度处理----------------------------------------------------------------------
def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])


img = mpimg.imread('yuantu.jpg')
gray = rgb2gray(img)
scipy.misc.imsave('huidu1.jpg', gray)
#显示灰度图----------------------------------------------------------------------
#plt.imshow(gray, cmap=plt.get_cmap('gray'))
#plt.show()
#显示原图图----------------------------------------------------------------------
#plt.imshow(img,cmap=plt.get_cmap('gray'))
#plt.show()


# #二值化处理----------------------------------------------------------------------
img = Image.open('yuantu.jpg')

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
#plt.imshow(photo,cmap=plt.get_cmap('gray'))
#plt.show()
photo.save("erzhitu.jpg")

#直方图计算----------------------------------------------------------------------
image =data.camera()*1.0
hist1=np.histogram(image, bins=2)   #用numpy包计算直方图
hist2=exposure.histogram(image, nbins=2)  #用skimage计算直方图
print(hist1)
print(hist2)
#绘制直方图----------------------------------------------------------------------
img2 = np.array(Image.open('huidu1.jpg'))
plt.figure('zhilangtu')
arr = img2.flatten()
n, bins, patches = plt.hist(arr, bins=256, normed=1, facecolor='green', alpha=0.75)
plt.show()

from PIL import Image
from PIL import ImageEnhance

img = Image.open('huidu1.jpg')
img.show()

# 对比度增强
enh_con = ImageEnhance.Contrast(img)
contrast = 3
img_contrasted = enh_con.enhance(contrast)
img_contrasted.show()
img_contrasted.save("zhengqing1.jpg")

#绘制直方图----------------------------------------------------------------------
img2 = np.array(Image.open('zhengqing1.jpg'))
plt.figure('zhilangtu')
arr = img2.flatten()
n, bins, patches = plt.hist(arr, bins=256, normed=1, facecolor='green', alpha=0.75)
plt.show()


def zhifangtu(image):
    a = [0]*256       #创建储存像素数的一维数组
    w = image.size[0]#得到图像宽高
    h = image.size[1]
    #将图像转为矩阵
    data = image.getdata()
    data = np.matrix(data)
    data = np.reshape(data,(w,h))
    #计算灰度像素数
    for i in range(w):
        for j in range(h):
            gray = data[i, j]
            a[gray] += 1
    #以灰度为x轴像素数为y轴画直方图
    y = a
    x = [i for i in range(256)]
    plt.figure()
    plt.title("zhifangtu")
    plt.xlabel("Bins")
    plt.ylabel("Pixels")
    plt.plot(x,y)
    plt.xlim([0,256])
    return a



def junhenghua(a, image):  # 入口参数：灰度像素数和图片
    b = [0] * 256  # 储存个灰度像素占比数据
    c = [0] * 256  # 储存累计分布数据
    w = image.size[0]  # 得到图像宽高
    h = image.size[1]
    data = image.getdata()
    data = np.matrix(data)
    data = np.reshape(data, (w, h))
    mn = w * h * 1.0
    img = np.zeros([w, h], np.uint8)  # 创建空数组储存均衡化后数据

    # 计算灰度分布密度
    for i in range(len(a)):
        b[i] = a[i] / mn
    # 计算累计直方图数据
    for i in range(len(c)):
        if i == 1:
            c[i] = b[i]
        else:
            c[i] = c[i - 1] + b[i]
            a[i] = int(255 * c[i])
    # 对各灰度值进行均衡化映射
    for i in range(w):
        for j in range(h):
            img[i, j] = a[data[i, j]]
    for i in range(w):
        for j in range(h):
            gray = img[i, j]
            a[gray] += 1
        # 以灰度为x轴像素数为y轴画直方图
    y = a
    x = [i for i in range(256)]
    plt.figure()
    plt.title("junhenghua")
    plt.xlabel("Bins")
    plt.ylabel("Pixels")
    plt.plot(x, y)
    plt.xlim([0, 256])



im = Image.open('huidu1.jpg')
Lim = im.convert('L')
a = zhifangtu(Lim)  # 画原始图像直方图并得到灰度像素数
b = junhenghua(a, Lim)
plt.show()
