
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#传入的直方图要求是个字典，每个灰度对应着概率
def drawHist(hist,name):
    keys = hist.keys()
    values = hist.values()
    x_size = len(hist)-1#x轴长度，也就是灰度级别
    axis_params = []
    axis_params.append(0)
    axis_params.append(x_size)

    #plt.figure()
    if name != None:
        plt.title(name)
    plt.bar(tuple(keys),tuple(values))#绘制直方图
    #plt.show()

def arrayToHist(grayArray,nums):
    if(len(grayArray.shape) != 2):
        print("length error")
        return None
    w,h = grayArray.shape
    hist = {}
    for k in range(nums):
        hist[k] = 0
    for i in range(w):
        for j in range(h):
            if(hist.get(grayArray[i][j]) is None):
                hist[grayArray[i][j]] = 0
            hist[grayArray[i][j]] += 1
    #normalize
    n = w*h
    for key in hist.keys():
        hist[key] = float(hist[key])/n
    return hist

#直方图匹配函数，接受原始图像和目标灰度直方图
def histMatch(grayArray,h_d):
    #计算累计直方图
    tmp = 0.0
    h_acc = h_d.copy()
    for i in range(256):
        tmp += h_d[i]
        h_acc[i] = tmp

    h1 = arrayToHist(grayArray,256)
    tmp = 0.0
    h1_acc = h1.copy()
    for i in range(256):
        tmp += h1[i]
        h1_acc[i] = tmp
    #计算映射
    M = np.zeros(256)
    for i in range(256):
        idx = 0
        minv = 1
        for j in h_acc:
            if (np.fabs(h_acc[j] - h1_acc[i]) < minv):
                minv = np.fabs(h_acc[j] - h1_acc[i])
                idx = int(j)
        M[i] = idx
    des = M[grayArray]
    return des



imdir = "./cat.JPG"
imdir_match = "./cat.JPG"

#直方图匹配
#打开文件并灰度化
im_s = Image.open(imdir).convert("L")
im_s = np.array(im_s)
print(np.shape(im_s))
#打开文件并灰度化
im_match = Image.open(imdir_match).convert("L")
im_match = np.array(im_match)
print(np.shape(im_match))
#开始绘图
plt.figure()

#原始图和直方图
plt.subplot(2,3,1)
plt.title("img")
plt.imshow(im_s,cmap='gray')

plt.subplot(2,3,4)
hist_s = arrayToHist(im_s,256)
drawHist(hist_s,"his")

#match图和其直方图
plt.subplot(2,3,2)
plt.title("match img")
plt.imshow(im_match,cmap='gray')

plt.subplot(2,3,5)
hist_m = arrayToHist(im_match,256)
drawHist(hist_m,"match his")

#match后的图片及其直方图
im_d = histMatch(im_s,hist_m)#将目标图的直方图用于给原图做均衡，也就实现了match
plt.subplot(2,3,3)
plt.title("after match img")
plt.imshow(im_d,cmap='gray')

plt.subplot(2,3,6)
hist_d = arrayToHist(im_d,256)
drawHist(hist_d,"after match img")

plt.show()


#-----------------------------------------------------------------------------------
#均值滤波
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图片
img = cv2.imread('./lena_noise.bmp')
source = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 均值滤波
result = cv2.blur(source, (5, 5))

# 显示图形
titles = ['Source Image', 'Blur Image']
images = [source, result]
for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

#box模板
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图片
img = cv2.imread('./lena_noise.bmp')
source = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 方框滤波
result = cv2.boxFilter(source, -1, (5, 5), normalize=0)

# 显示图形
titles = ['Source Image', 'BoxFilter Image']
images = [source, result]
for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
#plt.show()

#高斯滤波
# encoding:utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图片
img = cv2.imread('./lena_noise.bmp')
source = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 高斯滤波
result = cv2.GaussianBlur(source, (3, 3), 0)

# 显示图形
titles = ['Source Image', 'GaussianBlur Image']
images = [source, result]
for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

#中值滤波
# encoding:utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图片
img = cv2.imread('./lena_noise.bmp')

# 高斯滤波
result = cv2.medianBlur(img, 3)

# 显示图像
cv2.imshow("source img", img)
cv2.imshow("medianBlur", result)

# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()