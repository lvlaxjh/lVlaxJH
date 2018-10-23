# -*- coding: utf-8 -*-

import time
import sys
import urllib.request
import requests
import json

def Use_Tl_xiaomai(_T_re_Chat,_inputs,_L1,_L2, _Return_li):#图灵---小麦
    #API_KEY='87490f6fe8f640d89b9f97c476a5dac4'
    #API_URL='http://openapi.tuling123.com/openapi/api/v2'
    API_KEY='fb8fcc789ef4473bb96e790b45a07832'
    API_URL='http://openapi.tuling123.com/openapi/api/v2'
    info = _inputs#输入信息
    url = 'http://www.tuling123.com/openapi/api?key='+API_KEY+'&info='+info
    res = requests.get(url)#得到网页HTML代码
    res.encoding = 'utf-8'#防止中文乱码
    jd = json.loads(res.text)#将得到的json格式的信息转换为Python的字典格式
    TL_str_xm=jd['text']
    # print('\nTuling: '+TL_str)#输出结果
    flag_bool=True
    for chat in _Return_li:
        if TL_str_xm==chat:
            flag_bool=False

    if flag_bool!=False:
        _L1.write(_inputs+'\n')
        _L1.write(TL_str_xm+'\n')
    flag_bool = True
    return TL_str_xm
    #http://www.tuling123.com/openapi/api?key=fb8fcc789ef4473bb96e790b45a07832&info=***
    
def Use_Tl_xiaomaike(_inputs):#图灵---小麦可
    API_KEY='87490f6fe8f640d89b9f97c476a5dac4'
    API_URL='http://openapi.tuling123.com/openapi/api/v2'
    while True:
        info = _inputs#输入信息
        url = 'http://www.tuling123.com/openapi/api?key='+API_KEY+'&info='+info
        res = requests.get(url)#得到网页HTML代码
        res.encoding = 'utf-8'#防止中文乱码
        jd = json.loads(res.text)#将得到的json格式的信息转换为Python的字典格式
        TL_str_xmk=jd['text']
        #print('\nTuling: '+TL_str)#输出结果
        return TL_str_xmk


def Use_Tl_xiaomaikesi(_inputs):  # 图灵---麦克斯
    API_KEY = '7b84344e82ba4409a9e99b1abf0386c2'
    API_URL = 'http://openapi.tuling123.com/openapi/api/v2'
    while True:
        info = _inputs  # 输入信息
        url = 'http://www.tuling123.com/openapi/api?key=' + API_KEY + '&info=' + info
        res = requests.get(url)  # 得到网页HTML代码
        res.encoding = 'utf-8'  # 防止中文乱码
        jd = json.loads(res.text)  # 将得到的json格式的信息转换为Python的字典格式
        TL_str_xmk = jd['text']
        # print('\nTuling: '+TL_str)#输出结果
        return TL_str_xmk

if __name__=="__main__":
   chat=input()
   maikesi=Use_Tl_xiaomaikesi(chat)
   print(maikesi)
   f=open(r'txt\\yuliao.txt', 'a+', encoding='UTF-8')
   f.write(chat+'\n')
   flag=0
   while True:
       flag+=1
       # time.sleep(1)
       xiaomaike=Use_Tl_xiaomaike(maikesi)
       print(xiaomaike)
       maikesi=Use_Tl_xiaomaikesi(xiaomaike)
       print(maikesi)
       f.write(xiaomaike+'\n')
       f.write(maikesi+'\n')
       if flag==50:
           break;