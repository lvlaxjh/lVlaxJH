from aip import AipSpeech
import os
import mp3play



""" 你的 APPID AK SK """
APP_ID = '14237339'
API_KEY = 'PUmLG4e2WAWn6DOrScxwnnpc'
SECRET_KEY = 'aORMRa60PpdEcv6qXAXA4YMmK0G8XFuX'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result = client.synthesis('123456789', 'zh', 1, {
    'spd':'4',
    'pit':'5',
    'vol': '7',
    'per': '3'

})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)

os.system('auido.mp3')
