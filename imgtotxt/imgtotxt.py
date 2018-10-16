# -*- coding: utf-8 -*-

from aip import AipOcr

# 定义常量
APP_ID = '14407442'
API_KEY = 'VQTrvnsND3KH3GFpG5HXkmG8'
SECRET_KEY = 'ziT27q1IgKQbFeAqNK2BBFPCyqaVwEiq'

# 初始化文字识别分类器
aipOcr=AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
filePath = "1.png"

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 定义参数变量
options = {
    'detect_direction': 'true',
    'language_type': 'CHN_ENG',
}

# 网络图片文字文字识别接口
result = aipOcr.webImage(get_file_content(filePath),options)
print(result)
# 如果图片是url 调用示例如下
# result = apiOcr.webImage('http://files.eduuu.com/img/2017/01/04/185716_586cd50caffdc.png')

