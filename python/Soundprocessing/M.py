# -*- coding: utf-8 -*-
import librosa
import matplotlib.pyplot as plt
import numpy as np
import librosa.display
from aip import AipSpeech

APP_ID = '14237339'
API_KEY = 'PUmLG4e2WAWn6DOrScxwnnpc'
SECRET_KEY = 'aORMRa60PpdEcv6qXAXA4YMmK0G8XFuX'

# 初始化AipSpeech对象
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
a=aipSpeech.asr(get_file_content('test3.wav'), 'wav', 16000, {

})
print(a)
# # 从URL获取文件识别
# aipSpeech.asr('', 'pcm', 16000, {
#     'url': 'http://121.40.195.233/res/16k_test.pcm',
#     'callback': 'http://xxx.com/receive',
# })