# -*- coding: utf-8 -*-

import time
import sys
import urllib.request
import requests
import json

def Use_Tl_xiaomai(_T_re_Chat,_inputs,_L1,_L2):#图灵---小麦
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
    #print('\nTuling: '+TL_str)#输出结果
    while True:
        TL1=_L2.readline().rstrip()
        TL2=_L2.readline().rstrip()
        #print(TL1)
        #print(TL2)
        #if TL1 == '#END#':
        #    break
        #if TL2 == '#END#':
        #    break
        #print(TL_str_xm)
        #print(TL2)
        if False:
            pass
        else:
            _L1.write(_inputs+'\n')
            _L1.write(TL_str_xm+'\n')
            break
        if not TL1:
            break
        if not TL2:
            break
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
    #http://www.tuling123.com/openapi/api?key=87490f6fe8f640d89b9f97c476a5dac4&info=***    
    

    
#if __name__=="__main__":
#    try:
#        sfile=open('SSlanguage1.txt','a+')
#        #print('open')
#    except OSError as reason:
#        print('Error'+str(reason))
#        time.sleep(3)
#        exit(1)

#    try:
#        afile=open('AAlanguage1.txt','a+')
#        #print('open')
#    except OSError as reason:
#        print('Error'+str(reason))
#        time.sleep(3)
#        exit(1)
#    while True:
#        I_input=input()
#        sfile.write('SS'+I_input)
#        sfile.write('\n')
#        tlstr=Use_Tl_xiaomai(I_input)
#        print(tlstr)
#        afile.write('AA'+tlstr)
#        afile.write('\n')
#        isbreak=input('~pass&~:(p)')
#        if isbreak=='p':
#            break
#    #print('~'+I_input)
#    flag=0
#    #while True:
#    #    flag+=1
#    #    print(flag)
#    #    TL_Str_xm=Use_Tl_xiaomai(I_input)
#    #    print('1~~~:'+TL_Str_xm)
#    #    sfile.write('SS'+TL_Str_xm)
#    #    sfile.write('\n')
#    #    time.sleep(1)
#    #    TL_Str_xmk=Use_Tl_xiaomaike(TL_Str_xm)
#    #    print('2~~~:'+TL_Str_xmk)
#    #    afile.write('AA'+TL_Str_xmk)
#    #    afile.write('\n')
#    #    time.sleep(1)
#    #    if flag==10:
#    #        break
#    sfile.close()
#    afile.close()